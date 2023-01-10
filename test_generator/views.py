from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import random

from test_generator.models import *
# Create your views here.


def available_tests(request):
    tests = Themes.objects.all()
    context = {'available_tests': tests}
    return render(request, 'test_generator/available_tests.html', context)


@login_required
def create_test(request, pk):
    if request.method == 'POST':  # pokud jsme dostali data metodou POST
        th_name_id = pk
        question_count = int(request.POST.get('question_count').strip())
        answer_count = int(request.POST.get('answer_count').strip())

        original_question_count = len(TestQuestions.objects.filter(th_name_id=pk))
        original_answer_count = set(TestQuestions.objects.get('answer_count').filter(th_name_id=pk))

        if len(original_answer_count) == 1:
            orig_answer_count = int(original_answer_count)
        else:
            answer_list = []
            for orig_answer in original_answer_count:
                answer_list.append(int(orig_answer))
            orig_answer_count = min(answer_list)

        if original_question_count >= question_count > 0 and orig_answer_count >= answer_count > 0:
            test = GTest.objects.create(
                question_count=question_count,
                answer_count=answer_count,
                user=request.user,
                th_name_id=th_name_id
            )

            return redirect('generated_test', pk=test.id)

        # pokud místnost nebyla vytvořena
        if question_count == 0:
            context = {'error_message': "I can not create test without questions."}
        if answer_count == 0:
            context = {'error_message': "I can not create test without answers to questions."}
        if question_count == 0 and answer_count == 0:
            context = {'error_message': "I can not create test without questions and answers to them."}
        return render(request, 'tester_services/error_page.html', context)

    else:  # pokud jsme nedostali data pomocí POST, zobrazíme formulář

        return redirect(request, 'test_generator/create_test.html', pk=pk)


def generated_test(request, pk):
    g_test = GTest.objects.get(id=pk)
    answer_count = g_test.answer_count
    question_count = g_test.question_count
    th_name_id = g_test.th_name_id

    original_test_questions = [TestQuestions.objects.get('tq_id').filter(th_name_id=th_name_id)]

    for _ in range(question_count):
        new_question = random.choice(original_test_questions)

        original_test_answers = [TestAnswers.objects.get('id').filter(question_num_id=new_question)]
        for _ in range(answer_count):
            new_answer = random.choice(original_test_answers)

            g_test_answers = GTestAnswers.objects.create(
                gtest_id=pk,
                question_num_id=new_question,
                letter_answer_id=new_answer,
                correct=False,
                done=False,
            )

    questions_g_test = GTestAnswers.objects.get('question_num_id').filter(gtest_id=pk)

    answers_g_test = GTestAnswers.objects.get('letter_answer_id').filter(gtest_id=pk)
    all_answers = []
    set_of_answers = []
    i = 1
    for answer in answers_g_test:
        if i < answer_count:
            set_of_answers.append(answer)
            i += 1
        else:
            set_of_answers.append(answer)
            all_answers.append(set_of_answers)
            i = 1
            set_of_answers = []

    j = 0
    all_questions = []  # all_questions: [0]=q_number; [1]=q_body; [2][0] a_letter; [2][1]=a_body
    part_answers = []
    for question in questions_g_test:
        q_number = question.question_num
        q_body = question.question_body

        for answer in all_answers[j]:
            a_letter = answer.letter_answer
            a_body = answer.body_answer
            part_answers.append([a_letter, a_body])

        all_questions.append([q_number, q_body, part_answers])
        j += 1
        part_answers = []

    context = {'g_test': g_test, 'questions': all_questions}
    return render(request, "test_generator/generated_test", context)
