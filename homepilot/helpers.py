import requests

class SessionHelper:
    _session = requests.Session()
    
    @classmethod
    def current(cls):
        return cls._session

def raise_http_exception(name: str, res: requests.Response) -> None:
    raise Exception(f"Could not execute '{name}': HTTP response code: {res.status_code}\nMessage: {res.text}")

def clean_base_url(base_url: str) -> str:
    return base_url.strip('/')