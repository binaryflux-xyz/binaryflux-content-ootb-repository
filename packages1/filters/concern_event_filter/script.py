def condition(event):
    if event.get('event_level') == "error" or event.get('event_level') == "critical" or event.get('event_level') == "warning":
        return True
    else:
        return False
