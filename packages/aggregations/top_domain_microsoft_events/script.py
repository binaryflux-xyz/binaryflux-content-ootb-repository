def type() :
    return 'top_domain_microsoft_events'

def columns() : #column names to be aggregated
    return ['email_from_domain','email_to_address']

def archive() :
    return 'monthly'

def uniquekey(message):
    return "top_domain_microsoft_events"

        
def columnproperties():
    return {"email_to_address":"list"}