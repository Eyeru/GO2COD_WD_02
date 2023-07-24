from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Question.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.qtext))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.qtext):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'result.html',context)
    else:
        qu = Question.objects.all().values()
        template = loader.get_template('index.html')
        context = {
        'qu': qu,
        }
        return HttpResponse(template.render(context, request))

