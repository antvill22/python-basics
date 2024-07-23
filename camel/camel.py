camel_case=input("camelCase:")
snake_case=""
for c in camel_case:
    if c.isupper():
        snake_case += "_"+c.casefold()
    else:
        snake_case += c

snake_case = snake_case.lstrip("_")

print("snake_case:",snake_case)