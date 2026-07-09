import re
def condition(event):
    regex_ip  = r"(?:\d{1,3}\.){3}\d{1,3}"
    pattern = re.compile(regex_ip)
    match = pattern.search(event.get('host'))

    return True if event.get('host') is not None and (match or 'AD' in event.get('host')) else False
   