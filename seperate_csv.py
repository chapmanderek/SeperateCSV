# CVS Seperater

# Todo
# date stamp each file
# put them in a date stamped folder
# add in a with statement to auto close the file afterwards
# further error checking to make sure input is a number and not out of range of the columns

file = input('Enter csv name:')
if file == '' : file = 'csv_seperate_test_data.csv'

csv_handle = open(file)

seperate_by = int(input('Enter column to seperate by:'))
if seperate_by == None : seperate_by = 1

header = csv_handle.readline().rstrip()

sorted_info = dict()

for line in csv_handle:
	line = line.rstrip()
	line_parts = line.split(',')
	line_parts = [each.lstrip() for each in line_parts]
	if line_parts[seperate_by] in sorted_info.keys():
		sorted_info[line_parts[seperate_by]].append(line)
	else:
		sorted_info[line_parts[seperate_by]] = [line]



for key in sorted_info.keys():
	file_name = key + '.csv'
	file_handle = open(file_name, 'w')
	format_line = '{}\n'

	file_handle.write(format_line.format(header))
	for each in range(len(sorted_info[key])):
		file_handle.write(format_line.format(sorted_info[key][each]))
	file_handle.close()
