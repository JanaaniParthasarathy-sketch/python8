# Custom Python Module

def greet(name):
    return f"Welcome, {name}!"

def calculate_average(marks):
    return sum(marks) / len(marks)

def find_highest(marks):
    return max(marks)

def find_lowest(marks):
    return min(marks)

def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"
