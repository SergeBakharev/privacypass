import base64
import hmac
from hashlib import sha256

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

# Verifiable Oblivious Pseudorandom Function


def derive_key(unblindedPoint, token):
    """
Derives the shared key used for redemption MACs

Input:
unblindedPoint - Signed curve point associated with token
token - client-generated token data

Return: bytes of derived key
    """

    tagBytes = bytes('hash_derive_key', 'utf-8')

    h = hmac.new(key=tagBytes, digestmod=sha256)

    # Always compute derived key using uncompressed point bytes
    point = ec.EllipticCurvePublicKey.from_encoded_point(curve=ec.SECP256R1(), data=base64.b64decode(unblindedPoint))  # SECP256R1 is NIST p-256
    encodedPoint = point.public_bytes(Encoding.X962, PublicFormat.UncompressedPoint)

    tokenBytes = bytes(token)
    pointBytes = bytes(encodedPoint)

    h.update(tokenBytes)
    h.update(pointBytes)

    keyBytes = h.digest()
    return keyBytes


def create_request_binding(key, data):
    tagBits = bytes('hash_request_binding', 'utf-8')  # the exact bytes of the string "hash_request_binding"
    hash = sha256

    h = hmac.new(key=key, digestmod=hash)
    h.update(tagBits)

    for element in data:
        h.update(element)

    return base64.b64encode(h.digest())
