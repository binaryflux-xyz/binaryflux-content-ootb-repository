#Add your code here
def window():
    return None

def groupby():
    return None

def algorithm(event):
    if 'DELETE FROM' or 'DROP TABLE' in event.get('argument', ''):
        return 1.0
    return 0.0

def context(event_data):
    argument = event_data.get('argument', '')
    
    if 'DELETE FROM' in argument:
        return "{} was executed without WHERE clause to delete the table".format(argument)
    elif 'DROP TABLE' in argument:
        return "{} was executed without WHERE clause to drop the table".format(argument)


def criticality():
    return 'Critical'

def tactic():
    return 'Impact (TA0040)'

def technique():
    return 'Data Destruction (T1485)'

def artifacts():
    return stats.collect(['user_host', 'command_type'])

def entity(event):
    return {'derived': False, 'value': event['user_host'], 'type': 'hostname'}