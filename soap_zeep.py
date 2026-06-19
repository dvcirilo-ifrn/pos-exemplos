import zeep
numero = input("Digite o número: ")
print(zeep.Client(wsdl="http://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL").service.NumberToWords(ubiNum=numero))