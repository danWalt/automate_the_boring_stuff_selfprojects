#! python3
# websiteURL.py - find websites that start with http:// or https:// from
# clipboard.
# works with .com or .co.## domains. www. isn't necessary
import pyperclip, re

urlRegex = re.compile(r'''(
    (https:\/\/|http:\/\/)      # get the beginning of a website URL
    (www\.)?                 # world wide web, doesn't have to contain this
    (\w+\.)                    # website URL
    (com|co\.\w{2})                  # domain
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in urlRegex.findall(text):
    matches.append(groups[0])

if len(matches) == 0:
    print("no website URLs were found in the given text")
else:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
