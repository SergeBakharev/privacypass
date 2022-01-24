import json
from base64 import b64encode
from logging import error
from urllib.parse import urlparse

from .voprf import create_request_binding, derive_key

defaultECSettings = {"curve": 'p256',
                     "hash": 'sha256',
                     "method": 'increment'}


def _get_mac_key(token):
    if token['signed'] is None:
        error('Unsigned token is used to derive a MAC key')

    return derive_key(token.get('signed').get('unblindedPoint'), token.get('input'))


def redemption_token(token, url: str, method: str) -> str:
    """Creates a Privacy Pass redemption token

Args:
    token: A single Privacy Pass CF-Token dict
    url: URL being requested
    method: HTTP verb that will be used with the token. Eg. GET or POST

Return:
    str: Redemption token
    """
    key = _get_mac_key(token)

    parsed_uri = urlparse(url)

    hostname = parsed_uri.hostname
    path = parsed_uri.path

    if hostname is None:
        raise ValueError("Valid URL must be provided")

    binding = create_request_binding(key, [bytes(hostname, 'utf-8'), bytes(f"{method} {path}", 'utf-8')])

    contents = [b64encode(bytes(token.get('input'))).decode('utf-8'),
                binding.decode('utf-8'),
                b64encode(json.dumps(defaultECSettings, separators=(',', ':')).encode('utf-8')).decode('utf-8')]

    redemption_dict = {'type': 'Redeem', 'contents': contents}
    json_string = json.dumps(redemption_dict, separators=(',', ':'))
    redemption_token = b64encode(json_string.encode('utf-8'))
    return redemption_token.decode('utf-8')  # return str not bytes


def redemption_header(token, url: str, method: str) -> dict:
    """Returns a request header with appropriate redemption token

Args:
    token: A single Privacy Pass CF-Token dict
    url: URL being requested
    method: HTTP verb that will be used with the token. Eg. GET or POST

Return:
    dict: Header with challenge-bypass-token token
    """
    token = redemption_token(token=token, url=url, method=method)
    return {'challenge-bypass-token': token}
