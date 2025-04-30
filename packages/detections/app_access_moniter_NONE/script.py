import re

def window():
    return None

def groupby():
    return None

def algorithm(event):
    keywords = ['tcp','udp','netbios forward','PING','UNKNOWN','SNMP','SIP',
                'POP3','HTTP','DNS','SSL','Endpoint Control Registration',
                'Microsoft.Windows.Update','MMS','QUIC','Ping','Management',
                'icmp','DHCP','IPSec','RDP','SMTP','SMB','NTP','SQL','SQUID',
                'SOCKS','RTSP','KERBEROS','PPTP','NetBIOS','Trace.Route','RPC',
                'LDAP','IMAP','VNC','SCCP','SAMBA','L2TP','NFS','STUN','FSSOD',
                'Domain Name Server','TELNET','/','BGP','SSH','IKE']
    if event.get('applicationname') is not None \
        and not any (keyword in event.get('applicationname') for keyword in keywords) :
            return 0.01
    return 0.0

def context(event_data):
   url = event_data.get('applicationname') if event_data.get('applicationname') is not None else "NONE"
   ip = event_data.get('source_ip') if event_data.get('source_ip') is not None else "NONE"
#    return "source_ip = "+ip+" url = "+url
   return "User with an ip address ("+str(ip)+") tried to access "+ str(url) 


def criticality():
    return None


def tactic():
    return "Discovery (TA0007)"
 

def technique():
    return "Network Share Discovery (T1135)"


def entity(event):
    return {"derived": False, "value": event.get("source_ip"), "type": "ipaddress"}


def artifacts():
    try:
        return stats.collect(
            [
                "applicationname",
                "source_ip",
                "network_bytes_transferred",
                "network_bytes_out",
                "network_bytes_in",
                "destination_port",
                "destination_ip",
                "source_hostname"
            ]
        )
    except Exception as e:
        raise e


def is_valid_url(url):

    if url is None:
        return False
    # Define the regex pattern for a valid URL without http or https
    pattern = re.compile(
        r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}(?:/[\w\.-]*)*$', re.IGNORECASE)

    # Match the URL against the regex pattern
    match = pattern.match(url)
    
    return bool(match)