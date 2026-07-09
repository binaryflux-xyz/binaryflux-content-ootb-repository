
def format():
    return "table"


def query():

    return {

        "query": "select source_ip as sourceip,network_protocol as networkprotocol,destination_port as destinationport,(cast(network_bytes_out as bigint) +cast(network_bytes_in as bigint)) as totalexchangedbytes,to_char(to_timestamp(detectiontime/1000), 'YYYY/MM/DD HH24:MI:SS') as lastdetectiontime from detection where detectionid=:detectionid",
        "parameters": {"detectionid":'662f4fce911227439313de80'}
    }


def template():

    return """
            <h2>${title}</h2>
            <table>
                <tbody><tr>
                    <th>SourceIp</th>
                    <th>NetworkProtocol</th>
                    <th>DestinationPort</th>
                    <th>Total Exchanged Bytes</th>
                    <th>LastDetectiontime</th>
                </tr>
                
                    <#list 0..size-1 as i>
                    <tr>
                        <#assign entitydetails = index(i)>
                        <td>${entitydetails.sourceip}</td>
                        <td>${entitydetails.networkprotocol}</td>
                        <td>${entitydetails.destinationport}</td>
                        <td>${entitydetails.totalexchangedbytes}</td>
                         <td>${entitydetails.lastdetectiontime}</td>
                    </tr>
                    </#list>
                
                </tbody>
            </table>"""