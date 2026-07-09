def init(event):
    destination_port = event.get("destination_port")
    print("at start of init rare port")
    features = {
        "destination_port": event.get("destination_port"),
        'network_protocol': event.get('network_protocol'),
    }
    print("feature map created for rare port")

    clusters = stats.rarity("network_protocol", features, 3)
    print("kmean method called")
    session.set("clusters", clusters)
    print("session created")
    return "initialization completed"


# this to return window (5s , 5m) for which events needs to be aggregated else return null , this has to be small window , for larger windows use scheduled detections
def window():
  return '30d'

# this should return list of attributes to group algorithm data, this should be only provided in case of window is not None


def groupby():
  return ['source_ip']

# this to return double value for riskscore attached to this event based on detection algo ,  aggregated will receive as events list else it will be a single event


def algorithm(event):
  clusters = session.get("clusters")
  total_records = 0
  anomaly_records = 0
  if clusters:
    for entry in clusters:
        records = entry["records"]
        # records = entry['records']
        total_records += len(records) 
        anomaly_records += sum(1 for record in records if record["anomaly"])
    print("total_records: "+str(total_records))
    print("anomaly_records: "+str(anomaly_records))
    if anomaly_records > 0:
      # rest.call({body}, url, {headers}, method)
      print("score = "+str(round(anomaly_records / float(total_records), 2)))
      return round(anomaly_records / float(total_records), 2)
    else:
      return 0.0
  else:
    return 0.0

def clusters(event): 
  return  session.get("clusters")

# this to return html string to add context to detection
def context(event_data):
    clusters = session.get("clusters")
    ports_with_anomaly = []
    
    for entry in clusters:
        for record in entry["records"]:
            if record["anomaly"]:
                print("record.isAnomaly(): "+str(record["anomaly"]))
                network_protocol = record["features"]["network_protocol"]
                ports_with_anomaly.append(network_protocol)
                
    if len(ports_with_anomaly) > 0:
        msg = "Unusual or unauthorized protocol detected from source IP " + str(event_data.get('source_ip', 'unknown')) + "using protocol"+str(event_data.get('network_protocol', 'unknown')) + \
            " on port " + str(event_data.get('destination_port', 'unknown')) + \
            ". This may indicate unauthorized access or lateral movement."
        return msg
    else:
        return ""



def criticality():
  return 'HIGH'


# this to return mapping with MITRE attack tactics
def tactic():
  return 'Command and Control (TA0011)'

# this to return mapping with MITRE attack technique


def technique():
  return 'Application Layer Protocol (T1071)' 

# extract the artifacts required to be saved as part of this detection


def artifacts():
    try:
        return stats.collect([
                "source_ip",
                "network_protocol",
                "destination_port",
                "event_type"
            ])
    except Exception as e:
        raise e

def entity(event):
  return {'derived': False,
            'value': event.get("source_ip"), 'type': "ipaddress"}