import os
import json
import boto3
from PIL import Image
from io import BytesIO
import av

def remove_exif_from_image(file_content):
    img = Image.open(BytesIO(file_content))
    img = img.convert('RGB')

    # Save the image without EXIF data
    output = BytesIO()
    img.save(output, format='JPEG', quality=95)
    output.seek(0)

    return output

def remove_metadata_from_video(file_content):
    input_container = av.open(BytesIO(file_content), mode='r')
    output = BytesIO()
    output_container = av.open(output, mode='w')

    for stream in input_container.streams:
        output_stream = output_container.add_stream(stream.codec.name, stream.rate)
        for packet in input_container.demux(stream):
            for frame in packet.decode():
                packet = output_stream.encode(frame)
                if packet:
                    output_container.mux(packet)
        output_stream.encode(None)
    output_container.close()
    output.seek(0)

    return output

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Download the file
    s3_object = s3.get_object(Bucket=bucket, Key=key)
    file_content = s3_object['Body'].read()

    # Process the image or video and remove EXIF data
    if key.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')):
        output = remove_exif_from_image(file_content)
    elif key.lower().endswith(('.mp4', '.mkv', '.avi', '.mov', '.webm', '.flv')):
        output = remove_metadata_from_video(file_content)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Unsupported file format.')
        }

    # Upload the processed file
    new_bucket = os.environ['NEW_BUCKET'] if os.environ.get('NEW_BUCKET') else bucket
    s3.put_object(Bucket=new_bucket, Key=key, Body=output)

    return {
        'statusCode': 200,
        'body': json.dumps('File processed and uploaded.')
    }