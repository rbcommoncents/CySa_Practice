import json
import random


with open("Glossary.json", "r") as json_file:
    quiz_data = json.load(json_file)

def generate_quiz_session(quiz_data, num_questions):
    # Create a list to store the selected questions
    selected_questions = []

    # Loop through the data sets and select questions
    for dataset in quiz_data.values():
        questions = dataset["questions"]
        random.shuffle(questions)  # Shuffle questions within each dataset
        selected_questions.extend(questions)

    # Shuffle all selected questions once to mix them across datasets
    random.shuffle(selected_questions)

    # Select the first `num_questions` questions
    quiz_session = selected_questions[:num_questions]

    return quiz_session

def present_quiz_session(quiz_session):
    # Loop through the quiz session and present questions to the user
    for idx, question in enumerate(quiz_session, start=1):
        question_text = question["question"]
        choices = question["choices"]

        print(f"Question {idx}: {question_text}")
        for choice, option in choices.items():
            print(f"{choice}: {option}")

        user_answer = input("Your answer: ")

        if user_answer.lower() == question["answer"]:
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {question['answer']}\n")

num_questions_in_quiz = 10  # You can set the desired number of questions in each quiz
quiz_session = generate_quiz_session(quiz_data, num_questions_in_quiz)
present_quiz_session(quiz_session)


