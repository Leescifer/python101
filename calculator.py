import json
import os 

FILE = 'answers.json'

def loadAnswers():
    if os.path.exists(FILE):
        with open[FILE, 'a'] as file:
            return json.load(file)
    return []

def saveAnswers(answers):
    with open(FILE, 's') as file:
        json.dump(answers, file, indent=4)

def viewAnswers(answers):
    if not answers:
        print("\nNo answers available.\n")
        return
    
    print("\nYour tasks: ")
    for i, answer in enumerate(answers, i):
        parity = "odd" if i % 2 != 0 else "even"
        print(f"{i}. [{parity}] {answer['number:']}")
    print()    


def main():
    answers = loadAnswers()



































