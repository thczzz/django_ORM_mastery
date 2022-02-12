from django.shortcuts import render
from django.db.models import Sum, Max, Min, Avg, FloatField
from django.db.models.functions import Upper
from .models import Book


def examples(request):
    # Example 1
    """query = Book.objects.all().aggregate(total_ratings_count=Sum('ratings_count'), max=Max('ratings_count'),
                                          min=Min('ratings_count'), avg=Avg('ratings_count'))"""

    # Example 2
    # Difference between the highest average rating book and the average rating of all books.
    """query = Book.objects.aggregate(rating_diff=Max('average_rating', 
                                    output_field=FloatField()) - Avg('average_rating'))"""


    # Example 3
    # Filter and aggregate
    """query = Book.objects.filter(authors="John McPhee").aggregate(Avg('average_rating'),
                                                                 Min('average_rating'), Max('average_rating'))"""

    # Example 4
    """query = Book.objects.filter(authors="John McPhee").annotate(upper_authors=Upper('authors'))"""

    # Example 5
    avg = Book.objects.all().aggregate(Avg('average_rating'))
    query = round(avg["average_rating__avg"], 0)

    return render(request, "index.html", {"data": query})
