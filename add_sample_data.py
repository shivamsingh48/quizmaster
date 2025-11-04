#!/usr/bin/env python
"""
Sample data script for QuizMaster
Run this to add sample categories, quizzes, and questions for testing
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizmaster.settings')
django.setup()

from quiz.models import Category, Quiz, Question

def add_sample_data():
    # Create categories
    categories_data = [
        {'name': 'Python Programming', 'slug': 'python-programming'},
        {'name': 'Web Development', 'slug': 'web-development'},
        {'name': 'Data Science', 'slug': 'data-science'},
        {'name': 'General Knowledge', 'slug': 'general-knowledge'},
    ]
    
    categories = {}
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults={'name': cat_data['name']}
        )
        categories[cat_data['slug']] = category
        if created:
            print(f"Created category: {category.name}")
    
    # Create quizzes
    quizzes_data = [
        {
            'title': 'Python Basics',
            'category': 'python-programming',
            'total_time': 300,  # 5 minutes
            'questions': [
                {
                    'text': 'What is the correct way to create a list in Python?',
                    'option1': 'list = []',
                    'option2': 'list = ()',
                    'option3': 'list = {}',
                    'option4': 'list = ""',
                    'correct_option': '1'
                },
                {
                    'text': 'Which of the following is used to define a function in Python?',
                    'option1': 'function',
                    'option2': 'def',
                    'option3': 'func',
                    'option4': 'define',
                    'correct_option': '2'
                },
                {
                    'text': 'What does the len() function do?',
                    'option1': 'Returns the length of an object',
                    'option2': 'Creates a new list',
                    'option3': 'Converts to string',
                    'option4': 'Sorts a list',
                    'correct_option': '1'
                }
            ]
        },
        {
            'title': 'HTML & CSS Fundamentals',
            'category': 'web-development',
            'total_time': 420,  # 7 minutes
            'questions': [
                {
                    'text': 'What does HTML stand for?',
                    'option1': 'Hyper Text Markup Language',
                    'option2': 'High Tech Modern Language',
                    'option3': 'Home Tool Markup Language',
                    'option4': 'Hyperlink and Text Markup Language',
                    'correct_option': '1'
                },
                {
                    'text': 'Which CSS property is used to change the text color?',
                    'option1': 'font-color',
                    'option2': 'text-color',
                    'option3': 'color',
                    'option4': 'foreground-color',
                    'correct_option': '3'
                },
                {
                    'text': 'What is the correct HTML element for the largest heading?',
                    'option1': '<heading>',
                    'option2': '<h1>',
                    'option3': '<h6>',
                    'option4': '<head>',
                    'correct_option': '2'
                },
                {
                    'text': 'How do you create a comment in CSS?',
                    'option1': '// This is a comment',
                    'option2': '<!-- This is a comment -->',
                    'option3': '/* This is a comment */',
                    'option4': '# This is a comment',
                    'correct_option': '3'
                }
            ]
        },
        {
            'title': 'Data Science Basics',
            'category': 'data-science',
            'total_time': 600,  # 10 minutes
            'questions': [
                {
                    'text': 'Which Python library is most commonly used for data manipulation?',
                    'option1': 'NumPy',
                    'option2': 'Pandas',
                    'option3': 'Matplotlib',
                    'option4': 'Scikit-learn',
                    'correct_option': '2'
                },
                {
                    'text': 'What does SQL stand for?',
                    'option1': 'Structured Query Language',
                    'option2': 'Simple Query Language',
                    'option3': 'Standard Query Language',
                    'option4': 'Sequential Query Language',
                    'correct_option': '1'
                }
            ]
        },
        {
            'title': 'Quick General Knowledge',
            'category': 'general-knowledge',
            'total_time': 180,  # 3 minutes
            'questions': [
                {
                    'text': 'What is the capital of France?',
                    'option1': 'London',
                    'option2': 'Berlin',
                    'option3': 'Paris',
                    'option4': 'Madrid',
                    'correct_option': '3'
                },
                {
                    'text': 'Which planet is known as the Red Planet?',
                    'option1': 'Venus',
                    'option2': 'Mars',
                    'option3': 'Jupiter',
                    'option4': 'Saturn',
                    'correct_option': '2'
                },
                {
                    'text': 'Who painted the Mona Lisa?',
                    'option1': 'Vincent van Gogh',
                    'option2': 'Pablo Picasso',
                    'option3': 'Leonardo da Vinci',
                    'option4': 'Michelangelo',
                    'correct_option': '3'
                }
            ]
        }
    ]
    
    for quiz_data in quizzes_data:
        category = categories[quiz_data['category']]
        quiz, created = Quiz.objects.get_or_create(
            title=quiz_data['title'],
            category=category,
            defaults={'total_time': quiz_data['total_time']}
        )
        
        if created:
            print(f"Created quiz: {quiz.title}")
            
            # Add questions
            for q_data in quiz_data['questions']:
                question = Question.objects.create(
                    quiz=quiz,
                    text=q_data['text'],
                    option1=q_data['option1'],
                    option2=q_data['option2'],
                    option3=q_data['option3'],
                    option4=q_data['option4'],
                    correct_option=q_data['correct_option']
                )
                print(f"  Added question: {question.text[:50]}...")
    
    print("\n✅ Sample data added successfully!")
    print("You can now:")
    print("1. Visit http://127.0.0.1:8000 to see the quiz platform")
    print("2. Create an account to take quizzes")
    print("3. Access admin panel at http://127.0.0.1:8000/admin/ to manage content")

if __name__ == '__main__':
    add_sample_data()
