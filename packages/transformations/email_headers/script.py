import os
import re

def transform(event):
    #print("transformed called...")
    if "email_headers" in event and event.get("email_headers") is not None:
      email_headers = event['email_headers']
      #print("email_headers: " + str(email_headers))
      event['email_header_received'] = extract_specific_headers(email_headers, "Received")
      event['email_header_from'] = extract_specific_headers(email_headers, "From")
      event['email_header_replyto'] = extract_specific_headers(email_headers, "Reply-To")
      event['email_header_returnpath'] = extract_specific_headers(email_headers, "Return-Path")
      event['email_header_auth'] = extract_specific_headers(email_headers, "Authentication-Results")
      source_ips = extract_ips(email_headers)
      event['source_ip'] = source_ips
      event['source_location'] = get_country(source_ips)
      event['details.domains'] = []
      event['details.group'] = []
    return event


def extract_specific_headers(headers, header_name):
    matching_headers = []
    for header in headers:
        if header["name"].lower() == header_name.lower():
            matching_headers.append(header["value"])
    if len(matching_headers) == 0:
        return None  # Return the single header as a dictionary
    if len(matching_headers) == 1:
        return matching_headers[0]
    return matching_headers


def extract_ips(headers):
    
    # List to store unique IPs (maintain order)
    ip_addresses = []
    seen_ips = set()
    
    for header in headers:
        if header["name"].lower() == "received":
            # Extract IPs within parentheses
            ips = extract_ips_from_parentheses(header["value"])
            print("from_parenthsis: " + str(ips))
            seen_ips.update(ips)
    return seen_ips
    
def extract_ips_from_parentheses(text):
    # Regex to match content within parentheses
    parenthesis_pattern = r'\(([^()]+)\)'
    # IPv4 and IPv6 patterns
    ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ipv6_pattern = r'\b(?:[a-fA-F0-9]{1,4}:){1,7}[a-fA-F0-9]{1,4}\b|\b(?:[a-fA-F0-9]{1,4}:){1,6}:\b'
    
    # Find all content inside parentheses
    matches = re.findall(parenthesis_pattern, text)
    
    # Filter only valid IPs
    ip_addresses = set()
    for match in matches:
        if re.match(ipv4_pattern, match) or re.match(ipv6_pattern, match):
            ip_addresses.add(match)
    
    return sorted(ip_addresses)

def get_country(source_ips):
    countries = set()  # Use a set to avoid duplicates
    for ip in source_ips:
        ip_int = range.toIpLong(ip)
        print("ip_int", ip_int)
        country_data = tpi.query("Maxmindipv6", "? BETWEEN start_ip AND end_ip", [ip_int])
        print("country_data", country_data)

        # If not found, check IPv4
        if not country_data:
            country_data = tpi.query("Maxmindipv4", "? BETWEEN start_ip AND end_ip", [ip_int])
            print("ipv6 country_data", country_data)

        if country_data:
            geo_id = country_data[0][2]
            country = tpi.query("Maxmindcountries", "geoname_id=?", [geo_id])
            print("country", country)
            if country:
                countries.add(country[0][5])  # Add to set to avoid duplicates
    print("countries", countries)
    return list(countries)[0] if countries else None  # Convert to list & return first element

    
