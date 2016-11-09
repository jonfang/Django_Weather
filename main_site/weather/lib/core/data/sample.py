sample = []
with open('city_names.txt') as data:
	for _id in data:
		sample.append(_id.rstrip())
print(sample)
