from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return str('Group' + self.name)

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100)
    birthday = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    def __str__(self):
        return str('Student' + self.last_name + self.first_name)

class Discipline(models.Model):
    name = models.CharField(max_length=200)
    semester = models.PositiveIntegerField()
    students = models.ManyToManyField(
        Student,
        through='StudentDiscipline',
        related_name='disciplines',
    )
    def __str__(self):
        return f'Discipline {self.semester} {self.name}'


class Mark(models.Model):
    MARK_CHOICES = [
        ("2", "2 — неудовлетворительно"),
        ("3", "3 — удовлетворительно"),
        ("4", "4 — хорошо"),
        ("5", "5 — отлично"),
        ("passed", "Зачтено"),
        ("failed", "Не зачтено"),
        ("not_attested", "Не аттестовано"),
    ]
    value = models.CharField(max_length=20, choices=MARK_CHOICES)
    def __str__(self):
        return str('Mark')


class StudentDiscipline(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'discipline'],
                name='unique_student_discipline',
            )
        ]

    def __str__(self):
        return ('StudentDiscipline')