#!/usr/bin/env python
"""Create API For presigned URLS to objects"""

import requests


def download_file(pal_url, bucket_name, object_key):
    return s3_client.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket_name,
            'Key': object_key
        })


def get_presigned_upload(s3_client, bucket_name, object_key):
    # TODO(Andreas):
    return s3_client.generate_presigned_post(
        Bucket=bucket_name,
        Key=object_key
    )


def build_symlink(s3_client, bucket_name, object_key, target_link):
    response = s3_client.put_object(
        Body=str.encode(target_link),
        Key=object_key,
        Bucket=bucket_name,
        Metadata={
            'symlink': target_link
        }
    )
    return response
