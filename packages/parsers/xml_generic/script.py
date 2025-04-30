import xml.etree.ElementTree as ET

def parse(data: str):
    root = ET.fromstring(data)  # will raise ParseError if invalid
    return {root.tag: {child.tag: child.text for child in root}}
