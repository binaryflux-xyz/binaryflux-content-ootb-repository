
def format():
    return "table"
def query():

    return {

        "query": "select name as detectionname,criticality as criticality,technique as technique,tactic as tactic,COUNT(criticality) AS detectioncount,COUNT(distinct entity) as usercount FROM detection  where streamid=:streamid GROUP BY name,criticality,technique,tactic",
        "parameters": {"streamid":"662f4fcb911227439313de7c"}
    }

def template():

    return """
            <h2>${title}</h2>
            <table>
                <tbody><tr>
                    <th>Name</th>
                    <th>Criticality</th>
                    <th>Technique</th>
                    <th>Tactic</th>
                     <th>Detection Count</th>
                     <th>User Count</th>
                </tr>
                    <#list 0..size-1 as i>
                    <tr>
                        <#assign entitydetails = index(i)>
                        <td>${entitydetails.detectionname}</td>
                        <td>${entitydetails.criticality}</td>
                        <td>${entitydetails.technique}</td>
                        <td>${entitydetails.tactic}</td>
                        <td>${entitydetails.detectioncount}</td>
                        <td>${entitydetails.usercount}</td>
                    </tr>
                    </#list>
                
                </tbody>
            </table>"""