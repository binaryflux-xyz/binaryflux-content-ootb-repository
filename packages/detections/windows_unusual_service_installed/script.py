def window():
    return None
def groupby():
    return None
def algorithm(event):
    if event['event_id'] == 7045:
        return 0.9
    return 0.0
def context(event_data):
    return "A new service was installed: " + event_data['service_name'] + " (" + event_data['service_path'] + ")."
def criticality():
    return 'HIGH'
def tactic():
    return 'Persistence (TA0003)'
def technique():
    return 'Create or Modify System Process (T1543)'
def artifacts():
    return stats.collect(['service_name', 'service_path', 'event_id'])
def entity(event):
    return {'derived': False, 'value': event['service_name'], 'type': 'service'}