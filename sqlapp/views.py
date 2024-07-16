from django.shortcuts import render
from django.http import JsonResponse
from .sql_engine import SimpleSQLEngine

engine = SimpleSQLEngine()

def index(request):
    return render(request, 'sqlapp/main.html')

def execute(request):
    query = request.GET.get('query', '')
    if not query:
        return JsonResponse({'result': 'No query provided'})

    try:
        result = engine.execute(query)
    except Exception as e:
        result = str(e)

    return JsonResponse({'result': result})
