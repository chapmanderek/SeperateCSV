file = input('Enter csv name:')
if file == '' : file = 'csv_sort_test_data.csv'

csv_handle = open(file)

# further error checking to make sure it is a number and not out of range of the columns
seperate_by = int(input('Enter column to seperate by:'))
if seperate_by == None : seperate_by = 1

header = csv_handle.readline()
print(header)

sorted_info = dict()
names_seen = list()

for line in csv_handle.readline():
	print(line)
	line_parts = line.split(',')
	print(line_parts)
	print(line_parts[seperate_by])

