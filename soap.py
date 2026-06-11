import requests
from xml.dom.minidom import parseString

# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

country_code = input("Digite o código do país: ")
# XML estruturado
payload = f"""<?xml version=\"1.0\" encoding=\"utf-8\"?>
			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
				<soap:Body>
					<CountryIntPhoneCode xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
						<sCountryISOCode>{country_code}</sCountryISOCode>
					</CountryIntPhoneCode>
				</soap:Body>
			</soap:Envelope>"""
# headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}
# request POST
response = requests.request("POST", url, headers=headers, data=payload)

# imprime a resposta
if response.status_code == 200:
    print("O código telefônico do país é " + parseString(response.text).documentElement.getElementsByTagName("m:CountryIntPhoneCodeResult")[0].firstChild.nodeValue)