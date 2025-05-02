# {"timezoneName":"","messageType":"Error","eventType":"logEvent","source":null,"formatString":"Failed to authenticate user <%s> (error: %d).","userID":0,"activityIdentifier":1303937,"subsystem":"com.apple.Authorization","category":"AuthorizationHost","threadID":848669,"senderImageUUID":"CA6E4F8C-42DB-3E86-AB29-98D79D2666B6","backtrace":{"frames":[{"imageOffset":134502,"imageUUID":"CA6E4F8C-42DB-3E86-AB29-98D79D2666B6"}]},"bootUUID":"D6025D8F-B04B-4639-B5EA-D478CFF8EB24","processImagePath":"\/System\/Library\/Frameworks\/Security.framework\/Versions\/A\/MachServices\/authorizationhost.bundle\/Contents\/MacOS\/authorizationhost","senderImagePath":"\/System\/Library\/Frameworks\/Security.framework\/Versions\/A\/MachServices\/authorizationhost.bundle\/Contents\/MacOS\/authorizationhost","timestamp":"2025-04-02 16:17:12.103054+0530","machTimestamp":176396721012799,"eventMessage":"Failed to authenticate user <<private>> (error: 9).","processImageUUID":"CA6E4F8C-42DB-3E86-AB29-98D79D2666B6","traceID":730831668842500,"processID":73362,"senderProgramCounter":134502,"parentActivityIdentifier":1303936} 


# The placeholder <%s> would typically be replaced by the actual username, but in this case, it shows as <<private>>, meaning the username was not disclosed for privacy or security reasons. 



def window():
    return '10m'

def groupby():
    return ['host']

def algorithm(event):
    if event.get('event_type') == 'logEvent' and 'failed to authenticate user' in event['event_Message'].lower():
        if stats.count(event.get("host")) > 5:
            return 0.75
    return 0.0

def context(event_data):
    return "Multiple failed login attempts detected on " + str(event_data['host'])

def criticality():
    return 'HIGH'

def tactic():
    return 'Credential Access (TA0006)'

def technique():
    return 'Brute Force (T1110)'

def artifacts():
    return stats.collect(['host', 'timestamp'])

def entity(event):
    return {'derived': False, 'value': event['host'], 'type': 'device'}
