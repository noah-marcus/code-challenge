import pytest
from django.urls import reverse
from collections import OrderedDict

def test_api_parse_succeds(client):
    address_string = '123 main st chicago il'

    expected_return_address_components = OrderedDict([('AddressNumber', '123'), ('StreetName', 'main'), ('StreetNamePostType', 'st'), ('PlaceName', 'chicago'), ('StateName', 'il')])
    expected_return_address_type = 'Street Address'

    url = reverse('address-parse')
    # send address string to API endpoint
    response = client.get(url, {'input_string': address_string})

    assert response.status_code == 200
    assert response.data['input_string'] == address_string
    assert response.data['address_components'] == expected_return_address_components
    assert response.data['address_type'] == expected_return_address_type


def test_api_parse_raises_error(client):
    address_string = '123 main st chicago il 123 main st'

    # WIP - This is not currently working
    expected_error_message = "ERROR: Unable to tag this string because more than one area of the string has the same label\n\nORIGINAL STRING:  123 main st chicago il 123 main st\nPARSED TOKENS:    [('123', 'AddressNumber'), ('main', 'StreetName'), ('st', 'StreetNamePostType'), ('chicago', 'PlaceName'), ('il', 'StateName'), ('123', 'AddressNumber'), ('main', 'StreetName'), ('st', 'StreetNamePostType')]\nUNCERTAIN LABEL:  AddressNumber\n\nWhen this error is raised, it's likely that either (1) the string is not a valid person/corporation name or (2) some tokens were labeled incorrectly\n\nTo report an error in labeling a valid name, open an issue at https://github.com/datamade/usaddress/issues/new - it'll help us continue to improve probablepeople!\n\nFor more information, see the documentation at https://usaddress.readthedocs.io/"

    url = reverse('address-parse')
    # send address string to API endpoint
    response = client.get(url, {'input_string': address_string})
   
    # if the backend cannot parse, it returns error code 400 and passes on error name
    assert response.status_code == 400
    assert response.data['detail'] == expected_error_message
