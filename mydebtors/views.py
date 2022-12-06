from django.http import JsonResponse

def Test(request):
    return JsonResponse({'greetings':'Hey Emma'})