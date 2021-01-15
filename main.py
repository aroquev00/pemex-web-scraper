import requests

print("Hi")

mainUrl = 'https://www.comercialrefinacion.pemex.com/portal/menu/controlador?Destino=menu_gral.jsp'
pdfUrl = 'https://www.comercialrefinacion.pemex.com/portal/scgli004/controlador?Destino=MuestraPDF&doctoID=1'

s = requests.Session()
mainReq = s.get(mainUrl)
pdfReq = s.get(pdfUrl)

print(mainReq.text)
print(s.cookies)
print(pdfReq.text)
