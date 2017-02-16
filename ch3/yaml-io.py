import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

import yaml

customer = [
    { "name": "Yamada", "age": "35", "gender": "man" },
    { "name": "Sato", "age": "58", "gender": "woman" },
    { "name": "Kato", "age": "42", "gender": "man" },
    { "name": "Nishi", "age": "22", "gender": "man" }
]

yaml_str = yaml.dump(customer)
print(yaml_str)
print("--- --- ---")

data = yaml.load(yaml_str)

for p in data:
    print(p["name"])
