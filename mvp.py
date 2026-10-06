'''
MVP: Takes URL in → Spits shorter URL out

Components: (Added as I need them)
- random string generator to generate the shortened URL
- a hashmap to store all the shortened URL -> original URL pairs
- common domain name
'''

import random
import string

URLmappings = {}
slug = set()

domain = 'smoll'


def randomStringGenerator(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def URLgenerator(customDomain=None, alias=None):
    if alias is None:
        while True:
            randString = randomStringGenerator(7)
            if randString in slug:
                continue
            else:
                slug.add(randString)
                break
    return f"https://{customDomain if customDomain is not None else domain}/{alias if alias is not None else randString}"




def main():
    ogURL = str(input("Enter Your Long URL: "))

    while True:
        alias = str(input("Enter Your Alias (Optional): "))
        if alias in slug:
            print("Alias already taken")
            continue
        else:
            slug.add(alias)
            break
    customDomain = str(input("Enter Your Custom Domain (Optional): "))

    if len(alias) == 0:
        alias = None
    if len(customDomain) ==0:
        customDomain = None

    shortURL = URLgenerator(customDomain=customDomain, alias=alias)

    URLmappings[shortURL] = ogURL

    print(URLmappings)
    print("Short URL stored in the mapping")
 
main()
    