import csv

filename="/home/ec2-user/environment/glassdoor-app/python_library/tech-companies.csv"

# opening the file using "with"
# statement
with open(filename, 'r') as data:
	for line in csv.DictReader(data):
		print(line)
