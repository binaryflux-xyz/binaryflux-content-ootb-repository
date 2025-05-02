
def format():
    return "table"


def query():

    return {

        "query": "SELECT entity,COUNT(score) AS scorecount,detectioncriticality AS criticality,MAX(lastdetectiontime) AS lastdetectiontime FROM entityscoring e WHERE detectionid =:detectionid GROUP BY entity, detectioncriticality HAVING (entity, MAX(lastdetectiontime)) IN ( SELECT entity, MAX(lastdetectiontime) AS maxdetectiontime  FROM entityscoring  WHERE detectionid =:detectionid GROUP BY entity)",
        "parameters": {"detectionid":'663b4b9592ff9a66fe03c2e4'}
    }



def template():

    return """
            <h2>${title}</h2>
            <table>
                <tbody><tr>
                    <th>Entity</th>
                    <th>Criticality</th>
                    <th>Score</th>
                    <th>Last Detected</th>
                </tr>
                
                    <#list 0..size-1 as i>
                    <tr>
                        <#assign entitydetails = index(i)>
                        <td>${entitydetails.entity}</td>
                        <td>${entitydetails.criticality}</td>
                        <td>${entitydetails.scorecount}</td>
                        <td>${entitydetails.lastdetectiontime}</td>
                    </tr>
                    </#list>
                
                </tbody>
            </table>"""