import boto3
import io
import os
from PIL import Image
from moviepy.editor import *

def lambda_handler(event, _):
    bucket_name = os.environ['S3_BUCKET_NAME']
    s3 = boto3.client('s3')
    object_name = event['Records'][0]['s3']['object']['key']
    file_name, file_extension = os.path.splitext(object_name)
    
    supported_image_extensions = ['.jpg', '.jpeg', '.png', '.tiff', '.tif', '.heic', '.heif']
    supported_video_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.webm']
    
    image_data = s3.get_object(Bucket=bucket_name, Key=object_name)

    if file_extension.lower() in supported_image_extensions:
        with io.BytesIO(image_data['Body'].read()) as image_file:
            image = Image.open(image_file)
            image_format = image.format
            
            with io.BytesIO() as new_image_data:
                image.save(new_image_data, format=image_format)
                new_image_data.seek(0)
                
                s3.put_object(Bucket=bucket_name, Key=object_name, Body=new_image_data, Tagging='ExifDeleted=True')

    elif file_extension.lower() in supported_video_extensions:
        with io.BytesIO(image_data['Body'].read()) as video_file:
            video = VideoFileClip(video_file)
            with io.BytesIO() as new_video_data:
                video.write_videofile(new_video_data, codec='libx264', audio_codec='aac')
                new_video_data.seek(0)
                
                s3.put_object(Bucket=bucket_name, Key=object_name, Body=new_video_data, Tagging='ExifDeleted=True')