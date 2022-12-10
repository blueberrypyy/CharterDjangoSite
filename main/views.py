from django.shortcuts import render

def anogram_view(request):
    return render(request, 'main/base.html', {})
