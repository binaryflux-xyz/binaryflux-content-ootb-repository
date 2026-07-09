# this to return default widget config
def configure():
    return {
        "searchable": True, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "liveserverdata"},
        "dimension": {"x": 0, "y": 7, "width": 12, "height": 5}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "SELECT detectiontechnique AS technique,  COUNT(idx) AS total FROM entityscoring WHERE detectiontechnique IS NOT NULL GROUP BY technique",
        "parameters": {}
    }

# this to return filter queries based on filters selected by user and its parameters
def filters(filters):
    return None
# this to return free text search query and its parameters
def search(freetext):
    return None

# this to return sort query
def sort(sorcol, sortorder):
    sort += " order by " + sorcol + " " + sortorder


def render(data):
    series = [
    {
                    "serverstatus": "serverOnline",
                    "source": "fortigate",
                    "lastEvent": "13 min ago",
                    "location": "Lucknow",
                    "value": 822150.0
                },
                {
                    "serverstatus": "serverOnline",
                    "source": "fortigate",
                    "lastEvent": "13 min ago",
                    "location": "Naroda",
                    "value": 794344.0
                },
                {
                    "serverstatus": "serverOnline",
                    "source": "fortigate",
                    "lastEvent": "13 min ago",
                    "location": "Rajahmundry",
                    "value": 794349.0
                },
                {
                    "serverstatus": "serverOnline",
                    "source": "fortigate",
                    "lastEvent": "13 min ago",
                    "location": "Gandhidham",
                    "value": 795366.0
                },
                {
                    "serverstatus": "serverOnline",
                    "source": "fortigate",
                    "lastEvent": "13 min ago",
                    "location": "Dehradun",
                    "value": 795390.0
                },
                {
                    "serverstatus": "serverOnline",
                    "source": "fortigate",
                    "lastEvent": "13 min ago",
                    "location": "Mehsana",
                    "value": 806077.0
                },
                {
                    "serverstatus": "serverOnline",
                    "source": "fortigate",
                    "lastEvent": "13 min ago",
                    "location": "Dahod",
                    "value": 802101.0
                },
        {
            "value": 10,
            "datacenter": "DC1",
            "location": "New York",
            "lastEvent": "10 sec ago",
            "serverstatus": "serverUnstable",
            "source": "zoom",
        },
        {
            "value": 30,
            "datacenter": "DC2",
            "location": "Los Angeles",
            "lastEvent": "30 sec ago",
            "serverstatus": "serverOffline",
            "source": "okta",
        },
        {
            "value": 5,
            "datacenter": "DC3",
            "location": "London",
            "lastEvent": "5 sec ago",
            "serverstatus": "serverUnstable",
            "source": "google",
        },
        {
            "value": 15,
            "datacenter": "DC4",
            "location": "Tokyo",
            "lastEvent": "15 sec ago",
            "serverstatus": "serverOffline",
            "source": "linux",
        },
        {
            "value": 25,
            "datacenter": "DC5",
            "location": "Sydney",
            "lastEvent": "25 sec ago",
            "serverstatus": "serverUnstable",
            "source": "zoom",
        },
        {
            "value": 8,
            "datacenter": "DC6",
            "location": "Berlin",
            "lastEvent": "8 sec ago",
            "serverstatus": "serverUnstable",
            "source": "okta",
        },
        {
            "value": 20,
            "datacenter": "DC7",
            "location": "Mumbai",
            "lastEvent": "20 sec ago",
            "serverstatus": "serverOnline",
            "source": "google",
        },
        {
            "value": 100,
            "datacenter": "DC8",
            "location": "Singapore",
            "lastEvent": "1 min ago",
            "serverstatus": "serverOffline",
            "source": "linux",
        },
        {
            "value": 500,
            "datacenter": "DC9",
            "location": "Denmark",
            "lastEvent": "3 min ago",
            "serverstatus": "serverOnline",
            "source": "zoom",
        },
        {
            "value": 6000,
            "datacenter": "DC10",
            "location": "Germany",
            "lastEvent": "20 min ago",
            "serverstatus": "serverOffline",
            "source": "okta",
        },
        {
            "value": 1200,
            "datacenter": "DC11",
            "location": "Jerusalem",
            "lastEvent": "12 min ago",
            "serverstatus": "serverOnline",
            "source": "google",
        },
      {
            "value": 6000,
            "datacenter": "DC10",
            "location": "Germany",
            "lastEvent": "20 min ago",
            "serverstatus": "serverOffline",
            "source": "okta",
        },
        {
            "value": 1200,
            "datacenter": "DC11",
            "location": "Jerusalem",
            "lastEvent": "12 min ago",
            "serverstatus": "serverOnline",
            "source": "google",
        },
      {
            "value": 6000,
            "datacenter": "DC10",
            "location": "Germany",
            "lastEvent": "20 min ago",
            "serverstatus": "serverOffline",
            "source": "okta",
        },
        {
            "value": 1200,
            "datacenter": "DC11",
            "location": "Jerusalem",
            "lastEvent": "12 min ago",
            "serverstatus": "serverOnline",
            "source": "google",
        },
      {
            "value": 6000,
            "datacenter": "DC10",
            "location": "Germany",
            "lastEvent": "20 min ago",
            "serverstatus": "serverOffline",
            "source": "okta",
        },
        {
            "value": 1200,
            "datacenter": "DC11",
            "location": "Jerusalem",
            "lastEvent": "12 min ago",
            "serverstatus": "serverOnline",
            "source": "google",
        },
      {
            "value": 6000,
            "datacenter": "DC10",
            "location": "Germany",
            "lastEvent": "20 min ago",
            "serverstatus": "serverOffline",
            "source": "okta",
        },
        {
            "value": 1200,
            "datacenter": "DC11",
            "location": "Jerusalem",
            "lastEvent": "12 min ago",
            "serverstatus": "serverOnline",
            "source": "google",
        },
      {
            "value": 6000,
            "datacenter": "DC10",
            "location": "Germany",
            "lastEvent": "20 min ago",
            "serverstatus": "serverOffline",
            "source": "okta",
        },
        {
            "value": 1200,
            "datacenter": "DC11",
            "location": "Jerusalem",
            "lastEvent": "12 min ago",
            "serverstatus": "serverOnline",
            "source": "google",
        }
    ]

    columns = ["datacenter", "lastEvent", "value", "source", "location","serverstatus","Totaldetections"]

    return {"series": series, "columns": columns}
