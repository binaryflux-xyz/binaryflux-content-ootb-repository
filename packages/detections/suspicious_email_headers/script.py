import re
import socket
from email.utils import parseaddr

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
    # Extract headers
    if event.get('email_within_company') == True:
      return 0.0
    received_headers = [header["value"] for header in event['email_headers'] if header["name"].lower() == "received"]
    auth_results = event["email_header_auth"]

    # Perform checks
    suspicious_received = check_received_headers(received_headers)
    print("suspicious_received" + str(suspicious_received))
    suspicious_auth = check_authentication_results(auth_results)
    print("suspicious_auth" + str(suspicious_auth))
    mismatched_headers = check_mismatched_headers(event)
    print("mismatched_headers" + str(mismatched_headers))
    if ((suspicious_received and suspicious_auth) or (suspicious_received and mismatched_headers) or (suspicious_auth and mismatched_headers)):
        return 2.0
    else:
        return 0.0

def clusters(event): 
    return  None

# this to return html string to add context to detection
def context(event_data):
    received_headers = [header["value"] for header in event_data['email_headers'] if header["name"].lower() == "received"]
    suspicious_received = check_received_headers(received_headers)
    suspicious_auth = check_authentication_results(event_data.get("email_header_auth", ""))
    mismatched_headers = check_mismatched_headers(event_data)

    to_value = str(event_data['email_to_address']).replace('[', '').replace(']', '')
    from_value = ', '.join(event_data['email_from_address']) if isinstance(event_data['email_from_address'], list) else str(event_data['email_from_address'])

    message_parts = []

    if suspicious_received:
        message_parts.append(
            "Received Headers: Anomalies such as reverse DNS mismatches or loops in IP addresses were detected. "
            "This may indicate header tampering or misconfiguration."
        )
    if suspicious_auth:
        message_parts.append(
            "Authentication Results: The email failed SPF, DKIM, or DMARC checks, which suggests that it might be spoofed."
        )
    if mismatched_headers:
        message_parts.append(
            "Header Mismatch: There is an inconsistency among the From, Reply-To, and Return-Path domains. "
            "This is a common sign of phishing or spoofing attempts."
        )

    context_message = ""
    if message_parts:
        detailed_message = " ".join(message_parts)
        context_message = "An email from " + from_value + " to " + to_value + " raised suspicions: " + detailed_message

    return context_message

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
    return stats.collect(['email_to_address', 'email_header_from', 'email_header_replyto', 'email_header_returnpath', 'email_header_auth','email_from_address','source_location'])

# define entity derivation if required else write it like this :: { 'derived': False ,'type' :"Employee" , 'value': event['file_owner_shared']}


def entity(event):
    return {'derived': False,
            'value': event['email_from_address'],
            'type': 'email'}

# function to get the value of a specific header
def get_header_value(header_name, headers):
    for header in headers:
        if header["name"].lower() == header_name.lower():
            return header["value"]
    return None


# validates SPF, DKIM, and DMARC results
def check_authentication_results(auth_result):
    if not auth_result:
        return True
    checks = ["spf=fail", "dkim=fail", "dmarc=fail"]
    return any(check in auth_result.lower() for check in checks)


# checks for mismatches in From, Reply-To, and Return-Path.
def check_mismatched_headers(event):
    # spoofing
    from_header = event['email_header_from']
    reply_to_header = event['email_header_replyto']
    return_path_header = event['email_header_returnpath']
    
    def extract_domain(email_header):
      # Parse the email header into (display_name, email_address)
      name, email_address = parseaddr(email_header)
      # Check if the email address contains an '@' and return the domain
      if '@' in email_address:
          return email_address.split('@')[-1]
      return None

    from_domain = extract_domain(from_header)
    reply_to_domain = extract_domain(reply_to_header)
    return_path_domain = extract_domain(return_path_header)

    # if from_domain id part of trusteddomain then ignore

    is_from_trusteddomain = tpi.query("trusteddomains", "domains=?", [from_domain])
    if (is_from_trusteddomain is not None and len(is_from_trusteddomain) ==0):
      return False
    

    print("is_from_trusteddomain: " + str(is_from_trusteddomain))
    print("from_domain: " + str(from_domain))
    print("reply_to_domain: " + str(reply_to_domain))
    print("return_path_domain: " + str(return_path_domain))
    
    domains = {from_domain, reply_to_domain, return_path_domain}
    domains.discard(None)  # Remove None values
    return len(domains) > 1  # True if there are mismatched domains

# validates Received headers for suspicious behavior.
def check_received_headers(received_headers):
    suspicious = False
    previous_ip = None
    
    for received in received_headers:
        match = re.search(r"from\s+(\S+)\s+\((\d{1,3}(?:\.\d{1,3}){3}|[a-fA-F0-9:]+)\)", received)
        if match:
            domain, ip = match.groups()
            print("domain " + domain)
            try:
                # Reverse DNS lookup
                print("ip " + ip)
                # resolved_domain = socket.gethostbyaddr(ip)[0]
                hostname, aliaslist, ipaddrlist = socket.gethostbyaddr(ip)
                resolved_domain = hostname
                print("resolved_domain " + resolved_domain)
                if resolved_domain != domain:
                    suspicious = True
            except (socket.herror, socket.gaierror) as e:
                # Print the actual error message.
                print("Reverse DNS lookup error:", e)
                suspicious = False
                continue

            if previous_ip and ip == previous_ip:
                print("previous_ip " + previous_ip)
                suspicious = True  # Loops in Received headers
            previous_ip = ip
        # else:
        #     print("else ")
        #     suspicious = True
    return suspicious