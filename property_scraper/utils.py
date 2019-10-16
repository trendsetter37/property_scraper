# -*- coding: utf-8 -*-

from boto3 import Session

from fake_useragent import UserAgent

ro_creds = Session().get_credentials().get_frozen_credentials()
ua = UserAgent()

def get_random_useragent():
    return ua.random


def get_credentials():
    return ro_creds.access_key, ro_creds.secret_key
