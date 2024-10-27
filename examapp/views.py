from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ExamForm
from .models import Exam
from datetime import datetime


def exam_list(request):
    exams = Exam.objects.all().order_by('exam_date')
    today = datetime.today().date()

    # Calculate the days until the next exam and gaps between exams
    for exam in exams:
        exam.days_until = (exam.exam_date - today).days

    return render(request, 'exam_list.html', {'exams': exams})


def add_exam(request):
    if request.method == 'POST':
        try:
            subject_name = request.POST['subject_name']
            subject_code = request.POST['subject_code']
            exam_date = request.POST['exam_date']
            exam_time = request.POST['exam_time']  # This will now be in HH:MM:SS format
            semester = request.POST['semester']
            exam_slot = request.POST['exam_slot']

            # Create and save the Exam instance
            Exam.objects.create(
                subject_name=subject_name,
                subject_code=subject_code,
                exam_date=exam_date,
                exam_time=exam_time,
                semester=semester,
                exam_slot=exam_slot
            )
            return redirect('/')  # Redirect to the exam list or any other page

        except ValidationError as e:
            return render(request, 'add_exam.html', {'error': e.messages})

    return render(request, 'add_exam.html')


def update_exam(request, id):
    exam = get_object_or_404(Exam, id=id)

    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()  # Save the updated exam details
            return redirect('exam_list')  # Redirect to the exam list after updating
    else:
        form = ExamForm(instance=exam)  # Prepopulate the form with the current exam details

    return render(request, 'update_exam.html', {'form': form, 'exam': exam})


