
ALLOWED_GROUPS_LIST = []


def init(event):
    return "initialization completed"

# this to return window (5s , 5m) for which events needs to be aggregated else return None , this has to be small window , for larger windows use scheduled detections
def window():
    return None

# this should return list of attributes to group algorithm data, this should be only provided in case of window is not None


def groupby():
    return None

# this to return double value for riskscore attached to this event based on detection algo ,  aggregated will receive as events list else it will be a single event


def algorithm(event):
    email_attachments_size = event.get("email_attachments_size", 0)
    email_from_groups = event.get("email_from_groups", [])
    mail_folder=event.get("email_folder")
    
    # Check if the sender belongs to an excluded group and if attachment size exceeds limit
    SIZE_LIMIT = 5 * 1024 * 1024  
    if (mail_folder=="sent" and len(email_from_groups)>0):
        for email_group in email_from_groups:
            if email_group not in ALLOWED_GROUPS_LIST:
                if email_attachments_size > SIZE_LIMIT:  # Limit increased to 20 MB
                    return 0.75  # Assign a higher risk score for excessive attachment size
    return 0.0  # No risk if attachment size is within limit



def clusters(event): 
    return  None

# this to return html string to add context to detection
def context(event_data):
    to_addresses = event_data.get('email_to_address', [])
    from_address = event_data.get('email_from_address', 'Unknown')
    sender_domain = event_data.get('email_from_domain', 'Unknown Domain')
    email_attachments_size = event.get("email_attachments_size", 0)
    
    # Detection Explanation
    explanation = (
        "An email   was sent by "+str(from_address)+
        "(domain: "+str(sender_domain)+") to "+str(to_addresses)
    )
    attachemnt_mb=(email_attachments_size/(1024 * 1024))
    
    explanation += (
        " This email contains large attachments totaling "+str(attachemnt_mb)+ "MB, which exceeds the allowed limit of 5MB. This could indicate suspicious activity. The sender does not belong to an allowed group list, which further raises concerns."
    )
    
    return explanation



# this to return criticality induced by this detection [LOW MEDIUM HIGH CRITICAL]


def criticality():
    return 'HIGH'


# this to return mapping with MITRE attack tactics
def tactic():
    return 'Exfiltration (TA0010)'

# this to return mapping with MITRE attack technique


def technique():
    return 'Exfiltration Over Web or Email (T1567)' 

# extract the artifacts required to be saved as part of this detection


def artifacts():
    return stats.collect(['email_from_address', 'email_to_address', 'email_attachments_size','source_location'])

# define entity derivation if required else write it like this :: { 'derived': False ,'type' :"Employee" , 'value': event['file_owner_shared']}


def entity(event):
    return {'derived': False,
            'value': event.get('email_from_address'),
            'type': 'email'}