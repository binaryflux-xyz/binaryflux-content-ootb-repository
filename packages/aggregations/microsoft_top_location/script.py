def type() :
    return 'microsoft_top_location_event'

def columns() : #column names to be aggregated
    return ["source_location"]

def archive() :
    return 'monthly'

def uniquekey(message):
    return message.get('source_location')