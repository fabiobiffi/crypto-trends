from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
import requests

from backend.crypto_trends.crypto_trends.settings import API_SECRET_KEY, API_BASE_URL


@api_view(['GET'])
def ajax_table_overview(request):
    """
    Ajax for getting data about all cryptocurrencies
    :param request: the HttpRequest element
    :return: the json about all cryptocurrencies
    """

    url = f"{API_BASE_URL}/currencies/ticker?key={API_SECRET_KEY}"
    response = requests.get(url)
    response_dict = response.json()

    return Response(response_dict)
