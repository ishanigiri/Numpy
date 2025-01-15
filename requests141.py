import requests
#trivia API URL
url = "https://opentdb.com/api.php?amount=5&type=multiple"
#fetch trivia questions
response = requests.get(url)
# check if the request was successful
if response.status_code == 200:
    print("Trivia questions fetched successfully!\n")
    #parse the JSON data
    trivia_data = response.json()
    #Function to display question and get user answers
    def ask_question(question, options, correct_answer):
        print(f"Question:{question}")
        print("Options:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        answer = input("Your answer (1/2/3/4):")
        if options[int(answer)-1] == correct_answer:
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is: {correct_answer}\n")
    # Ask each question
    for trivia in trivia_data["results"]:
        question = trivia["question"]
        options = trivia["incorrect_answers"] + [trivia["correct_answer"]]
        # shuffle the options randomly
        from random import shuffle
        shuffle(options)
        correct_answer = trivia["correct_answer"]
        ask_question(question, options, correct_answer)
else:
    print(f"Failed to retrieve trivia data. Status Code: {response.status_code}")
