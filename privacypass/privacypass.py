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


def redemption_token(token, url, method):
    key = _get_mac_key(token)

    parsed_uri = urlparse(url)
    hostname = parsed_uri.hostname
    path = parsed_uri.path

    binding = create_request_binding(key, [bytes(hostname, 'utf-8'), bytes(f"{method} {path}", 'utf-8')])

    contents = [b64encode(bytes(token.get('input'))).decode('utf-8'),
                binding.decode('utf-8'),
                b64encode(json.dumps(defaultECSettings, separators=(',', ':')).encode('utf-8')).decode('utf-8')]

    redemption_dict = {'type': 'Redeem', 'contents': contents}
    json_string = json.dumps(redemption_dict, separators=(',', ':'))
    redemption_token = b64encode(json_string.encode('utf-8'))
    return redemption_token.decode('utf-8')  # return str not bytes
