import random

def generate_random_number(difficulty_level):
    if difficulty_level == 'easy':
        return random.randint(1, 9)
    elif difficulty_level == 'medium':
        return random.randint(10, 99)
    elif difficulty_level == 'hard':
        return random.randint(100, 999)

def check_answer(a, b, operation, user_answer):
    if operation == 'addition':
        return a + b == user_answer
    elif operation == 'subtraction':
        return a - b == user_answer
    elif operation == 'multiplication':
        return a * b == user_answer
    elif operation == 'division':
        return round(a / b, 2) == user_answer
def arithmethic_quiz(difficulty_level, operation):
    lives = 3
    score = 0
    while True:
        if lives == 0:
            break
        a = generate_random_number(difficulty_level)
        b = generate_random_number(difficulty_level)
        if operation == 'addition':
            user_answer = int(input(f"{a} + {b} = "))
        elif operation == 'subtraction':
            user_answer = int(input(f"{a} - {b} = "))
        elif operation == 'multiplication':
            user_answer = int(input(f"{a} * {b} = "))
        elif operation == 'division':
            user_answer = float(input(f"{a} / {b} = "))

        if check_answer(a, b, operation, user_answer):
            score += 1
            print("Correct!")
        else:
            lives -= 1
            print("Incorrect!")
    print("Quiz Completed!")
    print("Your score:", score)

if __name__ == "__main__":
    try:
        # pass
        difficulty_level = input("Choose difficulty level (easy/medium/hard): ").lower()
        operation = input("Choose operation (addition/subtraction/multiplication/division): ").lower()

        arithmethic_quiz(difficulty_level, operation)

    except ValueError:
        print("Please enter a valid input.")