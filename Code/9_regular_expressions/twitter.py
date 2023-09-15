'''

To clean up URL input leaving only user name

'''

import re

url = input('URL > ').strip()

# Replace URL with only user name using methon:

# username = url.replace('https://twitter.com/', '')

# print(f' user name:{username}')

# Using removeprefix method of string:

# username = url.removeprefix('https://twitter.com/')

# print(f' user name: {username}')

# with re.sub:

# username = re.sub(r'https://twitter.com/', '', url)
# print(username)

# Tidy up few of the more obvious errors that can occur
# add ^ to start so starts from begninning add \ before the . as this is also a reserved word
# add question mark after https to allow for http
# tolerate www. being added remember to escape the . and add parentheses ? to say optional
# make the https:// or http:// optional parenthesise and add question mark to make optional

# username = re.sub(r'(^https?)?://(www\.)?twitter\.com/', '', url)
# print(username)

# Doing the same with re.search() so that it can be added to a conditional

# if matches := re.search(r'^(https?://)?(www\.)?twitter\.com/(.+)$', url, re.IGNORECASE):
#     print(f'User name: {matches.group(3)}')

# # Using non-capturing parentheses:
# if matches := re.search(r'^(?:https?://)?(?:www\.)?twitter\.com/(.+)$', url, re.IGNORECASE):
#     print(f'User name: {matches.group(1)}')

# To allow for an extra / or other characters beyond the user name:

# Using non-capturing parentheses:
# Using non-capturing parentheses:
if matches := re.search(r'^(?:https?://)?(?:www\.)?twitter\.com/(\w+)', url, re.IGNORECASE):
    print(f'User name: {matches.group(1)}')