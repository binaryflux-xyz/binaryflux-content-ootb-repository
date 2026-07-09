from datetime import datetime

def only_contains_from_domain(domain_list,event):
    email_from_domain = event.get("email_from_domain", "")
    return all(domain == email_from_domain for domain in domain_list) if domain_list else True
    
def mail_sent_within_domain(event_data):
  mail_folder = event_data.get("email_folder")
  email_from_domain = event_data.get("email_from_domain", "")
  email_reply_to_domains = event_data.get("email_reply_to_address_domain", [])
  email_bcc_domains = event_data.get("email_bcc_address_domain", [])
  email_cc_domains = event_data.get("email_cc_address_domain", [])
  email_to_address_domain=event_data.get("email_to_address_domain",[])
  if (only_contains_from_domain(email_to_address_domain,event_data) 
  and only_contains_from_domain(email_bcc_domains,event_data) and 
only_contains_from_domain(email_cc_domains,event_data) and 
only_contains_from_domain(email_reply_to_domains,event_data)):
    return True
  else:
    return False
    
def check_group_sharing(event):
    recipients_groups = event.get("email_recipients_groups", [])
    from_groups = event.get("email_from_groups", [])

    # If recipients_groups is empty, return "No recipients"
    if not recipients_groups:
        return "No recipients"

    # Check if recipients_groups only contains from_groups
    if all(group in from_groups for group in recipients_groups):
        return "WithinSameGroup"
    
    # If any group in recipients_groups is not in from_groups, return "ShareOtherGroup"
    return "ShareOtherGroup"


def init(event):
  mail_folder = event.get("email_folder")
  if (mail_folder == "sent"):
      is_mail_within_org=mail_sent_within_domain(event)
      if (is_mail_within_org):
        print("at start of init rare domain")
        recipients_groups = event.get("email_recipients_groups")
        print("recipients_groups "+ str(recipients_groups))
        features = {
            "recipientsgroups": recipients_groups
        }
        print("feature map created for domain")
    
        clusters = stats.rarity("recipientsgroups", features, 3)
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
  is_mail_within_org=mail_sent_within_domain(event)
  if (not (mail_folder == "sent") and  (not is_mail_within_org)):
    return 0.0
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
    print("email_from_domain: " +str(event.get("email_from_domain")))
    if anomaly_records > 0:
      # rest.call({body}, url, {headers}, method)
      print("score = "+str(round(anomaly_records / float(total_records), 2)))
      check_group_sharing=check_group_sharing()
      if(check_group_sharing=="WithinSameGroup"):
          return 0.25
          session.set("criticality", 'LOW')
      else:
          session.set("criticality", 'CRITICAL')
          temp_score=round(anomaly_records / float(total_records), 2)
          return 1 if temp_score > 1 else temp_score
    else:
      return 0.0
  else:
    return 0.0

def clusters(event): 
  return  session.get("clusters")

# this to return html string to add context to detection
def context(event_data):
  clusters = session.get("clusters")
  domains_with_anomaly = []
  mail_folder = event.get("email_folder")
  email_reply_to_domains = event_data.get("email_reply_to_address_domain", [])
  email_bcc_domains = event_data.get("email_bcc_address_domain", [])
  email_cc_domains = event_data.get("email_cc_address_domain", [])
  is_mail_within_org=mail_sent_within_domain(event)
  
  for entry in clusters:
      for record in entry["records"]:
          if record["anomaly"]:
              print("record.isAnomaly(): "+str(record["anomaly"]))
              domain = record["features"]["domain"]
                              
              # Append the domain and device to their respective lists
              domains_with_anomaly.append(domain)
              
  if len(domains_with_anomaly) > 0:
      if (not (mail_folder != "sent") and (not is_mail_within_org)):
          return ""
    
          email_to_address,  email_from_domain,  email_from_domain,email_bcc_address,email_reply_to_address,email_recipients_groups
      to_value = str(event_data.get('email_to_address')).replace('[', '').replace(']', '')
      
      if check_group_sharing == "WithinSameGroup":
           msg = ("An email from {} (domain: {}) was sent within the same group to {}"
                   .format(email_from_address, email_from_domain, to_value))
      else:
          msg = ("An email from {} (domain: {}) was sent to {} outside the usual group"
                   .format(email_from_address, email_from_domain, to_value))
      if email_bcc_address:
          msg += ", BCC: {}".format(email_bcc_address)
      if email_reply_to_address:
          msg += ", Reply-To: {}".format(email_reply_to_address)
      if email_cc_domains:
        msg += ", CC: {}".format(email_reply_to_address)
      
      msg += ", targeting the group(s) {}".format(email_recipients_groups)

      return msg
  else:
      return ""

# this to return criticality induced by this detection [LOW MEDIUM HIGH CRITICAL]


def criticality():
  return session.get("criticality")


# this to return mapping with MITRE attack tactics
def tactic():
  return 'Exfiltration (TA0010)'

# this to return mapping with MITRE attack technique


def technique():
  return 'Unusual Email Activity (T1071.003)' 

# extract the artifacts required to be saved as part of this detection


def artifacts():
  return stats.collect(['email_from_address', 'email_from_domain','source_location'])

# define entity derivation if required else write it like this :: { 'derived': False ,'type' :"Employee" , 'value': event['file_owner_shared']}


def entity(event):
  return {'derived': False,
            'value': event.get('email_from_address'),
            'type': 'email'}