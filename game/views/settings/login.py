from django.http import JsonResponse
from django.contrib.auth import authenticate, login


def signin(request):
    data = request.get
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username = username, password = password)
    if not user:
        return JsonResponse({
            'result': "Incorrect Username or Password"
        })
    
    login(request, user)
    return JsonResponse({
        'result': "Success!"
    })