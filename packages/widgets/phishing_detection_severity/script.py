# sample name -> widgets/accounts_compromised/script.py

# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "properties": {"type": "column","onclick":"open_offcanvaspanel"},
        "dimension": {"x":0,"y":1,"width": 4, "height": 4}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        'query': 'SELECT COUNT(*) AS count, risk, agent FROM genaianalysis WHERE (agent = :agent1 or agent = :agent2 )  AND risk IS NOT null and risk != :risk GROUP BY risk, agent',
        'parameters': {"agent1":'email-pii',"agent2": 'email-phishing', "risk":"none"},
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
        "sortcol":"count",
        "sortorder":"desc"    
    }


def render(results):
    colors=["#003F5C","#007599"]
    
    # Extract unique risk categories from results
    categories = sorted(set(item["risk"].upper() for item in results))

    # Initialize risk mapping with all categories
    risk_mapping = {risk: i for i, risk in enumerate(categories)}

    # Initialize series data structure
    series = {}

    for item in results:
        agent = item["agent"]
        risk_level = item["risk"].upper()
        count = item["count"]

        if agent not in series:
            series[agent] = [0] * len(categories)  # Initialize data array

        if risk_level in risk_mapping:
            index = risk_mapping[risk_level]
            series[agent][index] += count  # Store count in the correct index

    # Convert to required series format
    series_list = [{"name": agent, "data": data} for agent, data in series.items()]

    return {"result": {"categories":categories,"series":series_list},"setColumnWidth":"dlp-dashboardwidgets","colors":colors,"column":"risk","label":"Risk","columnmap":["agent","risk"],"queryType":"genai"}