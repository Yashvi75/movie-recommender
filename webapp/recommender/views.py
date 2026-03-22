from django.shortcuts import render
from .utils import recommend


def home(request):
    return render(request, 'index.html')


def recommend_view(request):
    if request.method == 'POST':
        movie = request.POST.get('movie')
        recommendations = recommend(movie)
        return render(request, 'index.html', {
            'recommendations': recommendations
        })

    return render(request, 'index.html')