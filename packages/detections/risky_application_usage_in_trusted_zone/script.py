def window():
    # Check every event individually, no aggregation needed
    return None

def groupby():
    # No grouping required since we check event by event
    return None

def algorithm(event):
    """
    Calculate risk score for risky application usage in Trusted zone.
    Application risk is numeric and must be >= 3.
    """
    try:
        app_risk_str = event.get('application_risk', '0')
        app_risk = int(app_risk_str)
    except:
        app_risk = 0
    
    # Check if either source or destination zone is TRUST
    source_zone = event.get('source_zone', '').upper()
    destination_zone = event.get('destination_zone', '').upper()
    
    if app_risk >= 3 and ('TRUST' in [source_zone, destination_zone]):
        return 0.5  # Medium-High risk
    
    return 0.0

def context(event):
    return (
        "Risky application usage detected in Trusted zone. Application risk level: " + 
        str(event.get('application_risk', 'N/A')) + 
        ". Application: " + event.get('application', 'N/A') +
        ". Source Zone: " + event.get('source_zone', 'N/A') + 
        ", Destination Zone: " + event.get('destination_zone', 'N/A') +
        ". Source IP: " + event.get('source_ip', 'N/A') +
        ", Destination IP: " + event.get('destination_ip', 'N/A') + "."
    )

def criticality():
    return 'MEDIUM'

def tactic():
    return 'Defense Evasion (TA0005)'

def technique():
    return 'Use of Compromised Credentials (T1078)'  # Adjust if you prefer another technique

def artifacts():
    return stats.collect(['application', 'application_risk', 'source_zone', 'destination_zone', 'source_ip', 'destination_ip'])

def entity(event):
    return {'derived': False, 'value': event.get('source_ip'), 'type': 'ip_address'}
