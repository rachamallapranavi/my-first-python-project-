# Student Marks Calculator - Upgraded by Pranavi
name = input("Enter student name: ")

# Taking 5 subjects
telugu = int(input("Telugu marks: "))
english = int(input("English marks: "))
maths = int(input("Maths marks: "))
science = int(input("Science marks: "))
social = int(input("Social marks: "))

total = telugu + english + maths + science + social
average = total / 5

print(f"\n--- Result for {name} ---")
print(f"Total: {total} / 500")
print(f"Average: {average:.2f}%")

# PASS / FAIL and Grade
if average >= 35:
    print("Result: PASS")
    if average >= 90:
        print("Grade: A+ - Excellent!")
    elif average >= 75:
        print("Grade: A - Great job!")
    elif average >= 60:
        print("Grade: B - Good!")
    else:
        print("Grade: C - Keep trying!")
else:
    print("Result: FAIL - Don't worry, try again!")

print("-------------------------")
