import json

with open('./opt/config.json') as f:
    config = json.loads(f.read())
print(config)