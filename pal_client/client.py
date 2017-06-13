#!/usr/bin/env python
"""Create API For presigned URLS to objects"""

import requests

TARGET_URL = 'http://localsite:5000'


def download_file(**args):
    url = url_join(TARGET_URL, args['bucket'], args['key'], 'presigned_url')
    response = requests.post(
        url=url,
        data={
            'username': args['username'],
            'password': args['password']
        }
    )
    presigned_url = response.text
    response = requests.get(presigned_url)
    with open(args['target'], "wb") as target_file:
        target_file.write(response.content)

    return response


def upload_file(**args):
    url = url_join(TARGET_URL, args['bucket'], args['key'], 'presigned_post')
    response = requests.post(
        url=url,
        data={
            'username': args['username'],
            'password': args['password']
        }
    )
    files = {"file": open(args['target'], 'rb')}
    data = response.json()
    return requests.post(
        data["url"],
        data=data["fields"],
        files=files)


def symlink(**args):
    url = url_join(TARGET_URL, args['bucket'], args['key'], 'symlink')
    return requests.post(
        url=url,
        data={
            'username': args['username'],
            'password': args['password'],
            'target': args['target'],
            'mount_point': args['mount_point']
        }
    )


def url_join(*args):
    return "/".join(map(lambda x: str(x).rstrip('/'), args))
