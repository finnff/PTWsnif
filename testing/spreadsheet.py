# Integratie naar Googledrive/google sheets, voor nep database/ maken diagrammen via gsheets
# Werkt niet door libary die stuk is in oauth2client line 220 ergens.

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "client_secret.json", scope)
client = gspread.authorize(creds)

sheet = client.open("sniff data").sheet1

data = sheet.get_all_records()
print(data)
