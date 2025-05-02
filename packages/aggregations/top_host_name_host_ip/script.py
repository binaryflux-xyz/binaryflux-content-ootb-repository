def type() :
    return 'top_host_name_host_ip'

def columns() : #column names to be aggregated
    return ['host_name','log_syslog_hostip']

def archive() :
    return 'monthly'

def uniquekey(message):
  try:
    return message.get('host_name')+'_'+message.get('log_syslog_hostip')
  except:
     return None