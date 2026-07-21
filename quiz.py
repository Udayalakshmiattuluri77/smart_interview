# quiz.py

def start_quiz(question_list):

    score = 0

    for index, q in enumerate(question_list, 1):

        print("\nQuestion", index)

        print(q["question"])

        answer = input("Your answer: ")

        if answer.lower() == q["answer"].lower():

            print("Correct Answer")

            score += 1

        else:

            print("Wrong Answer")

            print("Expected:", q["answer"])

    return score