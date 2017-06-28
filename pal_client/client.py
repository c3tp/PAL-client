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
    response = requests.get(presigned_url, verify=False)
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
    presigned_url = response.text
    with open(args['target'], 'rb') as data_in:
        upload = requests.put(presigned_url, data=data_in.read(), verify=False)
        upload.close()
    return response


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


def restrict(**args):
    url = url_join(args['target_url'], args['bucket'], args['key'], 'restrict')
    response = requests.post(
        url=url,
        data={
            'username': args['username'],
            'password': args['password']
        },
        verify=False
    )

    return response.text


def release(**args):
    url = url_join(args['target_url'], args['bucket'], args['key'], 'release')
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
