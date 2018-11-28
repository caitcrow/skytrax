
import xlrd

airline_data = ("data/airlinedetailed.csv")
airport_data = ("data/airportdetailed.csv")
lounge_data = ("data/loungedetailed.csv")
seat_data = ("data/seatdetailed.csv")

wb = xlrd.open_workbook(airline_data)
sheet = wb.sheet_by_index(0);

sheet.cell_value(0,0)
for i in range(sheet.ncols):
    print(sheet.cell_value(0,i))
