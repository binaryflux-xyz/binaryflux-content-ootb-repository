import re
from datetime import datetime, timedelta
from email.utils import parseaddr
from urlparse import urlparse

TRUSTED_DOMAINS = ["facebook.com",
    "instagram.com",
    "twitter.com",
    "linkedin.com",
    "youtube.com",
    "pinterest.com",
    "wonderhfl.com",
    "income-tax-india.com",
    "incometax.gov.in"]
SUSPICIOUS_KEYWORDS = ["urgent", "verify", "account locked", "click here", "expired"]
EXECUTABLE_EXTENSIONS = [".exe", ".js", ".scr", ".docm", ".xlsm", ".bat", ".cmd", ".ps1", ".vbs", ".wsf", ".jar", ".dll", ".com", ".hta"]

def init(event):
    return "initialization completed"

# this to return window (5s , 5m) for which events needs to be aggregated else return null , this has to be small window , for larger windows use scheduled detections
def window():
    return None

# this should return list of attributes to group algorithm data, this should be only provided in case of window is not None


def groupby():
    return None

# this to return double value for riskscore attached to this event based on detection algo ,  aggregated will receive as events list else it will be a single event


def algorithm(event):
    mail_folder = event.get("email_folder")
    if mail_folder != "inbox" or event.get('email_within_company') == True:
      return 0.0
    sender = event.get('email_header_from', '')
    
    # print("sender: " +str(sender))
    unknown_sender = check_sender_anomalies(sender)
    result = False
    
    if unknown_sender:
        if result == False:
            result = check_suspicious_links(event.get('email_subject_links',''), sender)

        if result == False:
            result = check_suspicious_links(event.get('email_body_links',''), sender)
        
        if result == False:
            print("attachements----")
            print(str(event.get('email_attachment_names','')))
            result = check_unexpected_attachments(event.get('email_attachment_names',''))
        
        if result == False:
            result = check_generic_salutations(event.get('email_body_shortened',''))
        
        if result == False:
            result = check_unusual_requests(event.get('email_body_shortened',''))
        
        #if result == False:
            #result = check_timing(event['email_header_received'])
        print("result " + str(result))
    if result == True:
        return 2.0
    else:
        return 0.0

def clusters(event): 
    return  None

# this to return html string to add context to detection
def context(event):
    sender = event.get('email_header_from','')
    message_parts = []
    unknown_sender = check_sender_anomalies(sender)
    result = False
    if unknown_sender:
        result = check_suspicious_links(event.get('email_subject_links',''), sender)
        if result:
            message_parts.append(
                "Suspicious links found in the subject line, suggesting potential phishing attempts."
            )

        result = check_suspicious_links(event.get('email_body_links',''), sender)
        if result:
            message_parts.append(
                "Suspicious links detected in the email body, which may be used to mislead recipients."
            )

        result = check_unexpected_attachments(event.get('email_attachment_names',''))
        if result:
            message_parts.append(
                "Unexpected attachments were found, which may be indicative of malicious intent."
            ) 

        result = check_generic_salutations(event.get('email_body_shortened',''))
        if result:
            message_parts.append(
                "Generic salutations were detected in the email body, a common trait in phishing messages."
            ) 

        result = check_unusual_requests(event.get('email_body_shortened',''))
        if result:
            message_parts.append(
                "Unusual requests or instructions found in the email content, which may signal a scam or phishing attempt."
            )
    to_value = str(event.get('email_to_address','')).replace('[', '').replace(']', '')
    from_value = str(event.get('email_from_address',''))
    # return "An email that contains suscipious or phishing content was sent by " + from_value + " to " + to_value
    context_message = ""
    if message_parts:
        detailed_message = " ".join(message_parts)
        context_message = "An email from " + from_value +" to " + to_value + " raised suspicions: " + detailed_message

    return context_message

# this to return criticality induced by this detection [LOW MEDIUM HIGH CRITICAL]


def criticality():
    return 'HIGH'


# this to return mapping with MITRE attack tactics
def tactic():
    return  'Initial Access (TA0001)' 

# this to return mapping with MITRE attack technique


def technique():
    return 'Phishing (T1566)'

# extract the artifacts required to be saved as part of this detection


def artifacts():
    return stats.collect(['email_to_address', 'email_subject','email_attachments_name','source_location','email_from_address','email_body_shortened', 'email_subject_links', 'email_body_links'])

# define entity derivation if required else write it like this :: { 'derived': False ,'type' :"Employee" , 'value': event['file_owner_shared']}


def entity(event):
    return { 
        "derived":True, 
        "from":{
                "type":"email", 
                "class":"identity",
                "value":event.get("email_from_address")
        },
        "type": "employee"
    }

# retrieve a specific headers value
def get_header_value(header_name, headers):
    for header in headers:
        if header["name"].lower() == header_name.lower():
            return header["value"]
    return None

# check for anomalies in senders email
def check_sender_anomalies(sender):
    if not sender:
        return True
    match = re.search(r"@([\w.-]+)", sender)
    domain = match.group(1) if match else None
    email_match = re.search(r"<([^>]+)>", sender)
    email = email_match.group(1) if email_match else sender  # Use sender if no brackets
    
    if domain and domain not in TRUSTED_DOMAINS:
        return True  # Domain is not trusted
    if re.search(r"[^\w.-]", domain):
        return True  # Contains unusual characters
    if re.search(r"\d+", email):
        return True 
    return False

# check for urgent or threatening language
def check_urgency_or_threats(body):
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword.lower() in body.lower():
            return True
    return False

# detect suspicious links in the email body
def check_suspicious_links(links, sender):
    url_domain_mapping = []

    for url in links:
        # Parse the URL.
        parsed_url = urlparse(url)
        # The domain (host) is in the netloc attribute.
        domain = parsed_url.netloc
        # Save the result as a tuple or dictionary.
        url_domain_mapping.append(domain)
    sender_domain = extract_domain(sender)  
    if sender_domain is not None:
      TRUSTED_DOMAINS.append(sender_domain)
      
    for url_domain in url_domain_mapping:
        # Check if any trusted domain is a suffix of the URL domain
        if not any(url_domain.endswith("." + domain) or url_domain == domain for domain in TRUSTED_DOMAINS):
          return True  # Suspicious link found
    return False

# check for unexpected or dangerous attachments
def check_unexpected_attachments(attachments):
    if attachments is not None and any(
        attachment.endswith(ext) for attachment in attachments for ext in EXECUTABLE_EXTENSIONS
    ):
        return True
    return False

# detect generic salutations
def check_generic_salutations(body):
    if re.search(r"\b(Dear (Customer|User|Sir|Madam|Valued Client))\b", body, re.IGNORECASE):
        return True
    return False

# detect requests for sensitive information
def check_unusual_requests(body):
    if re.search(r"(password|credit card|debit card|aadhar card|pan card|scanner|qr code|confidential)", body, re.IGNORECASE):
        return True
    return False

# detect unusual sending times
def check_timing(received_headers):
    for header_value in received_headers:
        match = re.search(r"\b(\d{1,2}:\d{2}:\d{2})\b", header_value)
        if match:
            timestamp = match.group(0)
            email_time = datetime.strptime(timestamp, "%H:%M:%S").time()
            if email_time < datetime.strptime("08:00:00", "%H:%M:%S").time() or \
               email_time > datetime.strptime("18:00:00", "%H:%M:%S").time():
                return True
    return False

def extract_domain(email_header):
      # Parse the email header into (display_name, email_address)
      name, email_address = parseaddr(email_header)
      # Check if the email address contains an '@' and return the domain
      if '@' in email_address:
          return email_address.split('@')[-1]
      return None