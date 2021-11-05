# String Manipulation

def runStringManipulation():
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