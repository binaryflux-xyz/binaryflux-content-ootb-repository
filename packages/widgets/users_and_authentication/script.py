# sample name -> widgets/accounts_compromised/script.py

# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": False,
        "properties": {"type": "areastackedchart","layout": "conciselayout"},
        "dimension": {"x":0,"y":15,"width": 6, "height": 3}
    }

# this to return query to be used for rendering widget and its parameters

def query():
    return {
        "query": """
            select detectionname AS name, 
            entity AS user, 
            COUNT(entity) AS event_count
          FROM 
            entityscoring
          WHERE 
            detectionname IN (
              'MFA Fatigue', 
              'MFA disabled for an application', 
              'Login from multiple locations', 
              'Potential Password Spray Attack', 
              'Suspicious login attempts', 
              'User Authenticated from new machine', 
              'User password reset'
            )
          GROUP BY 
            detectionname, 
            entity;
        """,
        "parameters": {},
    }

# this to return filter queries based on filters selected by user and its parameters
def filters(filter):
    return None


# this to return free text search query and its parameters
def search(freetext):
    return None


# this to return sort query
def sort():
    return None

def render(results):
    if not results or len(results) == 0:
        raise Exception("no results found")

    # Fixed categories (X-axis)
    categories = [
        'MFA Fatigue',
        'MFA disabled for an application',
        'Login from multiple locations',
        'Potential Password Spray Attack',
        'Suspicious login attempts',
        'User Authenticated from new machine',
        'User password reset'
    ]

    # Step 1: Aggregate total count per user
    user_counts = {}
    for item in results:
        user = item.get('user')
        count = item.get('event_count', 0)

        if user and isinstance(count, (int, float)):
            user_counts[user] = user_counts.get(user, 0) + count

    if not user_counts:
        raise Exception("No valid user data found")

    # Step 2: Get top 5 users by total count
    top_users = sorted(user_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    top_user_names = [u[0] for u in top_users]

    # Step 3: Initialize series for top users
    series_map = {user: [0] * len(categories) for user in top_user_names}

    # Step 4: Populate series data
    for item in results:
        user = item.get('user')
        detection = item.get('name')
        count = item.get('event_count', 0)

        if user in series_map and detection in categories and isinstance(count, (int, float)):
            idx = categories.index(detection)
            series_map[user][idx] += count  # Accumulate if multiple rows match

    # Step 5: Prepare final series list
    series = []
    for user in top_user_names:
        series.append({
            "name": user,
            "data": series_map[user]
        })

    # Colors for up to 5 users
    colors = ["#00b8d3", "#aed987", "#eacc62", "#e4604e", "#8a6dd3"]

    legends = [{
        "layout": 'vertical',
        "align": 'right',
        "verticalAlign": 'middle',
        "itemMarginTop": 5,
        "itemStyle": {
            "color": '#888888',
            "fontWeight": 'normal',
            "fontSize": '12px'
        },
        "symbolHeight": 12,
        "symbolWidth": 12,
        "symbolRadius": 6
    }]

    return {
        "series": series,
        "categories": categories,
        "legends": legends,
        "colors": colors,
        "className": "dlp-dashboardwidgets",
        "xAxis": {
            "labels": {
                "enabled": True,
                "rotation": -45
            }
        },
        "yAxis": {
            "title": {
                "text": "Count"
            }
        }
    }
