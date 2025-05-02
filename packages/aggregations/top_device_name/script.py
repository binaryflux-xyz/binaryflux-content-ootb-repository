def type() :
    return 'top_device_name'

def columns() : #column names to be aggregated
    return ['source_device_id']

def archive() :
    return 'monthly'

def uniquekey(message):
    return message.get('source_device_id')