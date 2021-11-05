# Printing Hello World

msg = "Hello, World"
print(msg.upper())

# Declaring Variable

age = 23
full_name = "Armando I. Bibay Jr"
price = 29.40

print(f"I am {full_name} and I am {age} years old")

# Receiving input from user

name = input("What is your name? ")
print("The name is " + name)

# Type Conversion i.e. int(), float(), bool(), str()

birth_year = input("What is your birth year?" )
age = 2021 - int(birth_year)
print(f"The age is {age}")

# Adding Two Numbers

first_number =  float(input("Enter first Number: "))
second_number = float(input("Enter Second Number: "))
sum= first_number + second_number
print(f"The sum of two numbers is {sum}")


# String Manipulation

course = "Python Course For Beginners"
course_in_lowercase = course.lower()
course_in_uppercase = course.upper()
course_replaced_with_lesson = course.replace('Course', "Lesson")
is_the_word_Python_existing_in_the_course = "Python" in course #returns a boolean

print(f"The course is called: {course}")
print(f"The course in lowercase: {course_in_lowercase}")
print(f"The course in uppercase: {course_in_uppercase}")
print(f"The word course replaced with {course_replaced_with_lesson}")
print(f"The course has the word Python in it: {is_the_word_Python_existing_in_the_course}")