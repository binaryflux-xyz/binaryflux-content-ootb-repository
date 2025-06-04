import time
import datetime

def criteria(metainfo):
    return metainfo['provider'] == 'AWS' and metainfo['group'] == 'S3' \
        and metainfo['type'] == 'File Access' and  metainfo['name'] == 'Palo Alto Firewall'


def timestamp(data):
    event = map_values_to_fields(data)
    datestring = event.get("generated_time")
    dt = datetime.datetime.strptime(datestring, "%Y/%m/%d %H:%M:%S")
    epoch_time = time.mktime(dt.timetuple())  # Seconds since epoch
    return int(epoch_time * 1000)  # Convert to milliseconds
  

def map_values_to_fields(data_dict):
    try:
        values = data_dict.get("values", [])
        if not values or len(values) < 1:
            return {"error": "Empty or invalid values list"}

        # Extract log_time and hostname
        parts = values[0].split()
        if len(parts) >= 4:
            log_time = " ".join(parts[0:3])
            hostname = parts[3]
        else:
            log_time = values[0]
            hostname = ""

        # These are the expected field names after log_time and hostname
        log_type = values[3]
        if log_type == "GLOBALPROTECT":
            field_names =[
                "receive_time",                       # 1 - same
                "serial_number",                      # 2 - same
                "type",                               # 3 - same ("GLOBALPROTECT")
                "event_id",                           # 4 - custom (no match in base list)
                "future_use_1",                       # 5 - reused
                "generated_time",                     # 6 - same
                "virtual_system",                # 7 - reused
                "event_type",                         # 8 - custom (e.g., portal-prelogin)
                "stage",                              # 9 - custom (e.g., before-login)
                "source_user",                        # 10 - reused
                "destination_user",                   # 11 - reused
                "domain",                             # 12 - not in base list
                "src_country",                        # 13 - reused ("US")
                "dst_country",                        # 14 - reused (may be empty)
                "src_ip",                             # 15 - reused
                "dst_ip",                             # 16 - reused (can be internal IP)
                "nat_src_ip",                         # 17 - reused
                "nat_dst_ip",                         # 18 - reused
                "host_id",                            # 19 - reused
                "source_hostname",                    # 20 - reused
                "application",                        # 21 - reused ("Browser", "App")
                "src_device_os_family",               # 22 - reused ("Browser")
                "src_device_os_version",              # 23 - reused (version string, maybe empty)
                "repeat_count",                       # 24 - reused (e.g., login attempt count)
                "category",                           # 25 - reused
                "future_use_2",                       # 26 - reused
                "future_use_3",                       # 27 - reused
                "action",                             # 28 - reused ("success", "failure")
                "log_action",                         # 29 - reused (or error_message)
                "future_use_4",                       # 30 - reused (error code)
                "inbound_interface",                  # 31 - reused (duration)
                "device_group_hierarchy_level_1",     # 32 - reused (portal name)
                "session_id",                         # 33 - reused
                "flags",                              # 34 - reused
                "high_resolution_timestamp",          # 35 - reused
                "app_flap_count",                     # 36 - reused (not used, placeholder)
                "link_switches",                      # 37 - reused (not used, placeholder)
                "sd_wan_cluster",                     # 38 - reused (not used, placeholder)
                "sd_wan_device_type",                 # 39 - reused (not used, placeholder)
                "sd_wan_cluster_type",               # 40 - reused (not used, placeholder)
                "sd_wan_site",                        # 41 - reused (not used, placeholder)
                "bytes",                              # 42 - reused
                "bytes_sent",                         # 43 - reused
                "bytes_received",                     # 44 - reused
                "packets",                            # 45 - reused
                "tunnel_type",                        # 46 - reused
                "device_name",                        # 47 - reused
                "policy_id",                          # 48 - reused (was "1")
                "offloaded"                           # 49 - reused (final field)
            ]

        elif log_type == "TRAFFIC":
            field_names = [
            "receive_time", "serial_number", "type", "threat_content_type",
            "future_use_1", "generated_time", "src_ip", "dst_ip", "nat_src_ip", "nat_dst_ip",
            "rule_name", "source_user", "destination_user", "application", "virtual_system",
            "src_zone", "dst_zone", "inbound_interface", "outbound_interface", "log_action",
            "future_use_2", "session_id", "repeat_count", "src_port", "dst_port", "nat_src_port",
            "nat_dst_port", "flags", "protocol", "action", "bytes", "bytes_sent", "bytes_received",
            "packets", "start_time", "elapsed_time", "category", "future_use_3", "sequence_number",
            "action_flags", "src_country", "dst_country", "future_use_4", "packets_sent",
            "packets_received", "session_end_reason", "device_group_hierarchy_level_1",
            "device_group_hierarchy_level_2", "device_group_hierarchy_level_3",
            "device_group_hierarchy_level_4", "virtual_system_name", "device_name", "action_source",
            "source_vm_uuid", "destination_vm_uuid", "tunnel_id_imsi", "monitor_tag_imei",
            "parent_session_id", "parent_start_time", "tunnel_type", "sctp_association_id",
            "sctp_chunks", "sctp_chunks_sent", "sctp_chunks_received", "rule_uuid",
            "http2_connection", "app_flap_count", "policy_id", "link_switches", "sd_wan_cluster",
            "sd_wan_device_type", "sd_wan_cluster_type", "sd_wan_site", "dynamic_user_group_name",
            "xff_address", "src_device_category", "src_device_profile", "src_device_model",
            "src_device_vendor", "src_device_os_family", "src_device_os_version", "source_hostname",
            "source_mac_address", "dst_device_category", "dst_device_profile", "dst_device_model",
            "dst_device_vendor", "dst_device_os_family", "dst_device_os_version", "destination_hostname",
            "destination_mac_address", "container_id", "pod_namespace", "pod_name",
            "source_external_dynamic_list", "destination_external_dynamic_list", "host_id",
            "serial_number_2", "source_dynamic_address_group", "destination_dynamic_address_group",
            "session_owner", "high_resolution_timestamp", "a_slice_service_type",
            "a_slice_differentiator", "application_subcategory", "application_category",
            "application_technology", "application_risk", "application_characteristic",
            "application_container", "tunneled_application", "application_saas",
            "application_sanctioned_state", "offloaded"
        ]
        elif log_type=="THREAT":
            field_names = [
            "receive_time",                       # 1
            "serial_number",                      # 2
            "type",                               # 3 -> "THREAT"
            "threat_content_type",               # 4 -> "spyware", "vulnerability", etc.
            "future_use_1",                       # 5
            "generated_time",                     # 6
            "src_ip",                              # 7
            "dst_ip",                              # 8
            "nat_src_ip",                          # 9
            "nat_dst_ip",                          #10
            "rule_name",                           #11
            "source_user",                         #12
            "destination_user",                    #13
            "application",                         #14
            "virtual_system",                      #15
            "src_zone",                            #16
            "dst_zone",                            #17
            "inbound_interface",                   #18
            "outbound_interface",                  #19
            "log_action",                          #20
            "future_use_2",                        #21
            "session_id",                          #22
            "repeat_count",                        #23
            "src_port",                             #24
            "dst_port",                             #25
            "nat_src_port",                         #26
            "nat_dst_port",                         #27
            "flags",                                #28
            "protocol",                             #29
            "action",                               #30 -> "alert", "reset-client", etc.
            "bytes",                                #31
            "bytes_sent",                           #32
            "bytes_received",                       #33
            "packets",                              #34
            "start_time",                           #35
            "elapsed_time",                         #36
            "category",                             #37 -> threat category
            "future_use_3",                         #38
            "sequence_number",                      #39
            "action_flags",                         #40
            "src_country",                          #41
            "dst_country",                          #42
            "future_use_4",                         #43
            "packets_sent",                         #44
            "packets_received",                     #45
            "session_end_reason",                   #46
            "device_group_hierarchy_level_1",       #47
            "device_group_hierarchy_level_2",       #48
            "device_group_hierarchy_level_3",       #49
            "device_group_hierarchy_level_4",       #50
            "virtual_system_name",                  #51
            "device_name",                          #52
            "action_source",                        #53
            "source_vm_uuid",                       #54
            "destination_vm_uuid",                  #55
            "tunnel_id_imsi",                       #56
            "monitor_tag_imei",                     #57
            "parent_session_id",                    #58
            "parent_start_time",                    #59
            "tunnel_type",                          #60
            "sctp_association_id",                  #61
            "sctp_chunks",                          #62
            "sctp_chunks_sent",                     #63
            "sctp_chunks_received",                 #64
            "rule_uuid",                            #65
            "http2_connection",                     #66
            "app_flap_count",                       #67
            "policy_id",                            #68
            "link_switches",                        #69
            "sd_wan_cluster",                       #70
            "sd_wan_device_type",                   #71
            "sd_wan_cluster_type",                  #72
            "sd_wan_site",                          #73
            "dynamic_user_group_name",              #74
            "xff_address",                          #75
            "src_device_category",                  #76
            "src_device_profile",                   #77
            "src_device_model",                     #78
            "src_device_vendor",                    #79
            "src_device_os_family",                 #80
            "src_device_os_version",                #81
            "source_hostname",                      #82
            "source_mac_address",                   #83
            "dst_device_category",                  #84
            "dst_device_profile",                   #85
            "dst_device_model",                     #86
            "dst_device_vendor",                    #87
            "dst_device_os_family",                 #88
            "dst_device_os_version",                #89
            "destination_hostname",                 #90
            "destination_mac_address",              #91
            "container_id",                         #92
            "pod_namespace",                        #93
            "pod_name",                             #94
            "source_external_dynamic_list",         #95
            "destination_external_dynamic_list",    #96
            "host_id",                              #97
            "serial_number_2",                      #98
            "source_dynamic_address_group",         #99
            "destination_dynamic_address_group",    #100
            "session_owner",                        #101
            "high_resolution_timestamp",            #102
            "threat_id",                            #103 -> custom field (threat ID / signature ID)
            "url_or_filename",                      #104 -> custom field (URL or file name involved)
            "content_version",                      #105 -> content update version
            "pcap_id",                              #106 -> custom field (if packet capture is enabled)
            "offloaded"                             #107 -> reused
        ]

        # Map remaining values
        remaining_values = values[1:]
        mapped_fields = {
            "log_time": log_time,
            "hostname": hostname
        }

        for idx, field in enumerate(field_names):
            mapped_fields[field] = remaining_values[idx] if idx < len(remaining_values) else ''

        return mapped_fields

    except Exception as e:
        return {"error": "Mapping failed: " + repr(e)}



