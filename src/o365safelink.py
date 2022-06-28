# Reference:
#   http://www.o365atp.com/
#   view-source:http://www.o365atp.com/o365atp.js

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
