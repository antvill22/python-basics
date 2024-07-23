import string
s = "HELLO!"
punct = string.punctuation
for c in punct:
    s = s.replace(c, "").strip().casefold()
#out = "".join([i for i in s if i not in string.punctuation])
"""
punct = string.punctuation
for c in punct:
    s = s.replace(c, "")
"""
print(s)