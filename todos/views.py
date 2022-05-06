from django.shortcuts import render
from django.contrib.auth import login, authenticate

# Create your views here.
def loginPage(request):
    
    # print(request.GET.get('q'))

    if request.method == 'POST':
        req = request.POST
        username = req.get('username')
        password = req.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not False:
            login(request, user)
    return render(request, 'login.html')