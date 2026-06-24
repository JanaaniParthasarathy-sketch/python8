import pandas as pd
import mymodule

print("=" * 50)
print("STUDENT PERFORMANCE ANALYSIS SYSTEM")
print("=" * 50)

student_name = "Janaani"

marks = [95, 88, 91, 97, 89]

print(mymodule.greet(student_name))

average = mymodule.calculate_average(marks)
highest = mymodule.find_highest(marks)
lowest = mymodule.find_lowest(marks)
student_grade = mymodule.grade(average)

print("\nStudent Report")
print("-" * 30)
print("Marks:", marks)
print("Average Marks:", round(average, 2))
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Grade:", student_grade)

# Third-party package example using Pandas
data = {
    "Subject": ["Maths", "Physics", "Chemistry", "Biology", "English"],
    "Marks": marks
}

df = pd.DataFrame(data)

print("\nSubject-wise Marks")
print(df)

# Save data to CSV
df.to_csv("student_data.csv", index=False)

print("\nData saved successfully to student_data.csv")

print("\nProgram Completed Successfully!")
