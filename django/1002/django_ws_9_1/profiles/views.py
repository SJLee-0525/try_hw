from django.shortcuts import render
from accounts.models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'profiles/index.html', context)