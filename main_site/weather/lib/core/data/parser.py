import json
from pprint import pprint

data=[]
with open('city.list.us.json') as data_file:
	for line in data_file:
		data.append(json.loads(line))
for entry in data:
	print(entry['name'] + ' ,' + entry['country'])
#pprint(data)

