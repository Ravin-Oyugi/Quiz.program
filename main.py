quiz = {
    "question1": {
        "question": "What is the capital of Kenya",
        "answer": "Nairobi"
    },
    "question2": {
        "question": "What is the capital of Uganda",
        "answer": "Kampala"
    },
    "question3": {
        "question": "What is the capital of Tanzania",
        "answer": "Dar es salaam"
    },
    "question4": {
        "question": "What is the capital of Nigeria",
        "answer": "Abuja"
    },
    "question5": {
        "question": "What is the capital of Somalia",
        "answer": "Mogadishu"
    },
    "question6": {
        "question": "What is the capital of Ghana",
        "answer": "Accra"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer?")

    if answer.lower() == value['answer'].lower():
      print('Correct')
      score = score + 1
      print("Your score is: "+ str(score))
      print("")
      print("")

    else:
        print("Wrong!")
        print("The answer is: "+ value['answer'])
        print("Your score is: "+str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 6 questions correctly")
print("Your percentage is " + str(int(score/6 * 100)) + "%")
