file = input('Enter csv name:')
if file == '' : file = 'csv_seperate_test_data.csv'

csv_handle = open(file)

seperate_by = int(input('Enter column to seperate by:'))
if seperate_by == None : seperate_by = 1

header = csv_handle.readline()

sorted_info = dict()

for line in csv_handle:
	line = line.rstrip()
	line_parts = line.split(',')
	line_parts = [each.lstrip() for each in line_parts]
	if line_parts[seperate_by] in sorted_info.keys():
		sorted_info[line_parts[seperate_by]].append(line)
	else:
		sorted_info[line_parts[seperate_by]] = [line]
	print(sorted_info)

for key in sorted_info.keys():
	file_name = key + '.csv'
	print(file_name)
	# file_handle = open()
# add in a with statement to auto close the file afterwards
# further error checking to make sure input is a number and not out of range of the columns