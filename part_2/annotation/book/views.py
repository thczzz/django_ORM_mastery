from django.shortcuts import render
from django.db.models import Count, OuterRef, Subquery, Sum
from .models import BookData, BookChapterData
# Create your views here.


def examples(request):
    # Example 1
    # Add total num of chapters to each book in the queryset
    """query = BookData.objects.annotate(chapters_cnt=Count('bookchapterdata'))"""

    # Example 2
    # Now we want to have all the books with at least 3 chapters, sorted with chapters count.
    """query = BookData.objects.annotate(chapters_cnt=Count('bookchapterdata')).\
        filter(chapters_cnt__gte=3).order_by('-chapters_cnt')"""

    # Example 3
    """ We want to have the total number of topics from those ‘easy’ chapters which have MCQ’s
    available(Refer to the model image). To break it down, we want to calculate the sum of num_of_topics,
    with is_mcq_available=True and difficulty=’easy’ """

    chapter_subquery = BookChapterData.objects. \
        filter(book=OuterRef('id'), is_mcq_available=True, difficulty='easy'). \
        order_by().values('book_id'). \
        annotate(sum_of_topics=Sum('num_of_topics')). \
        values('sum_of_topics')

    query = BookData.objects.annotate(easy_mcq_topics_cnt=Subquery(chapter_subquery))

    return render(request, "index.html", {'data': query})
