# coding: utf-8

import requests


class Sms:
    """
    Get list or send new SMS via android grunt http api
    """

    def __init__(self, host):
        self.url = 'http://%s:8080/sms' % host

    def send(self, phone, message):
        try:
            r = requests.post(
                self.url,
                data={'phone': phone, 'message': message}
            )
            result = r.json()
            return result['status'] == 'success'
        except requests.exceptions.RequestException as e:
            print e.getMessage()
            return False

    def list(self):
        try:
            r = requests.get(self.url)
            r.encoding = 'utf-8'
            return r.json()
        except requests.exceptions.RequestException as e:
            print e.getMessage()
            return []
