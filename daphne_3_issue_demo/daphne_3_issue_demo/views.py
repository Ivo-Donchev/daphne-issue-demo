import time
from django.http import HttpResponse


def make_it_slow():
    """
    Sleep for 3 seconds to demostrate the paralle issue
    """
    print('Sleeping for 3 seconds')

    for i in range(3):
        time.sleep(1)
        print(i)


def view_1(request):
    make_it_slow()
    return HttpResponse('view_1 response')


def view_2(request):
    make_it_slow()
    return HttpResponse('view_2 response')
