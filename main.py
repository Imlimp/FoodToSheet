import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client.json', scope)
client = gspread.authorize(creds)

sheet = client.open("mat").sheet1

now = datetime.now()
date = now.strftime(" %d/%m/%Y")
print("date:", date)
todayCell = sheet.find(date)

meal = input('Frukost?:')
edit = True
if sheet.cell(todayCell.row, 2).value != "":
    edit = False
    overwrite = input('Vill du skriva över ' + "'" +
                      sheet.cell(todayCell.row, 2).value + "'? y/n: ")
    if overwrite == 'y':
        edit = True
if edit == True:
    if '-r' in meal:
        meal = meal.replace('-r', '')
        cellStr = "B" + str(todayCell.row) + ":B" + str(todayCell.row)
        sheet.format(cellStr, {
            "backgroundColor": {
                "red": 0.64,
                "green": 0.77,
                "blue": 0.79
            }
        })
    sheet.update_cell(todayCell.row, 2, meal)

meal = input('Lunch?:')
edit = True
if sheet.cell(todayCell.row, 3).value != "":
    edit = False
    overwrite = input('Vill du skriva över ' + "'" +
                      sheet.cell(todayCell.row, 3).value + "'? y/n: ")
    if overwrite == 'y':
        edit = True
if edit == True:
    if '-r' in meal:
        meal = meal.replace('-r', '')
        cellStr = "C" + str(todayCell.row) + ":C" + str(todayCell.row)
        sheet.format(cellStr, {
            "backgroundColor": {
                "red": 0.64,
                "green": 0.77,
                "blue": 0.79
            }
        })
    sheet.update_cell(todayCell.row, 3, meal)

meal = input('Kvällsmat?:')
edit = True
if sheet.cell(todayCell.row, 4).value != "":
    edit = False
    overwrite = input('Vill du skriva över ' + "'" +
                      sheet.cell(todayCell.row, 4).value + "'? y/n: ")
    if overwrite == 'y':
        edit = True
if edit == True:
    if '-r' in meal:
        meal = meal.replace('-r', '')
        cellStr = "D" + str(todayCell.row) + ":D" + str(todayCell.row)
        sheet.format(cellStr, {
            "backgroundColor": {
                "red": 0.64,
                "green": 0.77,
                "blue": 0.79
            }
        })
    sheet.update_cell(todayCell.row, 4, meal)
