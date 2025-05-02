#Add your code here
import time
import datetime



def criteria(metainfo):
  return metainfo['provider'] == 'microsoft' and metainfo['group'] == 'email' and metainfo['type'] == 'office365'

# this to return time of event 
def timestamp(event):
  #2014-03-17T15:39:18Z
  datestring = event['receivedDateTime'];
  element = datetime.datetime.strptime(datestring,"%Y-%m-%dT%H:%M:%SZ")
  timestamp = time.mktime(element.timetuple())
  return int(timestamp) * 1000


def message(event):
  if not event:
      return "Event data is missing."

  # Construct the message
  return "Microsoft email content"



# sample data after parsing


  
def dictionary(event):
  total_size=0
  body_content = event.get("body")
  attachments=event.get("attachments",[])
  if body_content is not None:
    body_content = body_content["content"]

  fromemailaddress=event.get("from").get("emailAddress").get("address")
  torecipent = event.get("toRecipients", [])
  finaltorecipentlist=[]
  finaltoccrecipients=[]
  finaltobccrecipients=[]
  finalreplyto=[]
  if torecipent:  # Checks if the list is not empty
    finaltorecipentlist = [entry["emailAddress"]["address"] for entry in torecipent]
      
  
  toccrecipients=event.get("ccRecipients" , [])
  if len(toccrecipients)>0:
      finaltoccrecipients=[entry["emailAddress"]["address"] for entry in toccrecipients]
  tobccrecipents=event.get("bccRecipients" , [])
  if len(tobccrecipents)>0:
      finaltobccrecipients=[entry["emailAddress"]["address"] for entry in tobccrecipents]
  replyto=event.get("replyTo" , [])
  if len(replyto)>0:
      finalreplyto=[entry["emailAddress"]["address"] for entry in replyto]

  email_attachments_name = []
  if len(attachments)>0:
    email_attachments_name = [attachment.get("name") for attachment in attachments]
    
    total_size = sum(attachment.get("size", 0) for attachment in attachments) if attachments else 0
    
  return {
    "email_message_id":event.get("id"),
    "email_subject": event.get("subject"),
    "email_body": body_content,
    "email_headers": event.get("internetMessageHeaders"),
    "email_from_address": fromemailaddress,
    "email_to_address": finaltorecipentlist,
    "email_cc_address": finaltoccrecipients,
    "email_bcc_address": finaltobccrecipients,
    "email_reply_to_address": finalreplyto,
    "email_attachments_name": email_attachments_name,
    "email_folder":event.get("mail_folder"),
    "email_attachments_size":total_size,
    "historic":event.get("historic",False)
  }