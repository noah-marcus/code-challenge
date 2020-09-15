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

        # 'initalize' the response variables
        address_components = {}
        address_type = ""
        status_code = 200

        # pass request address to parse method
        try:
            address_components, address_type = self.parse(input_string)
        except:
            # if user input could not be parsed, set http status code to 400
            # this will act as our way of reporting an error back to the 
            # front end without altering the expected response
            status_code = 400
        
        # generate response JSON
        response_data = { 'input_string': input_string, \
                          'address_components': address_components, \
                          'address_type': address_type }

        # return Response with data and status code
        return Response(response_data, status=status_code)

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
