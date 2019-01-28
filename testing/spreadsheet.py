import gspread
from oath2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfilename("client_secret.json", scope)
client = gspread.authorize(creds)

sheet = client.open("sniff data").sheet1

data = sheet.get_all_records()
print(data)

