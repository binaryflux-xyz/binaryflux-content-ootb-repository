#Add your code here
import time
import datetime


def criteria(metainfo): 
  return metainfo['provider'] == 'microsoft' and metainfo['group'] == 'entities' and metainfo['type'] == 'office365'

# this to return time of event 
def timestamp(event):
    return int(time.time() * 1000)


def message(event):
  if not event:
      return "Event data is missing."

  # Construct the message
  return "Microsoft email content"


# this to return attribute map to be indexed for this event
def dictionary(event):
    eventtype=event.get('type')
    data={}
    if(eventtype=="users"):
         data={
             "displayName":event.get('displayName'),
        'firstName': event.get('givenName'),
        'lastName': event.get('surname'),
        'contact': event.get('mobilePhone'),
        'email': event.get('mail'),
        'address': event.get('officeLocation'),
        'position': event.get('jobTitle'),
      'userPrincipalName':event.get('userPrincipalName'),
      'eventtype':eventtype
    }
    elif(eventtype=="groups"):
        data={
        'id': event.get('id'),
        'displayName': event.get('displayName'),
        'email': event.get('mail'),
        'eventtype':eventtype,
        'createdon': event.get('createdDateTime')
    }
    else:
        data={
        'displayName': event.get('displayName'),
         'firstName': event.get('givenName'),
         'lastName': event.get('surname'),
        'contact': event.get('mobilePhone'),
        'email': event.get('mail'),
        'address': event.get('officeLocation'),
        'position': event.get('jobTitle'),
      'userPrincipalName':event.get('userPrincipalName'),
      'eventtype':eventtype,
      'group_id':event.get('group_id'),
    }
        
    return data