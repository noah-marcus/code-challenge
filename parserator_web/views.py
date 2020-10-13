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

    def get(self, request):
        """Parse requested address string and return components to frontend 

        Arguments
            request - request from frontend {input_string; String} 

        Output
            input_string [String]
            address_components [Dictionary {address_part: tag}]
            address_type [String]
        """

        # get user's input_string from request data
        input_string = request.query_params['input_string']

        # 'initalize' the response variables
        address_components = {}
        address_type = ""

        # pass request address to parse method
        try:
            address_components, address_type = self.parse(input_string)
        except Exception as e:
  
            raise ParseError(detail=e.__class__.__name__, code=400)
        
        # generate response JSON
        response_data = { 'input_string': input_string, \
                          'address_components': address_components, \
                          'address_type': address_type}

        # return Response with data and status code
        return Response(response_data)


    def parse(self, address):
        """Return the parsed components of a given address using usaddress

        Arguments
            address [String]
        
        Output
            address_components [Dictionary {address_part: tag}]
            address_type [String]
        """


        # using usaddress tag() method to parse address string
        #       input: address string
        #       output: OrderedDict(Address Components), String (Address Type)
        address_components, address_type = usaddress.tag(address)

        return address_components, address_type
