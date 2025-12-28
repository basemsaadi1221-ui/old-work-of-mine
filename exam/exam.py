import random



dict = {
    "question1": {                                      # key
        "question": "what is the capital of france ?",  # value
        "answer": "paris"                               # value
    },
    "question2": {                                      # key
        "question": "what is the capital of germany ?", # value
        "answer": "berlin"                              # value    
    },
    "question3": {                                      # key        
        "question": "what is the capital of italy ?",   # value
        "answer": "rome"                                # value                                 
    },
    "question4": {                                      # key
        "question": "what is the capital of spain ?",   # value
        "answer": "madrid"                              # value
    },
    "question5": {                                      # key
        "question": "what is the capital of portugal ?",# value
        "answer": "lisbon"                              # value
    }
}


score = 0
question_list = list(dict.items())                        # Convert dict.items() to a list and shuffle it
random.shuffle(question_list)                             # This randomizes the order


for key, value in question_list:                            # looping thro question_list not dect.items()
    print(value["question"])                                # value for just the question
    user_answer = input("enter your answer : ").lower()     # now the user answer
    if user_answer == value["answer"].lower():              # if the answer is equal + 1 to score
        print("correct\n")
        score += 1
        print(f"your score is {score}\n")
    elif user_answer == "quit":
        print("Goodbye!")
        break
    else:
        print("incorrect\n")
        print(f"the correct answer is {value['answer']}")
        score -= 1
        print(f"your score is {score}\n")

print(f"your final score is {score}")