from django.db import models


# Create your models here.
class School(models.Model):
    """A data model representing a school.

    Attributes:
        name (str): The name of the school. VARCHAR max 256.
        principal (str): The name of the school's principal. VARCHAR max 256.
        location (str): The location of the school. VARCHAR max 256.
    """
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Student(models.Model):
    """A data model representing a student.

    Attributes:
        name (str): The name of the school. VARCHAR max 256.
        age (int): The age of the student. NUM (must be positive).
        school (School): The school the student attends. FK to school model
        (table).
    """
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='student', on_delete=models.CASCADE)

    def __str__(self):
        return self.name