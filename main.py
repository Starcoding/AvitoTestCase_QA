import json


fullfilled = {
    'params': []
}
ERROR = """{
    "error": {
    "message": "Входные файлы некорректны"
    }
} 
"""


def error():
    with open("error.json", "w") as error_file:
        error_file.write(ERROR)


def load_file(file_path):
    handler = {}
    with open(file_path) as structure_file:
        try:
            handler = json.load(structure_file)
        except:
            print("Error with structure")
            error()
    return handler


def validate_top(parametr, values_list):
    for values in values_list:
                if parametr['id'] == values['id']:
                    temp_parent_param = {
                            "id": parametr['id'],
                            "title": parametr['title'],
                            "value": values['value']
                        }
    return temp_parent_param


def validate_middle(parametr, value, values_list):
    temp_value = {
        "id": value['id'],
        "title": value['title']
    }
    if id_check(parametr, value, values_list) != "":
        parametr['value'] = \
            id_check(parametr, value, values_list)
    return temp_value


def id_check(parametr, value, values_list):
    temp_value = ""
    for values in values_list:
        if parametr['id'] == values['id'] and \
                value['id'] == values['value']:
            temp_value = value['title']
            break
    return temp_value


def validate_bottom(parametr, value, values_list):
    for parametr in value['params']:
        temp_param = {
            "id": parametr['id'],
            "title": parametr['title'],
            "value": "",
            "values": []}
        for value in parametr['values']:
            temp_child_value = {
                "id": value['id'],
                "title": value['title']
            }
            if id_check(parametr, value, values_list) != "":
                temp_param['value'] = \
                    id_check(parametr, value, values_list)
            temp_param['values'].append(temp_child_value)  
    return temp_param


def data_validator(structure_list, values_list):
    values_list = values_list['values']
    for parent_param in structure_list['params']:
        temp_parent_param = {
            "id": parent_param['id'],
            "title": parent_param['title'],
            "value": "",
            "values": []
        }
        if 'values' not in parent_param:
            temp_parent_param = validate_top(parent_param, values_list)
        else:
            for value in parent_param['values']:
                if id_check(parent_param, value, values_list) != "":
                    temp_parent_param['value'] = \
                        id_check(parent_param, value, values_list)
                temp_value = {
                    "id": value['id'],
                    "title": value['title'],
                    "params": []}
                if 'params' in value:                    
                    for child_param in value['params']:
                        temp_param = \
                            validate_bottom(child_param, value, values_list) 
                        temp_value['params'].append(temp_param)
                    temp_parent_param['values'].append(temp_value)
                else:
                    temp_value = \
                        validate_middle(parent_param, value, values_list)
                    temp_parent_param['values'].append(temp_value)
        fullfilled['params'].append(temp_parent_param)


def save_file(data):
    with open("StructureWithValues.json", "w") as output_file:
        json.dump(data, output_file)


if __name__ == '__main__':
    structure = load_file("TestcaseStructure.json")
    values = load_file("Values.json")
    data_validator(structure, values)
    with open('StructureWithValues.json', 'w', encoding='utf8') as outfile:
        json.dump(fullfilled, outfile, ensure_ascii=False)
    # print(json.dumps(fullfilled, indent=4))
    print(load_file("Values.json"))