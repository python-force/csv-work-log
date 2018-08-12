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