# Application logic

import random
import string
from database import checkAlias, addNew

default_domain = 'smoll'

'''
Function generates a random string consisting of small and capital
letters and digits. Length of the random string can be defined.
'''
def randomStringGenerator(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))


'''
Function takes long URL and optionally a custom domain and/or alias 
and produces the final shortened URL
'''
def URLgenerator(str: longURL, customDomain=None, alias=None):
    if alias is None:
        while True:
            randString = randomStringGenerator(7)
            if checkAlias(alias=alias) is None:
                break
            else:
                continue
    shortURL = f"https://{customDomain if customDomain is not None else default_domain}/{alias if alias is not None else randString}"

    addNew(longURL=longURL, customDomain=customDomain, alias=alias, shortURL=shortURL)
    
