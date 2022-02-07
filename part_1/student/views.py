from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q


def student_list_(request):

    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})

######################   01_OR_Queries   #######################

def student_list_(request):
    posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(surname__startswith='baldwin')

    print(posts)
    print(connection.queries)
    return render(request, 'output.html', {'posts': posts})


def student_list_(request):
    posts = Student.objects.filter(Q(surname__startswith='austin') | ~Q(surname__startswith='baldwin')
                                   | Q(surname__startswith='avery-parker'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})

#######################   02_AND_Queries   #######################

def student_list_(request):
    posts = Student.objects.filter(classroom=1) & Student.objects.filter(age=20)

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})

def student_list_(request):
    posts = Student.objects.filter(Q(firstname__startswith='lakisha') & Q(surname__startswith='baldwin'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


#######################   03_UNION_Queries   #######################

def student_list_(request):
    posts = Student.objects.all().values('firstname', 'surname').union(Teacher.objects.all().values('firstname', 'surname'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})

#######################   04_NOT_Queries   #######################

def student_list_(request):
    posts = Student.objects.exclude(age=20)

    posts = Student.objects.exclude(age__gt=20)  # >
    posts = Student.objects.exclude(age__gte=20) # >=
    posts = Student.objects.exclude(age__lt=20)  # <
    posts = Student.objects.exclude(age__lte=20) # <=


    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})

def student_list_(request):
    posts = Student.objects.filter(~Q(age__gt=20) & ~Q(firstname__startswith='shaina'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})

####################### SELECT & OUTPUT INDIVIDUAL FIELDS #####################

def student_list(request):
    posts = Student.objects.filter(classroom=1).only('firstname', 'surname').union(Teacher.objects.filter(firstname__startswith='trellany'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})
