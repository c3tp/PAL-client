#!/usr/bin/env python
"""Create API For presigned URLS to objects"""

import requests

TARGET_URL = '127.0.0.1:5000'

def build_request():
    requests.post(
        url=TARGET_URL,
        body={
            'username': 'hi',
            'password': 'dude'
        }
    )
    