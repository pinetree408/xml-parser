from xml.etree.ElementTree import parse

def parser(file):
    tree = parse(file)
    root = tree.getroot()
    result = {}
    for i in range(len(root.getchildren())):
        first_level = root.getchildren()[i]
	first_level_name = (first_level.get('name') == None) and first_level.tag or first_level.get('name')
	first_level_name += "_" + str(i)
        if len(first_level.getchildren()) != 0:
            first_level_result = {}
            for j in range(len(first_level.getchildren())):
                second_level = first_level.getchildren()[j]
		second_level_name = (second_level.get('name') == None) and second_level.tag or second_level.get('name')
		second_level_name += "_" + str(j)
	        if len(second_level.getchildren()) != 0:
                    second_level_result = {}
		    for k in range(len(second_level.getchildren())):
                        third_level = second_level.getchildren()[k]
		        third_level_name = (third_level.get('name') == None) and third_level.tag or third_level.get('name')
		        third_level_name += "_" + str(k)
                        second_level_result[third_level_name] = third_level.text
		    first_level_result[second_level_name] = second_level_result
	        else:
                    first_level_result[second_level_name] = second_level.text
            result[first_level_name] = first_level_result
        else: 
            result[first_level_name] = first_level.text

    return result
