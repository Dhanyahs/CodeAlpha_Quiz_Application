class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def get_question(self):
        if self.question_index < len(self.questions):
            return self.questions[self.question_index]
        else:
            return None

    def display_question(self, question):
        print(question.text)
        for i, choice in enumerate(question.choices, start=1):
            print(f"{i}. {choice}")
        print()

    def take_quiz(self):
        for question in self.questions:
            self.display_question(question)
            user_answer = input("Enter the number of your answer: ")
            if question.check_answer(user_answer):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong. The correct answer was: {question.answer}\n")
            self.question_index += 1
        print(f"Your score: {self.score}/{len(self.questions)}")


# Sample questions
questions = [
    Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
    Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Earth"], "Mars"),
    Question("What is the largest mammal in the world?", ["Elephant", "Giraffe", "Blue Whale", "Kangaroo"], "Blue Whale"),
]

# Create and run the quiz
quiz = Quiz(questions)
quiz.take_quiz()
