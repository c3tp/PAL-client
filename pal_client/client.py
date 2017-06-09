#!/usr/bin/env python
"""Create API For presigned URLS to objects"""

import requests

TARGET_URL = 'http://localsite:5000'


def download_file(b, k, username, password, target):
    url = url_join(TARGET_URL, b, k, 'presigned_url')
    response = requests.post(
        url=url,
        data={
            'username': username,
            'password': password
        }
    )
    presigned_url = response.text
    response = requests.get(presigned_url)
    with open(target, "wb") as target_file:
        target_file.write(response.content)

    print("hi")
    return response


def upload_file(b, k, username, password, target):
    url = url_join(TARGET_URL, b, k, 'presigned_post')
    response = requests.post(
        url=url,
        data={
            'username': username,
            'password': password
        }
    )
    files = {"file": open(target, 'rb')}
    data = response.json()
    return requests.post(
        data["url"],
        data=data["fields"],
        files=files)


def symlink(b, k, username, password, target):
    url = url_join(TARGET_URL, b, k, 'symlink')
    return requests.post(
        url=url,
        data={
            'username': username,
            'password': password,
            'target': target
        }
    )


def url_join(*args):
    return "/".join(map(lambda x: str(x).rstrip('/'), args))
