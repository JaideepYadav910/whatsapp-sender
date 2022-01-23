def clean_file(file):
	file = open(file,"r+",encoding='utf-8-sig')

	file.truncate(0)
	
	file.close()

def read_file(file, array=False):
	f = open(file, "r",encoding='utf-8-sig')
	lines = f.read()

	if array:
		lines = lines.split('\n')

	f.close()

	return lines

def write_file(file, message):
	f = open(file, "a",encoding='utf-8-sig')
	f.write(f"{message}\n")

	f.close()

	return "Success"
