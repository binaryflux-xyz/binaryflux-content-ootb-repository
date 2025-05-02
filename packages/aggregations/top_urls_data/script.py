def type() :
    return 'top_urls_data'

def columns() : #column names to be aggregated
    return ['url']

def archive() :
    return 'monthly'

def uniquekey(message):
    return message.get('url')