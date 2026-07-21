def show_result(username, score, total):

    percentage = (score / total) * 100

    print("\n========== RESULT ==========")

    print("User:", username)

    print("Score:", score, "/", total)

    print("Percentage:", percentage)

    if percentage >= 80:

        print("Excellent Preparation!")

    elif percentage >= 50:

        print("Good, keep practicing!")

    else:

        print("Need more practice!")