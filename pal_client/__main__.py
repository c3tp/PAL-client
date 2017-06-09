import sys
import argparse


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print("This is the main routine.")
    print("It should do something interesting.")
    parser = argparse.ArgumentParser()

    parser.add_argument('command', help='pre_upload/pre_download/upload/download')
    parser.add_argument('bucket')
    parser.add_argument('key')
    parser.add_argument('--username', default="lol", help='username help')
    parser.add_argument('--password', default="wut")
    parser.add_argument('--dummy-auth', default=True, action="store_true")
    args = vars(parser.parse_args())
    print("Hi! we tried parsing")
    if args['dummy_auth'] is False:
        # TODO(Andreas): We'll do real auth eventually
        return

    result = {
        'pre_upload': lambda b, k: pal_presigned.get_presigned_upload(client, b, k),
        'pre_download': lambda b, k: pal_presigned.get_presigned_download(client, b, k)
    }[args['command']](args['bucket'], args['key'])
    return result
    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.

if __name__ == "__main__":
    main()