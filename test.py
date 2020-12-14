import pytest
from main import validate_top, validate_middle, validate_bottom, check_id, data_validator

def test_validate_top():
    parametr = {'id': 34, 'title': 'testcaseId', 'value': ''}
    values_list = [{'id': 34, 'value': 298}, {'id': 146, 'value': 'Валидация параметров на подаче объявления'}, {'id': 73, 'value': 345}, {'id': 230, 'value': 4931}, {'id': 122, 'value': 646}, {'id': 1373, 'value': 7204}, {'id': 421, 'value': 877}, {'id': 2128, 'value': 3627}]
    t_validate_top = validate_top(parametr, values_list)
    expected = {'id': 34, 'title': 'testcaseId', 'value': 298}
    assert t_validate_top == expected


def test_validate_middle():
    parametr = {'id': 421, 'title': 'Priority', 'value': '', 'values': [{'id': 877, 'title': 'High'}, {'id': 879, 'title': 'Low'}]}
    value = {'id': 877, 'title': 'High'}
    values_list = [{'id': 34, 'value': 298}, {'id': 146, 'value': 'Валидация параметров на подаче объявления'}, {'id': 73, 'value': 345}, {'id': 230, 'value': 4931}, {'id': 122, 'value': 646}, {'id': 1373, 'value': 7204}, {'id': 421, 'value': 877}, {'id': 2128, 'value': 3627}]
    t_validate_middle = validate_middle(parametr, value, values_list)
    expected = {'id': 877, 'title': 'High'}
    assert t_validate_middle == expected


def test_validate_bottom():
    parametr = {'id': 230, 'title': 'Feature', 'value': '', 'values': [{'id': 4931, 'title': 'Publish item'}, {'id': 4932, 'title': 'Edit item'}]} 
    value = {'id': 345, 'title': 'SellerX', 'params': [{'id': 230, 'title': 'Feature', 'value': '', 'values': [{'id': 4931, 'title': 'Publish item'}, {'id': 4932, 'title': 'Edit item'}]}]}
    values_list = [{'id': 34, 'value': 298}, {'id': 146, 'value': 'Валидация параметров на подаче объявления'}, {'id': 73, 'value': 345}, {'id': 230, 'value': 4931}, {'id': 122, 'value': 646}, {'id': 1373, 'value': 7204}, {'id': 421, 'value': 877}, {'id': 2128, 'value': 3627}]
    t_validate_bottom = validate_bottom(parametr, value, values_list)
    expected = {'id': 230, 'title': 'Feature', 'value': 'Publish item', 'values': [{'id': 4931, 'title': 'Publish item'}, {'id': 4932, 'title': 'Edit item'}]}
    assert t_validate_bottom == expected

def test_check_id():
    parametr = {'id': 2128, 'title': 'Tags', 'value': '', 'values': [{'id': 3624, 'title': 'develop'}, {'id': 3627, 'title': 'production'}]}
    value = {'id': 3624, 'title': 'develop'}
    values_list = [{'id': 34, 'value': 298}, {'id': 146, 'value': 'Валидация параметров на подаче объявления'}, {'id': 73, 'value': 345}, {'id': 230, 'value': 4931}, {'id': 122, 'value': 646}, {'id': 1373, 'value': 7204}, {'id': 421, 'value': 877}, {'id': 2128, 'value': 3627}]
    t_check_id = check_id(parametr, value, values_list)
    expected = ""
    assert t_check_id == expected


def test_data_validator():
    structure_list = {'params': [{'id': 34, 'title': 'testcaseId', 'value': ''}, {'id': 73, 'title': 'unitId', 'value': '', 'values': [{'id': 345, 'title': 'SellerX', 'params': [{'id': 230, 'title': 'Feature', 'value': '', 'values': [{'id': 4931, 'title': 'Publish item'}, {'id': 4932, 'title': 'Edit item'}]}]}, {'id': 346, 'title': 'Trust&Safety', 'params': [{'id': 261, 'title': 'Feature', 'value': '', 'values': [{'id': 4894, 'title': 'Authorize user'}, {'id': 4896, 'title': 'Restore password'}]}]}]}, {'id': 421, 'title': 'Priority', 'value': '', 'values': [{'id': 877, 'title': 'High'}, {'id': 879, 'title': 'Low'}]}, {'id': 2128, 'title': 'Tags', 'value': '', 'values': [{'id': 3624, 'title': 'develop'}, {'id': 3627, 'title': 'production'}]}]}
    values_list = {'values': [{'id': 34, 'value': 298}, {'id': 73, 'value': 345}, {'id': 230, 'value': 4931}, {'id': 122, 'value': 646}]}
    t_data_validator = data_validator(structure_list, values_list)
    expected = {'params': [{'id': 34, 'title': 'testcaseId', 'value': 298}, {'id': 73, 'title': 'unitId', 'value': 'SellerX', 'values': [{'id': 345, 'title': 'SellerX', 'params': [{'id': 230, 'title': 'Feature', 'value': 'Publish item', 'values': [{'id': 4931, 'title': 'Publish item'}, {'id': 4932, 'title': 'Edit item'}]}]}, {'id': 346, 'title': 'Trust&Safety', 'params': [{'id': 261, 'title': 'Feature', 'value': '', 'values': [{'id': 4894, 'title': 'Authorize user'}, {'id': 4896, 'title': 'Restore password'}]}]}]}, {'id': 421, 'title': 'Priority', 'value': '', 'values': [{'id': 877, 'title': 'High'}, {'id': 879, 'title': 'Low'}]}, {'id': 2128, 'title': 'Tags', 'value': '', 'values': [{'id': 3624, 'title': 'develop'}, {'id': 3627, 'title': 'production'}]}]}
    assert t_data_validator == expected