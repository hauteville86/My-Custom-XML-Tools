import json

file = open("messages_en.properties")

newFile = open("i18_en.js", 'w')

lines = file.readlines()

i18n_dictionary = {}

def update_i18n_dictionary(element_indicators, element_value):
	current_node = i18n_dictionary
	for i in range(len(element_indicators)):
		element_indicator = element_indicators[i]
		old_node = current_node
		try:
			current_node = current_node[element_indicator]
		except KeyError:
			current_node = None
		if (current_node == None):
			if (i == len(element_indicators) - 1):
				current_node = element_value
			else:
				current_node = {}
			old_node[element_indicator] = current_node

def convert_line(line):
	line_elements = line.split('=')
	element_indicators = line_elements[0].split('.')
	element_value = line_elements[1]
	update_i18n_dictionary(element_indicators, element_value)

def convert_to_string(i18n_dictionary):
	result = ''
	i18n_list = str(i18n_dictionary).split(' ')
	for i in range(len(i18n_list)):
		element = i18n_list[i]
		if element.endswith(':'):
			newElement =''
			for j in range(len(element)):
				character = element[j]
				if not character == '\'':
					newElement += character
			element = newElement
		result += element
	print(result)
	return result

for i in range(len(lines)):
	line = lines[i].strip()
	if not (str(line).startswith('#')) and (str(line).strip()):
		convert_line(line)

result_string = convert_to_string(i18n_dictionary)
newFile.write('export default ')

newFile.write(result_string)