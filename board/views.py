from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
    return render(request, 'board/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'board/question_detail.html', context)

def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'board/question_detail.html', context)
    # return redirect('board:detail', question_id=question.id)

def question_create(request):
    """
    pybo 질문등록
    """

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        print(request.POST["subject"])
        print(request.POST["content"])
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('board:index')
    else:
        form = QuestionForm()

    context = {'form': form}

    return render(request, 'board/question_form.html', context)