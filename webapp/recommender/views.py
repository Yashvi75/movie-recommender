from django.shortcuts import render
from .utils import recommend


def home(request):
    return render(request, 'index.html')


def recommend_view(request):
    if request.method == 'POST':
        movie = request.POST.get('movie')
        names, posters = recommend(movie)

        movie_data = zip(names, posters)

        return render(request, 'index.html', {
            'movie_data': movie_data
        })

    return render(request, 'index.html')