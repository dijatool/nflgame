

def nflcom_http_wrapper( url, timeout = 0 ) :
    '''
        check encoding
    '''
    resp = urllib2.urlopen( url, timeout = timeout )
    encoding = resp.info().get( 'Content-Encoding', None )
    if encoding == 'gzip' :
        import zlib
        page = zlib.decompress( resp.read(), 16 + zlib.MAX_WBITS )
    else :
        page = resp.read()
    return page


