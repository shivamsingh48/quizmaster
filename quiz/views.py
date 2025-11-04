from django.shortcuts import render, get_object_or_404
from .models import Category, Quiz , Question , Result
from django.contrib.auth.decorators import login_required


def home(request):
    categories = Category.objects.all()
    return render(request, 'quiz/home.html', {'categories': categories})

def quiz_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    quizzes = Quiz.objects.filter(category=category)
    return render(request, 'quiz/quiz_list.html', {'category': category, 'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.question_set.all()  # related questions
    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz, 'questions': questions})

def start_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all()  
    return render(request, 'quiz/start_quiz.html', {'quiz': quiz, 'questions': questions})

@login_required
def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    score = 0
    total = questions.count()

    if request.method == 'POST':
        for question in questions:
            selected_option = request.POST.get(str(question.id))
            if selected_option and selected_option == question.correct_option:
                score += 1

    # ✅ Fix — convert safely to float and round properly
    percentage = 0
    if total > 0:
        percentage = (score / total) * 100
    percentage = round(float(percentage), 2)  # avoid string or decimal issues

    context = {
        'quiz': quiz,
        'score': score,
        'total': total,
        'percentage': percentage,
    }
    return render(request, 'quiz/result.html', context)
