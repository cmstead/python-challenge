#url -- http://www.pythonchallenge.com/pc/def/map.html
import string

letterset = string.letters
aValue = ord('a')
zValue = ord('z')

def normalize(value):
	normalized = value
	if value > zValue:
		normalized = value - 1 - zValue + aValue
	return normalized

def rotChar(character, distance):
	output = ord(character)
	if character in letterset:
		output = normalize(output + distance)
	return chr(output)

def rot(message, distance):
	result = ''
	for character in message:
		result += rotChar(character, distance)
	return result

message = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

print rot(message, 2)

print rot('map', 2)