def message(event):
    """
    Returns a human-readable message extracted from the event.

    Args:
        event (dict): Parsed log fields.

    Returns:
        str: Summary or message string.
    """
    # TODO: Construct a readable message from event fields
    return "message"


def dictionary(rawdata):
    event=map_values_to_fields(rawdata)
    return {

        "observer_serial_number":event.get("serial_number"),
        "event_id":event.get("sequence_number"),
        "hostname": event.get("hostname"),
        "event_type": event.get("type"),
        "event_action": event.get("action"),
        "event_duration":event.get("elapsed_time"),
        "source_ip": event.get("src_ip"),
        "destination_ip": event.get("dst_ip"),
        "source_nat_ip":event.get("nat_src_ip"),
        "destination_nat_ip":event.get("nat_dst_ip"),
        "rule":event.get("rule_name"),
        "source_use_name":event.get("source_user"),
        "destination_user_name":event.get("destination_user"),
        "application": event.get("application"),
        "source_zone":event.get("src_zone"),
        "destination_zone":event.get("dst_zone"),
        "source_device_interface": event.get("inbound_interface"),
        "destination_device_interface": event.get("outbound_interface"),
        "event_sessionid": event.get("session_id"),
        "source_port": event.get("src_port"),
        "destination_port": event.get("dst_port"),
        "source_nat_port":event.get("nat_src_port"),
        "destination_nat_port":event.get("nat_dst_port"),
        "network_protocol": event.get("protocol"),
        "network_bytes_in": event.get("bytes_received"),
        "network_bytes_out": event.get("bytes_sent"),
        "network_packets_in": event.get("packets_received"),
        "network_packets_out": event.get("packets_sent"),
        "source_country": event.get("src_country"),
        "destination_country": event.get("dst_country"),
        "application_risk": event.get("application_risk"),

        
        # Additional details
        "details": {
            'virtual_system': event.get("virtual_system"),
            "log_transport":event.get("log_action"),
            "event_repeat_count":event.get("repeat_count"),
            "flags":event.get("flags"),
            "session_end_reason":event.get("session_end_reason"),
            "action_flags":event.get("action_flags"),
        },
    }
