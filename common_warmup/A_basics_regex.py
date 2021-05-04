# regex
import re

# substitution
#

my_string = 'The envrionment we live, in is rather hostile! BE AWARE @#$*('
x = re.sub('\W+', ' ', my_string)
print(x)
