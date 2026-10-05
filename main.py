'''
MVP: Takes URL in → Spits shorter URL out

Components: (Added as I need them)
- random string generator to generate the shortened URL
- a hashmap to store all the shortened URL -> original URL pairs
- common domain name
'''

import random
import string

store = {}
domain = 'smoll'


def randomStringGenerator(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def URLgenerator(customDomain=None, alias=None):
    if alias is None:
        randString = randomStringGenerator(7)
    return f"https://{customDomain if customDomain is not None else domain}/{alias if alias is not None else randString}"

    