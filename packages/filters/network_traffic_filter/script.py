def condition(event):
    if event.get('log_type') == "traffic" :
        return True
    else:
        return False