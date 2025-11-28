import random
print("=== Welcome to Quiz Game ===")

question_list = [
    {
        "question": "Who is the Prime Minister of India?",
        "option1": "A) Narendra Modi",
        "option2": "B) Rahul Gandhi",
        "option3": "C) Amit Shah",
        "option4": "D) Muntsar Khan",
        "correct": "A"
    },

    {
        "question": "Which language is preferred as the national language of India?",
        "option1": "A) Kannada",
        "option2": "B) Sanskrit",
        "option3": "C) Urdu",
        "option4": "D) Hindi",
        "correct": "D"
    },

    {
        "question": "What is the most eaten food in India?",
        "option1": "A) Rice",
        "option2": "B) Rajma",
        "option3": "C) Meat",
        "option4": "D) Dal",
        "correct": "A"
    },

    {
        "question": "What is Nusrat Fateh Ali Khan most known for?",
        "option1": "A) Eating",
        "option2": "B) Dance",
        "option3": "C) Singing",
        "option4": "D) Swimming",
        "correct": "C"
    }
]
while True:
    score = 0

    for q in question_list:

        print("\n" + q["question"])
        print(q["option1"])
        print(q["option2"])
        print(q["option3"])
        print(q["option4"])

        user_ans = input("Enter the (A/B/C/D): ").upper()

        if user_ans == q["correct"]:
            print("yeah! correct answer")
            score += 1
        else:
            print("wrong answer!")

    print("\nYour score:", score, "/", len(question_list))

    again = input("If you want to play again type Y/N: ").upper()

    if again == "Y":
        print("\nGame is restarting!!\n")
       
    else:
        print("Thanks for playing, Goodbye!")
        break
