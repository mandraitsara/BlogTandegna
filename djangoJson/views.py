from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return render(request, "ajax/index.html")

@csrf_exempt
def compute(request):
    a = request.POST["a"]
    b = request.POST["a"]
    result = int(a) + int(b)
    return JsonResponse({"operation_result":result})