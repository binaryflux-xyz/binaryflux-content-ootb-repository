def type() :
    return 'injection_topoperation_data'

def columns() : #column names to be aggregated
    return ['table_name','operation']

def archive() :
    return 'monthly'


def uniquekey(message):
    return None