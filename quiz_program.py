"""""Users_Focused Program"""
print("##### WELCOME TO THE WORLD OF PROGRAMMING #######")


# Define the questions and their correct answers
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "What is 7 multiplied by 8?", "answer": "56"}
]

# Initialize a variable to keep track of the number of correct answers
correct_answers = 0

# Ask the user each question and check if their answer is correct
for i, question in enumerate(questions, start=1):
    user_answer = input(f"Question {i}: {question['question']} ").strip()
    
    if user_answer.lower() == question["answer"].lower():
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Wrong! The correct answer is: {question['answer']}")

# Display the number of correct answers
print(f"You answered {correct_answers} out of {len(questions)} questions correctly.")

      
   



