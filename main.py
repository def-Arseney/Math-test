import random

def generate(a,b):
    num1 = random.randint(a, b)
    num2 = random.randint(a, b)
    operator = random.choice(["/", "*","+","-"])
    return f"{num1} {operator} {num2}"

def check_answer(example,user_input):
    try:
        user_input = float(user_input)
        return user_input == eval(example)
    except:
        return False

def math_quiz(number_of_questions=5):
    print("Добро пожаловать в математический тест!")
    correct_answers = 0

    for i in range(number_of_questions):
        example = generate(1,10)
        user_input = input(f"{example} = ")
        if check_answer(example,user_input):
            correct_answers += 1
    print("тест завершон")
    print(f"вы решили { correct_answers} из {number_of_questions} примеров")
math_quiz()
