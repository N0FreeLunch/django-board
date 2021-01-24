from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Question

# Create your views here.
def index(request):
    page = request.GET.get('page', '1')

    question_list = Question.objects.order_by('-create_date')
    # context = {'question_list': question_list}

    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    # print(page_obj.__dict__)
    # print(paginator.__dict__)

    context = {'question_list': page_obj}

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
