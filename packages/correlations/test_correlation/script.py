def build(event):
    if  event.get("eventtype")=="groupmembers":
        data = relation(event)
    elif event.get("eventtype")=="users":
        data = employee(event)
    else:
        data = group(event)
    return data

def relation(event):
    nodes = {}
    edges = []
    
    nodes["userprincipalname"]=graph.getNode({"customer":event.get("customer"),"tenant":event.get("tenant"),"dynamic": [
            {"key": "label", "value": "employee"},
            {"key": "employeeHandle", "value": event.get("userPrincipalName")}
        ]})
    nodes["groupid"]=graph.getNode({"customer":event.get("customer"),"tenant":event.get("tenant"),"dynamic": [
            {"key": "label", "value": "group"},
            {"key": "groupid", "value": event.get("group_id")}
        ]})
    edges.append({
            'source': 'userprincipalname',
            'destination': 'groupid',
            'relation': 'has',
            'direction': 'out'})
    return {
        'nodes': nodes, 
        'edges': edges}



def group(event):
    nodes = {

     "email": {
            'type': 'identity',
            'label': 'email',
            'value': event.get('email')
        },
       
         "groupnode": {
            'type': 'identity',
            'label': 'group',
            'value': event.get('displayName'),
            "createddate":event.get('createdon'),
           "groupid": event.get('id'),
        }
       
    }
      
    edges = [

     {
            'source': 'groupnode',
            'destination': 'email',
            'relation': 'has',
            'direction': 'out',
        }
    ]
        
    return {
        'nodes': nodes, 
        'edges': edges
    }




def employee(event):
    nodes = {
        "employeenode": {
            'type': 'entity',
            'label': 'employee',
            'value': event.get('displayName'),
            'employeeHandle':event.get('userPrincipalName')
        },
        "email": {
            'type': 'identity',
            'label': 'email',
            'value': event.get('email')
        },

    }
      
    edges = [
     {
            'source': 'employeenode',
            'destination': 'email',
            'relation': 'has',
            'direction': 'out',
        }]


    if event.get('position') is not None :
        try:
            nodes["location"]={
                    'type': 'identity',
                    'label': 'location',
                    'value': event.get('position')
                }
            edges.append({
                'source': 'employeenode',
                'destination': 'location',
                'relation': 'has',
                'direction': 'out',
            })
        except Exception as error:
            print(error)
    if event.get('contact') is not None :
        try:
            nodes["employeenode"]["phoneno"]=event.get('contact')
        except Exception as error:
            print(error)
    if event.get('lastName') is not None :
        try:
            nodes["employeenode"]["lastname"]= event.get('lastName')

        except Exception as error:
            print(error)
    if event.get('firstName') is not None :
        try:
            nodes["employeenode"]["firstname"]=event.get('firstName') 
        except Exception as error:
            print(error)
    else:
      nodes["employeenode"]["firstname"] = event.get('displayName')
        
    return {
        'nodes': nodes, 
        'edges': edges
    }