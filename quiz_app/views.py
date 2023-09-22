from django.shortcuts import render, redirect, get_object_or_404
from .models import Question
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def start_quiz(request):
    if request.method == 'POST':
        user = request.user
        user.score = 0
        user.save()
        return redirect('questions', 1)
    return render(request, 'quiz/startQuiz.html')

@login_required
def display_question(request, pk):
    user = request.user
    question = get_object_or_404(Question, id=pk)
    total = Question.objects.count()

    if request.method == 'POST':

        answer_key = f'question_{question.id}'
        user_answer = request.POST.get(answer_key)
        print(user_answer)
        correct_answer = question.answer

        if user_answer == str(correct_answer):
            user.score += 2
        elif user_answer == None:
            pass
        else:
            user.score -= 1

        user.save()
        if question.id != total:
            return redirect('questions', question.id+1)
        else:
            return redirect('final_score')

    return render(request, 'quiz/question_detail.html', {'question': question, 'total': total})


@login_required
def display_score(request):
    user = request.user
    score = user.score

    return render(request, 'quiz/final_score.html', {'score': score})