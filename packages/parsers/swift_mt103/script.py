import re

def parse(data: str):
    matches = re.findall(r":([0-9A-Z]{2,}):([^\n\r]+)", data)
    if not matches:
        raise ValueError("Invalid MT103 format")
    return {tag: value.strip() for tag, value in matches}
