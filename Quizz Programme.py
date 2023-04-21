print("Welcome to Quizz ")
name=input("may i know your name ? ")
playing=input("Do you want play Quizz ? ")
if playing.lower() == "yes":
    print("Welcome " + name)
    print("Your first question is")
    question=input("what is your coding language? ")
    score=0
    if question.lower() == "python":
        print("correct")
        score+=1
    else:
        print("incorrect")
    question = input("Do you have github account? ")
    if question == "yes":
        print("correct")
        score += 1
    else:
        print("incorrect")
    question = input("Are you good at coding? ")
    if question.lower() == "yes":
        print("correct")
        score += 1
    else:
        print("incorrect")

    print("your final is : " + str(score))
    print("your percentage is : " + str((score/3)*100))
    print("Thanks for participating")
else:
    print("get out from here")
