import json

def parse(data: str):
    stix_json = json.loads(data)
    return {
        "type": stix_json["type"],
        "id": stix_json["id"],
        "objects": stix_json.get("objects", [])
    }
