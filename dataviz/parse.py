import csv
import numpy

MY_FILE = "sample_data.csv"

def parse(file, delimiter):
	"""Parse csv data to JSON-like object"""

	# Open CSV
	opened_file = open(file)

	# Read CSV
	data = csv.reader(opened_file, delimiter=delimiter)

	# Build data structure
	parsed_data = []
	fields = next(data)
	for row in data:
		parsed_data.append(dict(zip(fields, row)))

	# Close CSV
	opened_file.close()

	return parsed_data

def main():
	data = parse(MY_FILE, ",")
	print(data)

if __name__ == "__main__":
	main()
