def type() :
    return 'top_events_data'

def columns() : #column names to be aggregated
    return ['user_name','group_name','host_name','log_syslog_hostip','url','event_outcome','category_name','category_source','event_description', 'event_action', 'event_type','source_device_id','kaspersky_event_category','kaspersky_event_entity','source_device_name','kaspersky_event_action']

def archive() :
    return 'monthly'

def uniquekey(message):
    try:
        return (
            message.get('user_name', '') + "_" +
            message.get('group_name', '') + "_" +
            message.get('host_name', '') + "_" +
            message.get('log_syslog_hostip', '') + "_" +
            message.get('url', '') + "_" +
            message.get('event_outcome', '') + "_" +
            message.get('category_name', '') + "_" +
            message.get('category_source', '') + "_" +
            message.get('event_description', '') + "_" +
            message.get('event_action', '') + "_" +
            message.get('event_type', '') + "_" +
            message.get('source_device_id', '') + "_" +
            message.get('kaspersky_event_category', '') + "_" +
            message.get('kaspersky_event_entity', '') + "_" +
            message.get('source_device_name', '') + "_" +
            message.get('kaspersky_event_action', '')
        )
    except Exception:
        return None

        