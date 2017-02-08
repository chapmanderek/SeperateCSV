# CVS Seperater

# Todo
# loop back the opening section if the input is invalid or out of bounds, add in a q for quit option
# set page layout to landscape
# turn on fit to width 1 page

import datetime as dt
import os
import xlwt
import openpyxl as opx
from openpyxl.styles import NamedStyle, Font, Alignment, PatternFill, Border, Side

header_style = NamedStyle(name='header_style')
header_style.font = Font(bold=True, size=14, name='Arial')
header_style.alignment = Alignment(horizontal='center')
header_style.fill = PatternFill('solid', 'DCDCDC')
header_style.border = Border(bottom=Side(border_style='thin'))

row_style = NamedStyle(name='row_style')
row_style.font = Font(bold=True, size=12, name='Trebuchet')
row_style.alignment = Alignment(horizontal='left')
row_style.border = Border(bottom=Side(border_style='thin'))

def open_py_output(filename, header, data):
	wbook = opx.Workbook()
	wsheet = wbook.active
	wbook.add_named_style(header_style)
	wbook.add_named_style(row_style)

	header_parts = [ each.lstrip().rstrip() for each in header.split(',') ]
	header_width = len(header_parts)
	wsheet.append(header_parts)

	for row in wsheet.iter_rows():
		for cell in row:
			cell.style = header_style

	# split data list into individual rows then append each on to the spreadsheet
	row_count = 1
	for row in data:
		row_parts = [ each.lstrip().rstrip() for each in row.split(',') ]
		wsheet.append(row_parts)
		row_count += 1

	# add stle for data rows
	for row in wsheet.iter_rows(min_row=2, max_row=row_count):
		for cell in row:
			cell.style = row_style
	
	wsheet.print_options.horizontalcentered = True
	wsheet.page_setup.orientation = "landscape"

	wbook.save(filename)

# get filename
file = input('Enter csv name:')
if file == '' : file = 'csv_seperate_test_data.csv'
csv_handle = open(file)

# read in the header but get rid of trailing new line characters
header = csv_handle.readline().rstrip()

# get column to seperate the file by from user error check so exits gracefully
seperate_by = input('Enter column to seperate by (default is 1):')
if seperate_by == '' : seperate_by = 1
elif seperate_by.isdigit() == True : seperate_by = int(seperate_by)
else:
	print('Not valid input for some reason')
	exit()

# assume user means the 1st column when they say 1 and not the computer 1 which would be the 2nd column 
# make sure the number is a valid column and exit gracefully if not
seperate_by -= 1
if len(header.split(',')) < seperate_by or seperate_by < 0 : print('The number you entered to seperate the worksheet by was no good'); exit()


# seperate the rest of the info into a dict of lists of strings
sorted_info = dict()
for line in csv_handle:
	line = line.rstrip()
	line_parts = line.split(',')
	line_parts = [each.lstrip() for each in line_parts]
	if line_parts[seperate_by] in sorted_info.keys():
		sorted_info[line_parts[seperate_by]].append(line)
	else:
		sorted_info[line_parts[seperate_by]] = [line]

# setup a date stamp for the folder and individual worksheets / create folder
today = dt.date.today()
formatted_date = "{month}-{day}-{year}".format(month=today.month, day=today.day, year=today.year)
dir_name = '{cwd}/{date}'.format(date=formatted_date, cwd=os.getcwd())
if not os.path.exists(dir_name) : os.mkdir(dir_name)

# create the individual sheets
for key in sorted_info.keys():
	file_name = "{dn}/{key}_{date}.xlsx".format(key=key, date=formatted_date, dn=dir_name)
	open_py_output(file_name, header, sorted_info[key])


