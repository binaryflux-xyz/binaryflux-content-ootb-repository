#Add your code here

def widgets():
    return [
        "{%customer%}/{%tenant%}/widgets/top_users_by_alert_activity/",
        "{%customer%}/{%tenant%}/widgets/data_type_breakdown/",
        "{%customer%}/{%tenant%}/widgets/data_flow_analysis/",
        "{%customer%}/{%tenant%}/widgets/top_data_destinations/",
    ]

def configure():
    return {
        "datepicker": True,
    }
