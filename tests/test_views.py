import pytest
from django.urls import reverse
from collections import OrderedDict

def test_api_parse_succeds(client):
    address_string = '123 main st chicago il'

    expected_return_input_string = '123 main st chicago il'
    expected_return_address_components = OrderedDict([('AddressNumber', '123'), ('StreetName', 'main'), ('StreetNamePostType', 'st'), ('PlaceName', 'chicago'), ('StateName', 'il')])
    excpected_return_address_type = 'Street Address'

    url = reverse('address-parse')
    # send address string to API endpoint
    response = client.get(url, {'input_string': address_string})

    assert response.status_code == 200
    assert response.data['input_string'] == expected_return_input_string
    assert response.data['address_components'] == expected_return_address_components
    assert response.data['address_type'] == excpected_return_address_type
    # pytest.fail()


def test_api_parse_raises_error(client):
    address_string = '123 main st chicago il 123 main st'

    url = reverse('address-parse')
    # send address string to API endpoint
    response = client.get(url, {'input_string': address_string})

    # if the backend cannot parse, it returns error code 400
    # thus we can simply check that we recieved the error code 
    assert response.status_code == 400
