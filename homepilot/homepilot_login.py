import requests
import hashlib
import json
import encodings

from homepilot.helpers import raise_http_exception, clean_base_url, SessionHelper

SUBADDRESS_LOGIN = '/authentication/login'
SUBADDRESS_GET_SALT = '/authentication/password_salt'

s = SessionHelper.current()

def get_salt(base_url: str) -> str:
    get_salt_path = clean_base_url(base_url) + SUBADDRESS_GET_SALT
    res = s.post(get_salt_path)

    if res.ok:
        json_content = res.json()

        return json_content['password_salt']
    else:
        raise_http_exception('get_salt', res)

def login_homepilot(base_url: str, password: str) -> None:
    salt = get_salt(base_url)
    login_path = clean_base_url(base_url) + SUBADDRESS_LOGIN
    
    password_hash_stage1 = salt + hashlib.sha256(password.encode('utf8')).hexdigest()
    password_hash_stage2 = hashlib.sha256(password_hash_stage1.encode('utf8')).hexdigest()

    login_json = {
        'password': password_hash_stage2,
        'password_salt': salt
    }

    res = s.post(login_path, json=login_json)

    if res.ok:
        return True
    else:
        raise_http_exception('login', res)

