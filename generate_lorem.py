import lorem

index = 1

with open("lorem.txt", "w+") as lorem_file:
	while index < 1000000:
		lorem_file.write(lorem.sentence() + (' (Line Number %s)' % index) + '\n')
		index += 1

# with open("lorem.txt", "w+") as lorem_file:
# 	while index < 100:
# 		if index < 10:
# 			lorem_file.write('testing' + (' (Line Number 0%s)' % index) + '\n')
# 		else:
# 			lorem_file.write('testing' + (' (Line Number %s)' % index) + '\n')
# 		index += 1
# 	