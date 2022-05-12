import random

from django.http import HttpResponse


def home_view(request):
    name = "sajal"
    number = random.randint(1, 1000)
    h1_str = f"""
    <h1> Hello {name}, {number} </h1>
    """

    return HttpResponse(h1_str)
