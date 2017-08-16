from django.shortcuts import render, reverse
from django.views.generic.edit import CreateView

from .models import Poll

class CreatePoll(CreateView):
    model = Poll
    template_name = 'poll.html'
    fields = ['name', 'last_name', 'last_module', 'email', 'phone_number']

    def get_success_url(self):
        return reverse('polls:thanks')

def thanks(request):
    template = 'thanks.html'
    return render(request, template, context=None)
