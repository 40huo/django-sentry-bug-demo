from rest_framework.test import RequestsClient


def run():
    c = RequestsClient()
    resp = c.get(url='http://testserver/')
    print(resp.text)
