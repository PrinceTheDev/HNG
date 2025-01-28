import os
from django.http import JsonResponse
from datetime import datetime

def public_api(request):
    return JsonResponse({
        'email': 'sinbadprince9@gmail.com',
        'current_datetime': datetime.utcnow().isoformat() + 'Z',
        'github_url': 'https://github.com/PrinceTheDev/HNG'
    })
