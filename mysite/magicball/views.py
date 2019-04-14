from django.shortcuts import render
from django.http import HttpResponse

import random
from .models import OracleRecord

def index(request):

    magicball = ['The future is cloudy.', 'It has been decided in your favor.', 'You never know.', 'Try Again', 'The outlook is favorable.']
    if request.method == 'POST':
        computer_choice = random.choice(magicball)
        oracle_record = OracleRecord(computer_choice=computer_choice)
        oracle_record.save()
        return render(request, 'magicball/index.html', {'computer_choice': computer_choice})

    return render(request, 'magicball/index.html', {})


    # if request.method == 'POST':
    #     computer_choice = random.choice(magicball)
    #     oracle_record = OracleRecord(computer_choice=computer_choice)
    #     oracle_record.save()
    #     return render(request, 'magicball/index.html', {'magicball': magicball, 'computer_choice': computer_choice})
    #
    # return render(request, 'magicball/index.html', {'magicball': magicball})
    #
