def window():
    return None
def groupby():
    return None
def algorithm(event):
    if event['event_id'] == 4698:
        return 0.8
    return None
def context(event_data):
    return "A new scheduled task was created: " + event_data['task_name']
def criticality():
    return 'MEDIUM'
def tactic():
    return 'Persistence (TA0003)'
def technique():
    return 'Scheduled Task (T1053.005)'
def artifacts():
    return stats.collect(['task_name', 'event_id'])
def entity(event):
    return {'derived': False, 'value': event['task_name'], 'type': 'task'}