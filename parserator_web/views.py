import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    # parse requested address string and return components to frontend 
    #       input: request {input_string; String} from frontend
    #       output: input_string [String], 
    #               address_components [Dictionary {address_part: tag}], 
    #               address_type [String]
    def get(self, request):
        # get user's input_string from request data
        input_string = request.query_params['input_string']

        # pass request address to parse method
        address_components, address_type = self.parse(input_string)
        
        # generate response JSON
        response_data = { 'input_string': input_string, \
                          'address_components': address_components, \
                          'address_type': address_type }
        
        return Response(response_data)

    # return the parsed components of a given address using usaddress
    #       input: address [String]
    #       output: address_components [Dictionary {address_part: tag}],
    #               address_type [String]
    def parse(self, address):
        # using usaddress tag() method to parse address string
        #       input: address string
        #       output: OrderedDict(Address Components), String (Address Type)
        address_components, address_type = usaddress.tag(address)

        return address_components, address_type
