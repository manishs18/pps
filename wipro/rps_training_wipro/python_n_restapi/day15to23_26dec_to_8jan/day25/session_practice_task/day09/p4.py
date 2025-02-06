#SOAP API
import requests

soap_req = """<soapenv:Envelope xmls:soapenv="https://schemas.xmlsoap.org/soap/envelope/"
    <soapenv:Body>
        <getUser xmls="http://example.com">
            <id>1</id>
        </getUser>
    </soapenv: Body>
</soapenv:Envelope>"""


response = requests.post("http://www.dataaccess.com/webservicesserver/", data=soap_req)
print(response.text)
