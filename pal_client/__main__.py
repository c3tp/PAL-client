import sys
import argparse
import pal_client.client


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print("This is the main routine.")
    print("It should do something interesting.")
    parser = argparse.ArgumentParser()

    parser.add_argument('command', help='upload/download/symlink')
    parser.add_argument('bucket')
    parser.add_argument('key')
    parser.add_argument('target')
    parser.add_argument('--username', default="lol", help='username help')
    parser.add_argument('--password', default="wut")
    parser.add_argument('--dummy-auth', default=True, action="store_true")
    args = vars(parser.parse_args())
    print("Hi! we tried parsing")
    if args['dummy_auth'] is False:
        # TODO(Andreas): We'll do real auth eventually
        return

    return {
        'download': pal_client.client.download_file,
        'upload': pal_client.client.upload_file,
        'symlink': pal_client.client.symlink
    }[args['command']](
        args['bucket'],
        args['key'],
        args['username'],
        args['password'],
        args['target']
        )


if __name__ == "__main__":
    main()