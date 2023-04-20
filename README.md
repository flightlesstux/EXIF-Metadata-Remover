
# EXIF Metadata Remover

This Python script is designed to remove EXIF metadata from images and other metadata from videos. The script can be used as an AWS Lambda function to process files automatically as they are uploaded to an S3 bucket.

## Requirements

-   Python 3.6 or later
-   [Pillow](https://pillow.readthedocs.io/en/stable/) library
-   [PyAV](https://pyav.org/) library
-   [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) library

## How to use

To use this script, you can simply copy and paste it into your Python environment or editor. The script includes a `lambda_handler` function, which can be used as an AWS Lambda function to process files automatically as they are uploaded to an S3 bucket.

Before deploying the script as an AWS Lambda function, you will need to ensure that the following environment variables are set:

-   `NEW_BUCKET`: the name of the S3 bucket where the processed files will be uploaded.

To run the script locally, you can modify the `lambda_handler` function to accept a local file path instead of an S3 object key.

## How it works

The `remove_exif_from_image` function removes EXIF metadata from an image file. The function uses the [Pillow](https://pillow.readthedocs.io/en/stable/) library to open the image, convert it to RGB format, and save it as a new image without EXIF data.

The `remove_metadata_from_video` function removes metadata from a video file. The function uses the [PyAV](https://pyav.org/) library to open the video, iterate over each packet in each stream, decode the packets into frames, and encode the frames into new packets without metadata.

The `lambda_handler` function is the entry point for the AWS Lambda function. The function downloads the file from S3, determines whether it is an image or video file, and calls the appropriate function to remove metadata. The function then uploads the processed file to S3.

## Creating a custom Lambda layer

If you want to create a custom Lambda layer for this script, you can follow these steps:

1.  Create a new folder for your layer.
2.  Install the required libraries (`Pillow`, `PyAV`, and `boto3`) using pip and the `--target` flag to install the libraries in the folder you created:

1.  `pip install Pillow PyAV boto3 --target /path/to/your/layer/folder` 
    
2.  Copy the `remove_exif_from_image` and `remove_metadata_from_video` functions into a new Python file in the folder.
3.  Create an empty `__init__.py` file in the folder.
4.  Zip the contents of the folder (including the `__init__.py` file) into a file called `layer.zip`.
5.  Upload the `layer.zip` file to a new Lambda layer in your AWS account.

You can then reference the Lambda layer in your AWS Lambda function to use the `remove_exif_from_image` and `remove_metadata_from_video` functions without needing to include the libraries in your deployment package.
