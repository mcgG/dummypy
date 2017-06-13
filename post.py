import time
import urllib2
boundary = '----------%s' % hex(int(time.time() * 1000))

data = []
data.append('--%s' % boundary)


def upload(filename):
    f = open(filename, 'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('files', filename))
    data.append('Content-Type: %s\r\n' % 'multipart/form-data')
    data.append(f.read())
    f.close()
    data.append('--%s--\r\n' % boundary)

    http_url = 'http://127.0.0.1:3000/form'
    http_body = '\r\n'.join(data)
    try:
        print http_body
        req = urllib2.Request(http_url, data = http_body)
        print 'haha'
        #header
        req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
        req.add_header('User-Agent', 'Mozilla/5.0')
        req.add_header('Referer', 'http://127.0.0.1:3000')
        #post data to server
        res = urllib2.urlopen(req, timeout=5)
        qrcont = res.read()
        print qrcount
    except Exception, e:
        print 'error!'
