from django.http import JsonResponse
from datetime import datetime

def ping(request):
    return JsonResponse({'ping': 'pong', 'date': datetime.now().isoformat()})