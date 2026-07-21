from users import register, login
from questions import get_topics, get_questions
from quiz import start_quiz
from progress import show_result


def main():

    while True:

        print("\n====== Smart Interview Preparation System ======")

        print("""
1. Register
2. Login
3. Exit
""")

        choice = input("Enter choice: ")

        if choice == "1":

            register()

        elif choice == "2":

            user = login()

            if user:

                topics = get_topics()

                print("\nAvailable Topics")

                for i, topic in enumerate(topics, 1):

                    print(i, topic)

                try:

                    selected = int(
                        input("Choose topic: ")
                    )

                    topic_name = topics[
                        selected - 1
                    ]

                    question_list = get_questions(
                        topic_name
                    )

                    print(
                        "\nStarting",
                        topic_name,
                        "Interview"
                    )

                    score = start_quiz(
                        question_list
                    )

                    show_result(
                        user,
                        score,
                        len(question_list)
                    )

                except ValueError:

                    print(
                        "Please enter a number."
                    )

                except IndexError:

                    print(
                        "Please choose a valid topic number."
                    )

        elif choice == "3":

            print("Thank you!")

            break

        else:

            print("Invalid choice")


main()