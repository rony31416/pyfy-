import json

data = '{"name": "Rony", "age": 23}'
parsed = json.loads(data)

print(parsed['name'])  # Rony


from collections import Counter

text = "hello world"
counter = Counter(text)

print(counter)  # Counts each character
