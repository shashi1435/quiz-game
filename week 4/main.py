from quest import Questions

class Quiz:
    def __init__(self):
        self.questions = Questions.get_questions()
        self.score = 0

    def run_quiz(self):
        question_number = 1
        total_questions = len(self.questions)

        for question_data in self.questions:
            question = question_data[0]
            answer = question_data[1]

            print(f"Question {question_number}: {question}")
            user_answer = input("Enter True or False: ").lower()

            if user_answer == 'true' or user_answer == 'false':
                user_answer = user_answer == 'true'
                if user_answer == answer:
                    self.score += 1
                    print("Correct!")
                else:
                    print("Incorrect!")
            else:
                print("Invalid input. Please enter True or False.")
            
            print(f"Current Score: {self.score}/{question_number}")
            print()
            question_number += 1

        print("Quiz Complete!")
        print(f"Final Score: {self.score}/{total_questions}")


if __name__ == "__main__":
    n=input("Enter Your Name:")
    print(f"Hello!! {n}, Your Quiz has Started!!")
    quiz = Quiz()
    quiz.run_quiz()