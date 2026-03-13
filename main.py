# Create a function that will add two number using user input
def addNumbers(a, b):
    return a + b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter first number: "))

results = addNumbers(num1, num2)
print(results)


# Create a function that adds multiple numbers from a list
def addNumbersList(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

nums = [23, 42, 55 , 43]
print("The sum is:", addNumbersList(nums))
 
    
# Global keyword
x = "Leester"

def myName():
    global x
    x = "Cruspero"
    print("My name: " + x)
    
myName()
print("My name: " + x)    

#This way you only edit one list, not multiple prints.
menu = [
    "View Tasks",
    "Add Task",
    "Complete Task",
    "Delete Task",
    "Exit"
]

print("Task Manager")
for i, item in enumerate(menu, 1):
    print(f"{i}. {item}")


text = "algorithm"
print(text[3:7])

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

print(fruits)

print("banan" in fruits)
print("banan" not in fruits)

