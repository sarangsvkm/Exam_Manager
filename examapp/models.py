from django.db import models



class Exam(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20)
    exam_date = models.DateField()
    exam_time = models.TimeField()
    semester = models.CharField(max_length=10)
    exam_slot = models.CharField(max_length=10)

    def __str__(self):
        return self.subject_name


