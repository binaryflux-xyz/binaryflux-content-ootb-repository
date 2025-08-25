from datetime import datetime

def configure():
    return {
        "searchable": False,
        "datepicker": False,
        "properties": {"type": "fatalwidget","layout": "conciselayout"},
        "dimension": {"x":4,"y":4,"width": 8, "height": 3}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        'query': 'SELECT user_name as User,timestamp as Datetime,event_severity as Severity ,dbname as Database ,message as Msg,COUNT(event_severity) AS Count FROM aggregation_table WHERE type = :type AND event_severity = :event_severity GROUP BY user_name,timestamp,event_severity,dbname,message',
        'parameters': {"type":"event_severity_message","event_severity":"FATAL"}
    }

# this to return filter queries based on filters selected by user and its parameters
def filters(filter):
    return None


# this to return free text search query and its parameters
def search(freetext):
    
    return None


# this to return sort query
def sort():
    return{
        "sortcol":"Count",
        "sortorder":"desc"    
    }


# this to return return formated results to render a widget
def render(results):
    if len(results) > 5:
        results = results[:5]  # Limit to the first five records

    columnList = ['Datetime', 'Severity', 'Database', 'User', 'Msg', 'Count']

    for result in results:
        timestamp = result.get('Datetime')
        if timestamp:
            # Convert timestamp from milliseconds to seconds and format
            result['Datetime'] = datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

    return {"result": results, "columns": columnList}