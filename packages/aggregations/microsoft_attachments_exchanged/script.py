def type() :
    return 'microsoft_attachments_exchanged'

def columns() : #column names to be aggregated
    return ["email_attachments_size","email_from_address","email_to_address"]

def archive() :
    return 'monthly'

def uniquekey(message):
    return 'microsoft_attachments_exchanged'
  
def columnproperties():
    return {"email_to_address":"list"}