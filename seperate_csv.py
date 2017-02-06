# CVS Seperater

# Todo
# add in a with statement to auto close the file afterwards
# further error checking to make sure input is a number and not out of range of the columns
# http://stackoverflow.com/questions/13437727/python-write-to-excel-spreadsheet

import datetime as dt
import os
import xlwt
import openpyxl as ox

def open_py_output(filename, header, data):
	oxbook = ox.Workbook()
	oxsheet = oxbook.active

	header_parts = [ each.lstrip().rstrip() for each in header.split(',') ]
	oxsheet.append(header_parts)

	# split data list into individual rows then split that into a list of indvidual cells
	for row in data:
		row_parts = [ each.lstrip().rstrip() for each in row.split(',') ]
		oxsheet.append(row_parts)

	oxbook.save(filename)

def xcel_output(filename, header, data):

	book = xlwt.Workbook()
	sheet = book.add_sheet('sheet1')

	# write header
	column = 0
	for each in header.split(','):
		sheet.write(0, column, each)
		column += 1

	# # write individual entries  row would be the each counter  sheet(row, column, info)
	row = 1
	for each in range(len(data)):
		column = 0
		row_parts = data[each].split(',')
		print(row_parts)
		for cell in row_parts:
			sheet.write(row, column, cell)
			column += 1

	book.save(filename)


# get filename and column to seperate the file by from user
file = input('Enter csv name:')
if file == '' : file = 'csv_seperate_test_data.csv'
csv_handle = open(file)

seperate_by = int(input('Enter column to seperate by:'))
if seperate_by == None : seperate_by = 1

# read in the header but get rid of trailing new line characters
header = csv_handle.readline().rstrip()

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

	# new way exporting to excel
	file_name = "{dn}/{key}_{date}.xlsx".format(key=key, date=formatted_date, dn=dir_name)
	# xcel_output(file_name, header, sorted_info[key])
	open_py_output(file_name, header, sorted_info[key])
	

	# old way exporting to csvs
	# file_name = "{dn}/{key}_{date}.csv".format(key=key, date=formatted_date, dn=dir_name)
	# file_handle = open(file_name, 'w')
	# format_line = '{}\n'

	# file_handle.write(format_line.format(header))
	# for each in range(len(sorted_info[key])):
	# 	file_handle.write(format_line.format(sorted_info[key][each]))
	# file_handle.close()

