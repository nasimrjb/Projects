import re
pattern = re.compile(r'\d{3} \d{3}-\d{4}')
res = pattern.search('call me at 415 555-4242!')
