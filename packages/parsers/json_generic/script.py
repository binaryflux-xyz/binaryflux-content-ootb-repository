import json

def parse(data: str):
    return json.loads(data)  # will raise JSONDecodeError on failure
