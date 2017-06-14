#!/usr/bin/env python
"""Create API For presigned URLS to objects"""

import requests


def download_file(**args):
    if args['target'] is None:
        return "Download file needs a target parameter to save file to"
    url = url_join(args['target_url'], args['bucket'], args['key'], 'presigned_get')
    response = requests.post(
        url=url,
        data={
            'username': args['username'],
            'password': args['password']
        },
        verify=False
    )
    presigned_url = response.text
    response = requests.get(presigned_url)
    with open(args['target'], "wb") as target_file:
        target_file.write(response.content)

    return response


def upload_file(**args):
    if args['target'] is None:
        return "upload file needs a target parameter to choose file to save"
    url = url_join(args['target_url'], args['bucket'], args['key'], 'presigned_post')
    response = requests.post(
        url=url,
        data={
            'username': args['username'],
            'password': args['password']
        },
        verify=False
    )
    files = {"file": open(args['target'], 'rb')}
    presigned_url = response.text
    return requests.post(
        presigned_url,
        files=files,
        verify=False)


def presigned_get(**args):
    url = url_join(args['target_url'], args['bucket'], args['key'], 'presigned_get')
    response = requests.post(
        url=url,
        data={
            'username': args['username'],
            'password': args['password']
        },
        verify=False
    )

    return response.text


def presigned_post(**args):
    url = url_join(args['target_url'], args['bucket'], args['key'], 'presigned_post')
    response = requests.post(
        url=url,
        data={
            'username': args['username'],
            'password': args['password']
        }
    )
    return response.text


def symlink(**args):
    if args['target'] is None:
        return "symlink needs a target file directory to symlink to"
    url = url_join(args['target_url'], args['bucket'], args['key'], 'symlink')
    return requests.post(
        url=url,
        data={
            'username': args['username'],
            'password': args['password'],
            'target': args['target'],
            'mount_point': args['mount_point']
        },
        verify=False
    )


def url_join(*args):
    return "/".join(map(lambda x: str(x).rstrip('/'), args))
