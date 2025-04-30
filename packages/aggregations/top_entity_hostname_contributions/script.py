def type() :
    return 'hostname_entity_map'

def columns() : #column names to be aggregated
    return ['source_ip' , 'source_hostname']

def archive() :
    return 'monthly'

def uniquekey(message):
    try:
        return message.get('source_ip')+'_'+message.get('source_hostname')
    except:
        return None