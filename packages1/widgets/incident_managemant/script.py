import time
# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": False,
        "properties": {"type": "multichart"},
        "dimension": {"x":0,"y":5,"width": 12, "height": 3}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return [{
        'query': 'select criticality,count(*) as total from incidentdetails where criticality is not null group by criticality',
        'parameters': {},
    },
  {
        'query': 'select status,count(*) as total from incidentdetails where status is not null group by status',
        'parameters': {},
    },
  {
        'query': 'select id,criticality,createdon as createdtime from incidentdetails where status!=:status',
        'parameters': {"status":"Completed"},
    }]
 


# this to return filter queries based on filters selected by user and its parameters
def filters(filter):
    return None


# this to return free text search query and its parameters
def search(freetext):
    
    return None


# this to return sort query
def sort():
    return[{
        "sortcol":"total",
        "sortorder":"desc"    
    },
           {
        "sortcol":"total",
        "sortorder":"desc"    
    },
          {
        "sortcol":"createdtime",
        "sortorder":"desc"    
    }]


def render(data):
    series = {"HIGH": 0, "MEDIUM": 0, "LOW": 0, "CRITICAL": 0, "NONE": 0}

    for item in data[0]:
        criticality_level = item["criticality"].upper()
        if criticality_level in series:
            series[criticality_level] += item["total"]


  
    statusdata=data[1]
    seriesdata = []
    categoriesdata = []
    counter=0

    for item in statusdata:
        if(counter<10):
            categoriesdata.append(item["status"])
            seriesdata.append(item["total"])
            counter=counter+1

    # 3. SLA data: calculate newtime
    sladata = data[2]
    current_time = int(time.time() * 1000)
    updated_sladata = []

    for item in sladata:
        created_time = item.get("createdtime")
        if created_time is not None:
            new_item = {
                "criticality": item.get("criticality", ""),
                "newtime": current_time - created_time,
                "id": item.get("id", "")
            }
            updated_sladata.append(new_item)

    # Limit to 10 records
    updated_sladata = updated_sladata[:5]
    
    return {"result":{"incidentpriority":series,"incidentstatus":{"series":[{'data':seriesdata}], "categories": categoriesdata},"slacompliance":updated_sladata}}
  