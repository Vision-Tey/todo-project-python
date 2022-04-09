from django.http import HttpResponse

def todos(request):
    return HttpResponse("Hello there!")


def home(request):
    return HttpResponse("Homepage!")


