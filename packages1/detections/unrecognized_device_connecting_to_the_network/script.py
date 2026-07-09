
def init(event):
    source_device_id = event.get("source_device_id")
    print("at start of init rare port")
    features = {
        "source_device_id": source_device_id
    }
    print("feature map created for rare port")

    clusters = stats.rarity("source_device_id", features, 3)
    print("kmean method called")
    session.set("clusters", clusters)
    print("session created")
    return "initialization completed"


# this to return window (5s , 5m) for which events needs to be aggregated else return null , this has to be small window , for larger windows use scheduled detections
def window():
  return '30d'

# this should return list of attributes to group algorithm data, this should be only provided in case of window is not None


def groupby():
  return ['applicationname']

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
  device_with_anomaly = []
  
  for entry in clusters:
      for record in entry["records"]:
          if record["anomaly"]:
              print("record.isAnomaly(): "+str(record["anomaly"]))
              source_device_id = record["features"]["source_device_id"]
              device_with_anomaly.append(source_device_id)
              
  if len(device_with_anomaly) > 0:
      return "A rare device " + event_data.get('source_device_id') + " was detected in the network trying to access " + event_data.get('applicationname') + " application "
  else:
      return ""

# this to return criticality induced by this detection [LOW MEDIUM HIGH CRITICAL]


def criticality():
  return 'HIGH'


# this to return mapping with MITRE attack tactics
def tactic():
  return 'Initial Access (TA0001)'

# this to return mapping with MITRE attack technique


def technique():
  return 'External Remote Services (T1133)' 

# extract the artifacts required to be saved as part of this detection


def artifacts():
    try:
        return stats.collect([
                "source_ip",
                "network_protocol",
                "source_device_id",
                "destination_port",
                "applicationname",
                "destination_ip",
                "destination_country"
            ])
    except Exception as e:
        raise e

def entity(event):
  return {'derived': False,
            'value': event.get("source_ip"), 'type': "ipaddress"}