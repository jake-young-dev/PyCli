#imports
import http.client
#import json
from urllib.parse import urlparse

#path;parameters?query#fragment

def get(url, port):
    # print()
    # print("Requesting: " + url)

    link = urlparse(url)

    connection = None
    if port == None:
        if link.scheme == "https":
            connection = http.client.HTTPSConnection(link.hostname, http.client.HTTPS_PORT, timeout=10)
        elif link.scheme == "http":
            connection = http.client.HTTPConnection(link.hostname, http.client.HTTP_PORT, timeout=10)
    else:
        if link.scheme == "https":
            connection = http.client.HTTPSConnection(link.hostname, port, timeout=10)
        elif link.scheme == "http":
            connection = http.client.HTTPConnection(link.hostname, port, timeout=10)

    reqPath = link.path 
    if link.params != "":
        reqPath += ";" + link.params
    if link.query != "":
        reqPath += "?" + link.query
    if link.fragment != "":
        reqPath += "#" + link.fragment
    
    connection.request("GET", reqPath)
    res = connection.getresponse()

    # print(str(res.status) + " " + res.reason)

    if res.status == 301:
        newurl = res.getheader("Location")
        print("Redirected to: " + newurl)
        return get(newurl, port)

    body = None
    checkpoint = res.read()
    try:
        body = checkpoint.decode()
    except UnicodeDecodeError:
        # print("Decode error, returning raw body")
        body = checkpoint
    connection.close()

    return str(res.status) + " " + res.reason, body


def post(url, port, body):
    # print()
    # print("Posting to: " + url)
    
    link = urlparse(url)

    connection = None
    if port == None:
        if link.scheme == "https":
            connection = http.client.HTTPSConnection(link.hostname, http.client.HTTPS_PORT, timeout=10)
        elif link.scheme == "http":
            connection = http.client.HTTPConnection(link.hostname, http.client.HTTP_PORT, timeout=10)
    else:
        if link.scheme == "https":
            connection = http.client.HTTPSConnection(link.hostname, port, timeout=10)
        elif link.scheme == "http":
            connection = http.client.HTTPConnection(link.hostname, port, timeout=10)

    reqPath = link.path 
    if link.params != "":
        reqPath += ";" + link.params
    if link.query != "":
        reqPath += "?" + link.query
    if link.fragment != "":
        reqPath += "#" + link.fragment

    connection.request("POST", reqPath, body)
    res = connection.getresponse()

    # print(str(res.status) + " " + res.reason)
    body = str(res.read().decode())
    connection.close()

    return str(res.status) + " " + res.reason, body