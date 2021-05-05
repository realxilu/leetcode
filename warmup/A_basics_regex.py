# https://docs.python.org/3/library/re.html

import re

# substitution

my_string = 'The WORLD we live, in is RatheR hoStile!** BE AWARE @#$*('
x = re.sub('\W+', ' ', my_string)
print(x)

# matching TODO

