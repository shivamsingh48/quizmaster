from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Category, Quiz, Question, Result
from .forms import SignUpForm, UserProfileForm


def home(request):
    categories = Category.objects.all()
    return render(request, 'quiz/home.html', {'categories': categories})

def quiz_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    quizzes = Quiz.objects.filter(category=category)
    return render(request, 'quiz/quiz_list.html', {'category': category, 'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz, 'questions': questions})

@login_required
def start_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    return render(request, 'quiz/start_quiz.html', {'quiz': quiz, 'questions': questions})

@login_required
def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    score = 0
    total = questions.count()
    user_answers = {}
    correct_answers = {}

    if request.method == 'POST':
        for question in questions:
            selected_option = request.POST.get(str(question.id))
            user_answers[question.id] = selected_option
            correct_answers[question.id] = question.correct_option
            
            if selected_option and selected_option == question.correct_option:
                score += 1

        # Save result to database
        Result.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            max_score=total
        )

    percentage = round((score / total) * 100, 2) if total > 0 else 0

    context = {
        'quiz': quiz,
        'questions': questions,
        'score': score,
        'total': total,
        'percentage': percentage,
        'user_answers': user_answers,
        'correct_answers': correct_answers,
    }
    return render(request, 'quiz/result.html', context)

# Authentication Views
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    # Get user's quiz history
    user_results = Result.objects.filter(user=request.user).order_by('-taken_at')
    
    context = {
        'form': form,
        'user_results': user_results
    }
    return render(request, 'quiz/profile.html', context)

@login_required
def dashboard_view(request):
    user_results = Result.objects.filter(user=request.user).order_by('-taken_at')[:10]
    total_quizzes = user_results.count()
    
    if total_quizzes > 0:
        avg_score = sum(result.score / result.max_score for result in user_results) / total_quizzes * 100
        avg_score = round(avg_score, 2)
    else:
        avg_score = 0
    
    context = {
        'user_results': user_results,
        'total_quizzes': total_quizzes,
        'avg_score': avg_score,
    }
    return render(request, 'quiz/dashboard.html', context)
