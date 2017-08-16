from django.shortcuts import render


def poll(request):
    template = 'poll.html'
    return render(request, template, None)
