from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from publisher_subs_app.tasks import add, subtract, multiply
from .models import CeleryTasks
import time

from celery import shared_task
from breachlock_proj.celery import *

def calculator(request, a, b):
    result = add_numbers.delay(a, b)
    return render(request, 'publisher_subs_app/result.html', {'task_id': result.id})

from django.http import JsonResponse
from celery.result import AsyncResult


from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def check_result(request, task_id):
    # Check the status and result of the Celery task using AsyncResult
    result = app.AsyncResult(task_id)
    print("task_id", result, task_id, type(task_id), result.status, result.ready())
    if result.ready():
        # Task has completed, retrieve the result
        data = {'status': 'completed', 'result': result.result}
    else:
        # Task is still pending or running
        data = {'status': 'pending'}
    
    return JsonResponse(data)



class NumbersInputView(APIView, TemplateView):
    template_name = 'publisher_subs_app/numbers_input.html'  

    def get(self, request):
        return self.render_to_response({})

    def post(self, request):
        number1 = int(request.POST.getlist('number1')[0])
        number2 = int(request.POST.getlist('number2')[0])
        print('numbers ', number1 , number2)
        add_task_id = add.apply_async(args=(number1, number2), queue='addition')
        sub_task_id = subtract.apply_async(args=(number1, number2), queue='subtraction')
        mul_task_id = multiply.apply_async(args=(number1, number2), queue='multiplication')
        CeleryTasks.objects.create(queue_name = 'addition', task_id = add_task_id.id)
        CeleryTasks.objects.create(queue_name = 'subtraction', task_id = sub_task_id.id)
        CeleryTasks.objects.create(queue_name = 'multiplication', task_id = mul_task_id.id)
        return render(request, 'publisher_subs_app/result.html', {'task_ids': [add_task_id.id, sub_task_id.id, mul_task_id.id]})


def check_result_of_a_queue(request, queue_name):
    all_task_ids = list(CeleryTasks.objects.filter(queue_name = queue_name).values_list('task_id',flat=True))
    return render(request, 'publisher_subs_app/result.html', {'task_ids': all_task_ids})


