# BEGIN NUMERICS_DEMO
import unicodedata
import re

re_digit = re.compile(r'\d')

sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

for char in sample:
    print('U+%04x' % ord(char),                       # <1>
          char.center(6),                             # <2>
          '{:6}'.format('re_dig' if re_digit.match(char) else '-'),  # <3>
          '{:6}'.format('isdig' if char.isdigit() else '-'),         # <4>
          '{:6}'.format('isnum' if char.isnumeric() else '-'),       # <5>
          '{:6}'.format(format(unicodedata.numeric(char), '5.2f')),  # <6>
          unicodedata.name(char),                     # <7>
          sep='\t')
# END NUMERICS_DEMO
