from django.shortcuts import render



def streaming_view(request):
    return render(request, 'streaming.html')

# Create your views here.
