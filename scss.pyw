import re
import glob

def parce(line, width):
	containsPx = line.find('px')
	if containsPx != -1:
		patternString = "\s\d*?px"
		matchString = re.findall(patternString, line)
		for j in matchString:
			matchString2 = re.search(patternString, line)
			# newStr = re.sub(patternString, repl, line, count=0)
			# print(matchString2)
			# print(matchString2.group(0))
			# print(float(matchString2.group(0)[1:-2]))
			# print(float(matchString2.group(0)[1:-2])/width)
			# print(str(((float(matchString2.group(0)[1:-2]))/width)*100))
			line = line.replace(matchString2.group(0), ' ' + str(((float(matchString2.group(0)[1:-2]))/width)*100) + 'vw', 1)
	return line
def parsScss(lines):
	# 0 - mob
	# 1 - tablet
	# 2 - netbuk
	# 3 - pc
	typeOfDevice = 0
	output = ''
	for i in lines:
		containsMedia = i.find('media')
		if containsMedia != -1:
			typeOfMedia = re.search("\s\d*?px", i).group(0)[1:-2]
			if (int(typeOfMedia) == 768):
				typeOfDevice = 1
			elif (int(typeOfMedia) == 992):
				typeOfDevice = 2
			else:
				typeOfDevice = 3
			output += i + '\n'
			continue
		if (typeOfDevice == 0):
			output += parce(i, 320)  + '\n'
		elif (typeOfDevice == 1):
			output += parce(i, 991)  + '\n'
		elif (typeOfDevice == 2):
			output += parce(i, 1199)  + '\n'
		else:
			output += parce(i, 1920) + '\n'
	return output
for filename in glob.glob('*.scss'):
	file = open(filename, "r")
	filein = file.read()
	lines = filein.split('\n')
	file = open(filename, "w")
	file.write(parsScss(lines))

