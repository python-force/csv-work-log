import re
search_time = "1"
i = "1"
x = "r'\\b{}\\b'".format(i)
print(x)
formula = re.compile(r'\b{0}\b'.format(i))
found = re.search(formula, i)
print(found)
x = "r'\\b" + "1" + "\\b'"
print(x)

try:
    re.compile('def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):')
    is_valid = True
except re.error:
    is_valid = False

print(is_valid)