# vim: fileencoding=utf-8

from urllib import urlencode
from urllib2 import urlopen, Request

QUERY = u'Медведь с балалайкой'

if __name__ == '__main__':
    url = 'http://google.com/search?' + urlencode({'q': QUERY})
    #url = 'http://google.com/search?' + urlencode({'q': QUERY.encode('utf-8')})
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    print urlopen(request).read()[:200]


