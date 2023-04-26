# 🎞️ EXIF Metadata Remover 📸

![Python](https://img.shields.io/badge/Python-3.8-blue) ![License](https://img.shields.io/badge/license-GNU-green)

**EXIF Metadata Remover** is a super cool 😎 Python script to remove EXIF metadata from your images 🖼️ and videos 📹 stored in an AWS S3 bucket. It's lightweight, efficient, and easy to use! Get rid of those pesky EXIF data and protect your privacy! 🛡️

## 🚀 Features

-   Supports multiple image formats: `.jpg`, `.jpeg`, `.png`, `.tiff`, `.tif`, `.heic`, `.heif`
-   Supports multiple video formats: `.mp4`, `.mov`, `.avi`, `.mkv`, `.webm`
-   AWS Lambda ready! ⚡

## 📦 Requirements

-   Python 3.8 or higher
-   `boto3` (AWS SDK for Python)
-   `Pillow` (Python Imaging Library)
-   `moviepy` (Video editing library)

## 🛠️ Installation

1.  Clone the repo:
`git clone https://github.com/flightlesstux/EXIF-Metadata-Remover.git` 
-   Install the required packages:
2.  `pip3 install -r requirements.txt` 
3.  Replace `your-bucket-name` with the actual name of your S3 bucket, and `your-function-name` with the name of your Lambda function. This policy allows the Lambda function to read and write objects in the specified S3 bucket, invoke the Lambda function, and write logs to CloudWatch Logs.
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::your-bucket-name/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "lambda:InvokeFunction"
      ],
      "Resource": "arn:aws:lambda:*:*:function:your-function-name"
    }
  ]
}

```
4.  Set the `S3_BUCKET_NAME` environment variable to the name of your AWS S3 bucket.
    

## 🎯 Usage

1.  Upload an image or video to your S3 bucket.
2.  The script automatically processes the file and removes the EXIF metadata.
3.  The cleaned file is saved back to the S3 bucket with a tag `ExifDeleted=True`.
    

## 📖 License

This project is licensed under the GNU GENERAL PUBLIC LICENSE License. See the [LICENSE](https://github.com/flightlesstux/EXIF-Metadata-Remover/blob/main/LICENSE) file for more information.

## Published On
[Secure Your Media Files by Removing Metadata with AWS Lambda](https://ercanermis.com/secure-your-media-files-by-removing-metadata-with-aws-lambda/)