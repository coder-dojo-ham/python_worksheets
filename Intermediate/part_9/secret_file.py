import base64


def write_secret(filename, secret):
    encoded_secret = base64.encodebytes(bytes(secret))
    with open(filename, 'wb') as new_secret:
        new_secret.write(encoded_secret)


def read_secret(filename):
    with open(filename, 'rb') as secret:
        for line in secret:
            print(base64.decodebytes(line))
