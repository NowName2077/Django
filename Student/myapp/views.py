from django.shortcuts import render
from .models import Student, Group
from django.db.models import Q, Count
# Create your views here.
def home(request):
    context = {}
    return render(request, 'myapp/home.html', context)

def about(request):
    context = {}
    return render(request, 'myapp/about.html', context)

def students(request):
    context = {}
    return render(request, 'myapp/students.html', context)

def get_students(request):
    students_all = Student.objects.all()

    try:
        student_get = Student.objects.get(id=1)
    except Student.DoesNotExist:
        student_get = None

    student_first = Student.objects.order_by("last_name").first()
    student_last = Student.objects.order_by("last_name").last()

    students_count = Student.objects.count()

    context = {
        "students_all": students_all,
        "student_get": student_get,
        "student_first": student_first,
        "student_last": student_last,
        "students_count": students_count,
    }
    return render(request, 'myapp/students/GetStudents.html', context)


def filter_students(request):
    students_filter = Student.objects.filter(
        group__name="410"
    )

    students_exclude = Student.objects.exclude(
        group__name="410"
    )

    students_contains = Student.objects.filter(
        last_name__icontains="ов"
    )

    students_in = Student.objects.filter(
        group__name__in=["410", "416"]
    )

    students_q = Student.objects.filter(
        Q(group__name="410") |
        Q(group__name="416")
    )

    context = {
        "students_filter": students_filter,
        "students_exclude": students_exclude,
        "students_contains": students_contains,
        "students_in": students_in,
        "students_q": students_q,
    }
    return render(request, 'myapp/students/FilterStudents.html', context)


def sort_students(request):
    students_ordered = Student.objects.order_by(
        "last_name",
        "first_name"
    )

    students_values = Student.objects.values(
        "last_name",
        "first_name",
        "email",
    )

    students_values_list = Student.objects.values_list(
        "last_name",
        "first_name",
    )

    context = {
        "students_ordered": students_ordered,
        "students_values": students_values,
        "students_values_list": students_values_list,
    }
    return render(request, 'myapp/students/SortStudents.html', context)


def query_students(request):
    students_select_related = Student.objects.select_related(
        "group"
    )

    students_prefetch = Student.objects.prefetch_related(
        "disciplines"
    )

    groups = Group.objects.prefetch_related(
        "students"
    )

    students_disciplines = Student.objects.prefetch_related(
        "disciplines"
    )

    students_annotated = Student.objects.annotate(
        discipline_count=Count("disciplines")
    )

    students_aggregate = Student.objects.aggregate(
        total=Count("id")
    )

    students_chain = (
        Student.objects
        .filter(group__name="410")
        .order_by("last_name", "first_name")
    )

    students_sql = students_chain.query

    students_without_prefetch = Student.objects.all()

    students_with_prefetch = Student.objects.prefetch_related(
        "disciplines"
    )

    context = {
        "students_select_related": students_select_related,
        "students_prefetch": students_prefetch,
        "groups": groups,
        "students_disciplines": students_disciplines,
        "students_annotated": students_annotated,
        "students_aggregate": students_aggregate,
        "students_chain": students_chain,
        "students_sql": students_sql,
        "students_without_prefetch": students_without_prefetch,
        "students_with_prefetch": students_with_prefetch,
    }
    return render(request, 'myapp/students/QueryStudents.html', context)