import xml.etree.ElementTree as ET

def parse(data: str):
    root = ET.fromstring(data)
    ns = {'ns': root.tag.split('}')[0].strip('{')}
    header = root.find('.//ns:GrpHdr', ns)
    if header is None:
        raise ValueError("pain.001 format does not contain GrpHdr")
    return {
        "MsgId": header.findtext('ns:MsgId', default="", namespaces=ns),
        "CreDtTm": header.findtext('ns:CreDtTm', default="", namespaces=ns),
        "NbOfTxs": header.findtext('ns:NbOfTxs', default="", namespaces=ns)
    }
