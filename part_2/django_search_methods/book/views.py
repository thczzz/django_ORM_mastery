from django.shortcuts import render
from .forms import PostSearchForm
from .models import Book
# Create your views here.


def search(request):
    form = PostSearchForm()

    context = {
        'form': form
    }

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']

            """ Example 1 - Standard textual queries """
            ## case-sensitive
            # results = Book.objects.filter(title__contains=q)

            ## case-insensitive
            # results = Book.objects.filter(title__icontains=q)

            """ Example 2 - full text search """
            # results = Book.objects.filter(title__search=q)

            """ Example 3 - SearchVector (search against multiple fields) """
            # from django.contrib.postgres.search import SearchVector
            # results = Book.objects.annotate(search=SearchVector('title', 'authors'), ).filter(search=q)

            """ Example 4 - Search Ranking (Found 11127 results with q=harry, therefore we need to paginate results)"""
            # from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
            # vector = SearchVector('title')
            # query = SearchQuery(q)
            # results = Book.objects.annotate(rank=SearchRank(vector=vector, query=query)).order_by('-rank')

            """ Example 5 - Search Ranking Weights (Found 11127 results with q=harry, therefore we need to paginate results) """
            ## here we search with more emphasis on title
            # from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
            # vector = SearchVector('title', weight='A') + SearchVector('authors', weight='B')
            # query = SearchQuery(q)
            # results = Book.objects.annotate(rank=SearchRank(vector=vector, query=query, cover_density=True)).order_by('-rank')

            """ Example 6 - Search TrigramSimilarity & Trigram Distance """
            ## first, we need to install the "pg_trgm" extension in our postgres db trough the pgAdmin
            # from django.contrib.postgres.search import TrigramSimilarity, TrigramDistance
            # results = Book.objects.annotate(similarity=TrigramSimilarity('title', q), ).filter(similarity__gte=0.2).order_by('-similarity')
            # results = Book.objects.annotate(distance=TrigramDistance('title', q), ).filter(distance__lte=0.8).order_by('-distance')

            """ Example 7 - Search Headline """
            # from django.contrib.postgres.search import SearchQuery, SearchVector, SearchHeadline
            # vector = SearchVector('authors')
            # query = SearchQuery(q)
            # results = Book.objects.annotate(search=vector, headline=SearchHeadline('authors', query, start_sel='<span>', stop_sel='</span>')).filter(search=query)

            """ Example 8 - now utilizing the GinIndex """
            from django.contrib.postgres.search import TrigramSimilarity
            # results = Book.objects.filter(title__trigram_similar=q)
            results = Book.objects.filter(title__trigram_similar=q).annotate(similar=TrigramSimilarity('title', q)).order_by('-similar')

            print(results.explain(analyze=True))
            context['results'] = results
            context['q'] = q

    return render(request, 'index.html', context)
