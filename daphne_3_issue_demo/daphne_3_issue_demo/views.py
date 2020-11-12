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


def view_1(request):  # Url is `/1/`
    make_it_slow()  # Sleeps for 3 seconds
    return HttpResponse('view_1 response')


def view_2(request):  # Url is `/2/`
    make_it_slow()  # Sleeps for 3 seconds
    return HttpResponse('view_2 response')
