import json
import os

FILE = "answers.json"

def loadAnswers():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return []


def saveAnswers(answers):
    with open(FILE, "w") as file:
        json.dump(answers, file, indent=4)


def viewAnswers(answers):
    if not answers:
        print("\nNo answers available.\n")
        return

    print("\nYour answers:")
    for i, answer in enumerate(answers, 1):
        parity = "odd" if i % 2 else "even"
        print(f"{i}. [{parity}] {answer['number']}")
    print()


def addition(answers):
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a + b

    print(f"Result: {result}")

    answers.append({"number": result})
    saveAnswers(answers)


def subtraction(answers):
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a - b

    print(f"Result: {result}")

    answers.append({"number": result})
    saveAnswers(answers)


def main():
    answers = loadAnswers()

    actions = {
        "1": lambda: viewAnswers(answers),
        "2": lambda: addition(answers),
        "3": lambda: subtraction(answers),
        "4": exit
    }

    menu = [
        "View Answers",
        "Addition",
        "Subtraction",
        "Exit"
    ]

    while True:
        print("\nOperations")

        for i, item in enumerate(menu, 1):
            print(f"{i}. {item}")

        choice = input("Choose an option: ")

        action = actions.get(choice)

        if action:
            action()
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()