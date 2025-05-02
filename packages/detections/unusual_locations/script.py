from datetime import datetime

def init(event):
    mail_folder = event.get("email_folder")
    if mail_folder != "inbox":
      return "email is not of type inbox"
    print("at start of init method in unsual locations")
    features = {
        "source_ip": event["source_ip"],
        "email_from_address": event["email_from_address"]
    }
    
    clusters = stats.rarity("source_ip", features, 3)
    print("kmean method called")
    session.set("clusters", clusters)
    print("session created")
    return "initialization completed"

# this to return window (5s , 5m) for which events needs to be aggregated else return null , this has to be small window , for larger windows use scheduled detections
def window():
    return '90d'

# this should return list of attributes to group algorithm data, this should be only provided in case of window is not None

def groupby():
    return ['email_from_address']

# this to return double value for riskscore attached to this event based on detection algo ,  aggregated will receive as events list else it will be a single event


def algorithm(event):
    mail_folder = event.get("email_folder")
    if mail_folder != "inbox":
      return 0.0
    clusters = session.get("clusters")
    print("clusters " + str(clusters))
    total_records = 0
    anomaly_records = 0
    if clusters is not None:
      for entry in clusters:
          records = entry["records"]
          # records = entry['records']
          total_records += len(records) 
          anomaly_records += sum(1 for record in records if record["anomaly"])
    print("total_records: "+str(total_records))
    print("anomaly_records: "+str(anomaly_records))
    if anomaly_records > 0:
        print("score = "+str(round(anomaly_records / float(total_records), 2)))
        return round(anomaly_records / float(total_records), 2)
    else:
        return 0.0

def clusters(event): 
    return  session.get("clusters")

# this to return html string to add context to detection
def context(event_data):
    clusters = session.get("clusters")
    ips_with_anomaly = []
    
    print("Clusters: " + str(clusters))
    
    for entry in clusters:
        for record in entry["records"]:
            if record["anomaly"]:
                print("Anomalous Record Detected: " + str(record["anomaly"]))
                ip = record["features"]["source_ip"]
                ips_with_anomaly.append(ip)
    
    print("Number of anomalous IPs: " + str(len(ips_with_anomaly)))
    
    if len(ips_with_anomaly) > 0:
        to_value = str(event_data.get("email_to_address", "")).replace('[', '').replace(']', '')
        source_location = event_data.get("source_location", [])  # Getting source location list
        location_str = ", ".join(source_location) if source_location else "Unknown Location"

        msg = ("An unfamiliar email activity was detected. An email was sent from {from_addr} "
               "with IP address {ip} (originating from {location}) to {to_addr} "
               "with the subject: '{subject}'").format(
            from_addr=event_data.get("email_from_address", "Unknown"),
            ip=event_data.get("source_ip", "Unknown"),
            location=location_str,
            to_addr=to_value,
            subject=event_data.get("email_subject", "No Subject")
        )

        print("Alert Message: " + msg)
        return msg
    
    return ""

# this to return criticality induced by this detection [LOW MEDIUM HIGH CRITICAL]


def criticality():
    return 'HIGH'


# this to return mapping with MITRE attack tactics
def tactic():
    return 'Initial Access (TA0001)'

# this to return mapping with MITRE attack technique


def technique():
    return 'Phishing (T1566)'

# extract the artifacts required to be saved as part of this detection


def artifacts():
    return stats.collect(['source_ip','source_location'])

# define entity derivation if required else write it like this :: { 'derived': False ,'type' :"Employee" , 'value': event['file_owner_shared']}


def entity(event):
    return {'derived': False,
            'value': event['email_from_address'],
            'type': 'email'}