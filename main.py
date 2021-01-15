import requests
import os
from datetime import date
import time

# Get the day's full date
today = date.today()

# Format the date to be used in the pdf file name
dateFormatted = today.strftime("%d-%m-%Y")

# Get the full path of the script
path = os.path.dirname(os.path.realpath(__file__))

# Create the pdf name
filename = path + "/public/docs/pemex-" + dateFormatted + ".pdf"

# Get the urls
mainUrl = 'https://www.comercialrefinacion.pemex.com/portal/menu/controlador?Destino=menu_gral.jsp'
pdfUrl = 'https://www.comercialrefinacion.pemex.com/portal/scgli004/controlador?Destino=MuestraPDF&doctoID=1'

# Start a session
s = requests.Session()

# Request main page to get cookies and headers
mainReq = s.get(mainUrl)

# Maybe unnecessary, but may allow the server to catch up before next request?
time.sleep(1)

# Make request for PDF file
pdfReq = s.get(pdfUrl)

# Write PDF file to filesystem
with open(filename, 'wb') as f:
  f.write(pdfReq.content)
