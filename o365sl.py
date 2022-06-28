from src.o365safelink import safelinkDecode
from src.utils import copyToClipboard
import argparse
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        args = {
            'url': '',
            'd': False,
            's': False
            }

        args['url'] = input('target url: ')
        if type(args['url']) is not str or len(args['url']) < 3:
            raise Exception(f'url cannot be empty.')

    else:
        parser = argparse.ArgumentParser('python o365sl.py', description='Decode Outlook365 safelink url.')
        parser.add_argument('url', type=str, help='Target URL', default='')
        parser.add_argument('--d', help='disable copy to cLipboard', action='store_true')
        parser.add_argument('--s', help='silent mode', action='store_true')
        args = parser.parse_args()

        if args.d and args.s:
            raise Exception('clipboard is disabled and silent mode is enabled, btw.')
        args = dict(args._get_kwargs())

    parsed_value = safelinkDecode(args['url'])

    if not args['s']:
        print('\n', f'Parsed Value:','\n')
        for k, v in parsed_value.items():
            print(f'{k} = {v}')

    if not args['d']:
        errno = copyToClipboard(parsed_value['url'])
        if not errno:
            print()
            print(f'Copied to clipboard: \'{parsed_value["url"]}\'')
