import argparse
import sys

# Reference:
#   http://www.o365atp.com/
#   view-source:http://www.o365atp.com/o365atp.js


def copyToClipboard(string):
    import subprocess
    import platform
    string = string.strip()
    platform = platform.system()
    
    if platform == 'Windows':
        # windows shell
        clipcmd = 'clip'
    elif platform == 'Darwin':
        # mac bash?
        clipcmd = 'pbcopy'
    else:
        raise ValueError(f'{plarform=} : Unassigned copy command for current platform.')

    cmd = f'echo {string}|{clipcmd}'
    return subprocess.check_call(cmd, shell=True)

def safelinkDecode(url):
    from urllib import parse
    data = parse.urlparse(url)
    query = data.query
    if not query:
        raise ValueError(f'tried to parse {url}: \n\tno valid query string in the given url')
    queryfragment = [i.split('=') for i in query.split('&')]
    qkeys, qvals = tuple(zip(*queryfragment))
    qvals = map(parse.unquote, qvals)
    queryfragment = dict(zip(qkeys, qvals))
    return queryfragment

if __name__ == '__main__':
    if len(sys.argv) == 1:
        args = {
            'url': '',
            'd': False,
            's': False
            }

        args['url'] = input('target url: ')
        if type(args['url']) is not str or len(args['url']) < 3:
            raise ValueError(f'url cannot be empty.')

    else:
        parser = argparse.ArgumentParser('python o365sl.py', description='Decode Outlook365 safelink url.')
        parser.add_argument('url', type=str, help='Target URL', default='')
        parser.add_argument('--d', help='disable copy to cLipboard', action='store_true')
        parser.add_argument('--s', help='silent mode', action='store_true')
        args = parser.parse_args()

        if args.d and args.s:
            raise ValueError('clipboard is disabled and silent mode is enabled, btw.')
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
