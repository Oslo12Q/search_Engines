from django.test import TestCase

# Create your tests here.
from django.http import HttpResponse


def test(request):
    return HttpResponse('test ok.')



