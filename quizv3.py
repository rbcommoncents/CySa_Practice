import requests
import json
import random


# Fetch the JSON data from the URL
url = "https://raw.githubusercontent.com/rbcommoncents/CySa_Practice/main/questions.json"
response = requests.get(url)
data = response.json()



# Shuffle the keys to randomize the order of question sets
shuffled_keys = list(data.keys())
random.shuffle(shuffled_keys)

# Extract quiz data from the JSON
quiz_data = data

def present_quiz_session(quiz_session):
    # Loop through the quiz session and present questions to the user
    for idx, key in enumerate(quiz_session, start=1):
        lesson_data = quiz_data[key]
        lesson = lesson_data["lesson"]
        questions = lesson_data["questions"]

        print(f"Lesson {lesson} - Question {idx}:")
        question = random.choice(questions)

        question_text = question["question"]
        choices = question["options"]

        print(question_text)
        for choice in choices:
            print(choice)

          while True:
            user_answer = input("Your answer: ").strip().lower()

            if user_answer in choices:
                break
            else:
                print("Invalid choice. Please choose a valid option.\n")


        if user_answer.lower() == question["correct_answer"]:
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {question['correct_answer']}\n")

shuffled_keys = list(quiz_data.keys())
random.shuffle(shuffled_keys)
num_questions_in_quiz = 25
quiz_session = shuffled_keys[:num_questions_in_quiz]
present_quiz_session(quiz_session)

