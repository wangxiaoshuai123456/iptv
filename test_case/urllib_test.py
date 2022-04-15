import urllib
from urllib.request import urlopen
import urllib.robotparser

try:
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url("http://www.musi-cal.com/robots.txt")
    rp.read()
    rrate = rp.request_rate("*")
    # print('rrate.requests:', rrate.requests)
    # print('rrate.seconds:', rrate.seconds)

    ret = rp.crawl_delay("*")
    print(ret)

    ret = rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco")
    print(ret)

    ret = rp.can_fetch("*", "http://www.musi-cal.com/")
    print(ret)

    decode_url = urllib.parse.urlparse('https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B')
    print('decode_url', decode_url)

    # encode_url = urllib.request.quote("https://www.runoob.com/")
    # print('encode_url:', encode_url)
    # decode_url = urllib.request.unquote(encode_url)
    # print(decode_url)

    url = "https://www.runoob.com/try/py3/py3_urllib_test.php"
    data = {'name': 'RUNOOB', 'tag': '菜鸟教程'}
    data = urllib.parse.urlencode(data).encode('utf8')

    header = {'User-Agent': \
                  'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    request = urllib.request.Request(url, data=data, headers=header)
    response = urllib.request.urlopen(request).read()

    # my_url = urlopen("https://www.runoob.com/")
    # print("code:", my_url.getcode())
    with open('../data/urllib_test.html', 'wb') as file:
        # content = my_url.read()
        file.write(response)
        file.close()

except urllib.error.HTTPError as err:
    if err.code == 404:
        print("页面不存在：", err.code)
