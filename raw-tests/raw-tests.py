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


i = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
x = input("Type the patter")
print(x)
formula = re.compile(x)
found = re.search(formula, i)
print(found)


search_data = input("Enter a string you looking for: ")
x = r'\b{0}\b'
found = re.search(x.format(search_data), i)
print(found)


# Edit Record: Validate the Date
# Time Spent: Integer

