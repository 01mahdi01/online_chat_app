from django.shortcuts import render


# Create your views here.
def loby(request):
    return render(request, 'index.html')


def room_name(request, room_name):
    the_room_name = room_name
    return render(request, '{}.html'.format(the_room_name), {"room_name": room_name})

