import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question, options, correct_answer):
        print(question)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        user_answer = input("Your answer (enter the corresponding number):- ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
            user_answer = int(user_answer)
            if options[user_answer - 1] == correct_answer:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {correct_answer}\n")
        else:
            print("Invalid input. Please enter a valid number.\n")

    def run_quiz(self):
        for question, options, correct_answer in self.questions:
            self.ask_question(question, options, correct_answer)

        print(f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")

def main():
    # Customize your quiz by modifying questions, options, and correct answers.
    questions = [
        ("Who developed Python Programming Language?", ["Wick van Rossum","Guido van Rossum", "Rasmus Lerdorf", "Niene Stom"], "Guido van Rossum"),
        ("Python supports the creation of anonymous functions at runtime, using a construct called ___________ ?", ["pi", "lambda","anonymous", "none of the mentioned"], "lambda"),
        ("What does pip stand for python?", ["pip Installs Python", "Pip Installs Packages", "Preferred Installer Program", "All of The mention"], "Preferred Installer Program"),
        ("Which of the following is the truncation division operator in Python?",["|","//","/","%"],"//"),
        ("Which of the following function is a built-in function in python?",["factorial()","print()","seed()","sqrt()"],"print()"),
        ("To add a new element to a list we use which python command?",["list1.addEnd(5)","list1.addLast(5)","list1.append(5)","list1.add(5)"],"list1.append(5)"),
        ("Which of these is NOT a fundamental features of OOP?",["Instantiation","Encapsulation","Inheritance","Polymorphism"],"Instantiation"),
        ("Which data structure is used for implementing recursion?",["Stack","Queue","List","Array"],"Stack"),
        ("Which data structure is needed to convert infix notation to postfix notation?",["Stack","Tree","Branch","Queue"],"Stack"),
        ("Which data structure is based on the Last In First Out (LIFO) principle?",["Tree","Linked List","Stack","Queue"],"Stack")

    ]

    # Shuffle the questions to make the quiz more interesting
    random.shuffle(questions)

    # Create and run the quiz
    quiz = Quiz(questions)
    quiz.run_quiz()

if __name__ == "__main__":
    main()
