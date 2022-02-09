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


def student_list_(request):
    posts = Student.objects.filter(classroom=1).only('firstname', 'surname').union(Teacher.objects.filter(firstname__startswith='trellany'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})


####################### SIMPLE RAW QUERIES #####################


def student_list_(request):
    posts = Student.objects.raw("SELECT * FROM student_student")
    posts = Student.objects.raw("SELECT * FROM student_student WHERE age=21")

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'x': posts})


####################### SIMPLE RAW QUERIES, bypassing the ORM #####################

def student_list_(request):
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) FROM student_student")
    r = cursor.fetchone()
    print(r)

    return render(request, 'output.html', {'posts': r})


def student_list(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM student_student WHERE age > 20")
    r = dictfetchall(cursor)
    print(r)

    return render(request, 'output.html', {'x': r})


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
