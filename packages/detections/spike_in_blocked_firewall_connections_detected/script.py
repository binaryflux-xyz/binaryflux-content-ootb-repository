from datetime import datetime

def init(event):
    if event.get('event_action') == 'deny':
        # print("inside init method")
        clusters = stats.spike("event_action", "DAY_OF_MONTH", 1)
        # print("clusters spike called")
        session.set("clusters", clusters)
    return "initialization completed"

# this to return window (5s , 5m) for which events needs to be aggregated else return null , this has to be small window , for larger windows use scheduled detections
def window():
    return '30d'

# this should return list of attributes to group algorithm data, this should be only provided in case of window is not None


def groupby():
    return ['source_ip']

# this to return double value for riskscore attached to this event based on detection algo ,  aggregated will receive as events list else it will be a single event


def algorithm(event):
    #clusters = session.get("clusters")
    if event.get('event_action') == "deny":
        clusters = session.get("clusters")
        print("clusters: "+str(clusters))
        total_records = 0
        anomaly_records = 0
        for entry in clusters:
          records = entry["records"]
          total_records += len(records)
          anomaly_records += sum(1 for record in records if record["anomaly"])
        if anomaly_records > 0:
          return round(anomaly_records / float(total_records), 2)
        else:
          return 0.0
    # print("clusters: "+str(clusters))
    # total_records = 0
    # anomaly_records = 0
    # for entry in clusters:
    #     records = entry["records"]
    #     total_records += len(records) 
    #     anomaly_records += sum(1 for record in records if record["anomaly"])
    # print("total_records: "+str(total_records))
    # print("anomaly_records: "+str(anomaly_records))
    # if anomaly_records > 0:
    #     print("score = "+str(round(anomaly_records / float(total_records), 2)))
    #     return round(anomaly_records / float(total_records), 2)
    # else:
    #     return 0.0

def clusters(event): 
    return  session.get("clusters")


def context(event_data):
    return (
        "Spike detected in denied connections from source IP " + str(event_data.get('source_ip', 'unknown')) +
        ". This may indicate port scanning or DDoS behavior."
    )

# this to return criticality induced by this detection [LOW MEDIUM HIGH CRITICAL]


def criticality():
    return 'MEDIUM'


# this to return mapping with MITRE attack tactics
def tactic():
    return 'Reconnaissance (TA0043)'

# this to return mapping with MITRE attack technique


def technique():
    return 'Network Service Scanning (T1046)'

# extract the artifacts required to be saved as part of this detection


def artifacts():
    return stats.collect(['source_ip', 'destination_ip', 'destination_port', 'event_action', 'event_type'])

# define entity derivation if required else write it like this :: { 'derived': False ,'type' :"Employee" , 'value': event['file_owner_shared']}


def entity(event):
    return {'derived': False,
            'value': event['source_ip'],
            'type': 'ipaddress'}
