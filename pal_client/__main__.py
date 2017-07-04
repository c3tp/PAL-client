import sys
import argparse
import pal_client.client
DEFAULT_URL = 'http://localsite:5000'


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()

    parser.add_argument('command', help='upload/download/symlink')
    parser.add_argument('bucket')
    parser.add_argument('key')
    parser.add_argument('--target')
    parser.add_argument('--username', default="lol", help='username help')
    parser.add_argument('--password', default="wut")
    parser.add_argument('--dummy-auth', default=True, action="store_true")
    parser.add_argument('--mount-point')
    parser.add_argument('--target-url')
    args = vars(parser.parse_args())
    if args['dummy_auth'] is False:
        # TODO(Andreas): We'll do real auth eventually
        return

    if args['target_url'] is None:
        args['target_url'] = DEFAULT_URL
    result = {
        'download': pal_client.client.download_file,
        'upload': pal_client.client.upload_file,
        'symlink': pal_client.client.symlink,
        'presigned_get': pal_client.client.presigned_get,
        'presigned_post': pal_client.client.presigned_post,
        'restrict': pal_client.client.restrict,
        'release': pal_client.client.release
    }[args['command']](**args)
    return result

if __name__ == "__main__":
    main()