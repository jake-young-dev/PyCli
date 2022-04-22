#imports
import http.client
from urllib.parse import urlparse

#path;parameters?query#fragment

def get(url):
    link = urlparse(url)
    
    connection = None
    if link.scheme == 'https':
        connection = http.client.HTTPSConnection(link.hostname, http.client.HTTPS_PORT, timeout=10)
    elif link.scheme == 'http':
        connection = http.client.HTTPConnection(link.hostname, http.client.HTTP_PORT, timeout=10)
    else:
        print("PROB")

    reqPath = link.path 
    if link.params != "":
        reqPath += ";" + link.params
    if link.query != "":
        reqPath += "?" + link.query
    if link.fragment != "":
        reqPath += "#" + link.fragment
    
    connection.request("GET", reqPath)
    res = connection.getresponse()

    body = res.read().decode()
    connection.close()

    return str(res.status), body



status, body = get("https://www.youtube.com/playlist?list=PL5WG4doTSrXSzrzgMa2HiLdqOnlBynVEH")
print(status)
print(body)