import json
import sys

newFile = open("output.js", 'w', encoding="utf8")
i18n_dictionary = {}

def update_i18n_dictionary(element_indicators, element_value):
	current_node = i18n_dictionary
	for i in range(len(element_indicators)):
		element_indicator = element_indicators[i]
		old_node = current_node
		try:
			current_node = current_node[element_indicator]
			print(element_indicator)
		except KeyError:
			current_node = None
		if (current_node == None):
			if (i == len(element_indicators) - 1):
				current_node = element_value
			else:
				current_node = {}
			old_node[element_indicator] = current_node

def parse_value_element(source):
	element_value = ''
	source_list = source.split(' ')
	for i in range(len(source_list)):
		source_list_item = source_list[i]
		element_value += source_list_item
		if i < len(source_list) -1:
			element_value += '&'
	return element_value

def convert_line(line):
	line_elements = line.split('=')
	element_indicators = line_elements[0].split('.')
	element_value = parse_value_element(line_elements[1])
	update_i18n_dictionary(element_indicators, element_value)

def convert_key_element(element):
	newElement = ''
	for j in range(len(element)):
		character = element[j]
		if not character == '\'':
			if character == '{' or character == '}':
				character += '\n'
			newElement += character
	return newElement

def convert_value_element(element):
	newElement = ''
	for j in range(len(element)):
		character = element[j]
		if character == '&':
			character = ' '
		newElement += character
	return newElement

def convert_to_string(i18n_dictionary):
	result = ''
	i18n_list = str(i18n_dictionary).split(' ')
	for i in range(len(i18n_list)):
		element = i18n_list[i]
		if element.endswith(':'):
			element = convert_key_element(element)
		else:
			element = convert_value_element(element)
		result += element
	print(result)
	return result

def main(argv):
	file = open(argv[0], encoding="utf8")
	lines = file.readlines()

	for i in range(len(lines)):
		line = lines[i].strip()
		if not (str(line).startswith('#')) and (str(line).strip()):
			convert_line(line)

	result_string = convert_to_string(i18n_dictionary)
	if(len(result_string)):
		print('New file ' + newFile.name + ' has been generated.')
	newFile.write('export default ')

	newFile.write(result_string)

if __name__ == "__main__":
    main(sys.argv[1:])

