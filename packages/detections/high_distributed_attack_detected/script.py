def window():
    return None

def groupby():
    return None

def algorithm(event):
    source_ip = event.get("source_ip", "")
    pps = float(event.get("pps", 0))

    if source_ip and pps > 300000:
        source_ip = stats.accumulate(['source_ip'])
        unique_ip=len(source_ip.get("source_ip"))
        if unique_ip > 20:
          stats.dissipate(['source_ip'])
          return 0.75
    return 0.0

def context(event):
    return "This detection triggered because traffic was identified from multiple distributed sources and packet rate exceeded 300000 PPS. Target=%s, Current PPS=%s. This may indicate a coordinated botnet-based DDoS attack designed to increase attack scale and bypass simple source-based blocking." % (
        event.get("destination_ip", "unknown"),
        event.get("pps", 0)
    )

def criticality():
    return "HIGH"

def tactic():
    return "Impact (TA0040)"

def technique():
    return "Network Denial of Service (T1498)"

def entity(event):
    return {
        "derived": False,
        "value": event.get("destination_ip"),
        "type": "ipaddress"
    }