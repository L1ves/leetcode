import base64

def to_base_64(string):
    string_encode = base64.b64encode(string.encode('ascii'))
    return string_encode.decode('utf-8').replace('=', '')

def from_base_64(string):
    # Add padding to the string
    padded_string = string + '=' * (-len(string) % 4)
    string_decode = base64.b64decode(padded_string)
    return string_decode.decode('utf-8')