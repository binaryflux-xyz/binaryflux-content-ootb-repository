from datetime import datetime

def init(event):
    mail_folder=event.get("email_folder")
    if mail_folder == "inbox":
      print("at start of init receiving unusual recipients")
      recipients = []
      recipients.append(event["email_from_address"])
      recipients = recipients + event["email_to_address"]
      recipients = recipients + event["email_cc_address"]
      recipients = recipients + event["email_bcc_address"]
      recipients = recipients + event["email_reply_to_address"]
      features = {
          "recipients": recipients
      }
      print("feature map created")

      clusters = stats.rarity("recipients", features, 3)
      print("kmean method called")
      session.set("clusters", clusters)
      print("session created")
      return "initialization completed"
    else:
      return "mail folder is not type of inbox"

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
    total_records = 0
    anomaly_records = 0
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
    recipients_with_anomaly = []
    
    for entry in clusters:
        for record in entry["records"]:
            if record["anomaly"]:
                print("record.isAnomaly(): "+str(record["anomaly"]))
                recipients = record["features"]["recipients"]
                                
                # Append the recipients and device to their respective lists
                recipients_with_anomaly.append(recipients)
                
    if len(recipients_with_anomaly) > 0:
        to_value = str(event_data['email_to_address']).replace('[', '').replace(']', '')
        msg = "An unfamiliar email address was detected while receiving an email from " + event_data['email_from_address'] + " to " + str(to_value) + " with subject " + event_data['email_subject']
        if event_data['email_cc_address'] is not None and len(event_data['email_cc_address']) > 0:
            msg = msg + " having cc: " + str(event_data['email_cc_address'])
        if event_data['email_bcc_address'] is not None and len(event_data['email_bcc_address']) > 0:
            msg = msg + ", having bcc: " + str(event_data['email_bcc_address'])
        if event_data['email_reply_to_address'] is not None and len(event_data['email_reply_to_address']) > 0:
            msg = msg + " and replyTo: " + str(event_data['email_reply_to_address'])

        return msg
    else:
        return ""

# this to return criticality induced by this detection [LOW MEDIUM HIGH CRITICAL]


def criticality():
    return 'HIGH'


# this to return mapping with MITRE attack tactics
def tactic():
    return 'Phishing (T1566)'

# this to return mapping with MITRE attack technique


def technique():
    return 'Initial Access (TA0001)' 

# extract the artifacts required to be saved as part of this detection


def artifacts():
    return stats.collect(['email_from_address', 'email_to_address', 'email_cc_address', 'email_bcc_address', 'email_reply_to_address','source_location'])

# define entity derivation if required else write it like this :: { 'derived': False ,'type' :"Employee" , 'value': event['file_owner_shared']}


def entity(event):
    return {'derived': False,
            'value': event['email_from_address'],
            'type': 'email'}