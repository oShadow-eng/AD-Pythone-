"""
Day 4 Activity: Parse nested dictionaries (student database).
Tasks:
1) Get Alice's AI301 grade
2) Calculate Bob's GPA (weighted by credits)
3) Find all students in CS101
4) Get average grade across all courses
5) Find student with highest GPA
"""

students = {
    "S001": {
        "name": "Alice Chen",
        "courses": {
            "CS101": {"grade": 92, "credits": 3},
            "MATH201": {"grade": 88, "credits": 4},
            "AI301": {"grade": 95, "credits": 3},
        },
        "advisor": "Dr. Smith",
    },
    "S002": {
        "name": "Bob Lee",
        "courses": {
            "CS101": {"grade": 85, "credits": 3},
            "MATH201": {"grade": 90, "credits": 4},
        },
        "advisor": "Dr. Patel",
    },
}
# Task 1
Alice_cahn = students\
    .get( "S001", {})\
    .get( "courses", {})\
    .get( "AI301", {} )\
    .get( "grade" , 0)
#Task 2
Bob_GPA_CS101_grade = students\
    .get("S002", {})\
    .get("courses", {})\
    .get("CS101", {})\
    .get("grade", 0)
    
Bob_GPA_MATH201_grade = students\
    .get("S002", {})\
    .get("courses", {})\
    .get("MATH201", {})\
    .get("grade", 0)

Bob_GPA_CS101_credits = students\
    .get("S002", {})\
    .get("courses", {})\
    .get("CS101", {})\
    .get("credits", 0)

Bob_GPA_MATH201_credits = students\
    .get("S002", {})\
    .get("courses", {})\
    .get("MATH201", {})\
    .get("credits", 0)

Bob_GPA_grades_CS101 = Bob_GPA_CS101_grade * Bob_GPA_CS101_credits
Bob_GPA_grades_MATH201 = Bob_GPA_MATH201_grade * Bob_GPA_MATH201_credits
Bob_GPA_grades = Bob_GPA_grades_CS101 + Bob_GPA_grades_MATH201
Tutal_credits = Bob_GPA_MATH201_credits + Bob_GPA_CS101_credits
Bob_GPA = Bob_GPA_grades / Tutal_credits
#C
if Bob_GPA >= 70 and Bob_GPA <= 80:
    grade = 3
#B
if Bob_GPA >= 85 and Bob_GPA <= 89:
    grade = 3.5
#A
if Bob_GPA >= 90 and Bob_GPA <= 95:
    grade = 4
#A+
if Bob_GPA >= 96 and Bob_GPA <= 100:
    grade = 5

#Task 3
cs101_students = [
    info["name"]
    for info in students.values()
    if "CS101" in info["courses"]
]

#Task 4
Alice_cahn_AI301 = students\
    .get( "S001", {})\
    .get( "courses", {})\
    .get( "AI301", {} )\
    .get( "grade" , 0)

Alice_cahn_MATH201 = students\
    .get( "S001", {})\
    .get( "courses", {})\
    .get( "MATH201", {} )\
    .get( "grade" , 0)

Alice_cahn_CS101= students\
    .get( "S001", {})\
    .get( "courses", {})\
    .get( "CS101", {} )\
    .get( "grade" , 0)

Bob_CS101_grade = students\
    .get("S002", {})\
    .get("courses", {})\
    .get("CS101", {})\
    .get("grade", 0)

Bob_MATH201_grade = students\
    .get("S002", {})\
    .get("courses", {})\
    .get("MATH201", {})\
    .get("grade", 0)

avrege_grades = sum([Alice_cahn_AI301, Alice_cahn_MATH201, Alice_cahn_CS101, Bob_CS101_grade, Bob_MATH201_grade])/5

#Task 5
Alice_cahn_GPA_grade_AI301 = students\
    .get( "S001", {})\
    .get( "courses", {})\
    .get( "AI301", {} )\
    .get( "grade" , 0)
Alice_cahn_GPA_grade_MATH201 = students\
    .get( "S001", {})\
    .get( "courses", {})\
    .get( "MATH201", {} )\
    .get( "grade" , 0)
Alice_cahn_GPA_grade_CS101= students\
    .get( "S001", {})\
    .get( "courses", {})\
    .get( "CS101", {} )\
    .get( "grade" , 0)\

Alice_cahn_credits_AI301= students\
    .get( "S001", {})\
    .get( "courses", {})\
    .get( "AI301", {} )\
    .get( "credits" , 0)\
    
Alice_cahn_credits_MATH201= students\
    .get( "S001", {})\
    .get( "courses", {})\
    .get( "MATH201", {} )\
    .get( "credits" , 0)\
    
Alice_cahn_credits_CS101= students\
    .get( "S001", {})\
    .get( "courses", {})\
    .get( "CS101", {} )\
    .get( "credits" , 0)\

Alice_cahn_AI301_grades = Alice_cahn_GPA_grade_AI301 * Alice_cahn_credits_AI301
Alice_cahn_MATH201_grades = Alice_cahn_GPA_grade_MATH201 * Alice_cahn_credits_MATH201
Alice_cahn_CS101_grades =  Alice_cahn_GPA_grade_CS101 * Alice_cahn_credits_CS101
Alice_cahn_Tutal_grades = sum([Alice_cahn_AI301_grades, Alice_cahn_MATH201_grades,Alice_cahn_CS101_grades])
Alice_cahn_Tutal_credits = sum([Alice_cahn_credits_AI301, Alice_cahn_credits_MATH201, Alice_cahn_credits_CS101])
Alice_cahn_GPA= Alice_cahn_Tutal_grades / Alice_cahn_Tutal_credits

if Alice_cahn_GPA > Bob_GPA:
    Highest_Student_GPA = "Alice_cahn"
else:
    Highest_Student_GPA = " Bob Lee"

print("Alice_cahn's:", Alice_cahn)
print("grade's:", grade)
print("cs101_students're:", cs101_students)
print("avrege_grades's:", avrege_grades)
print("Highest_Student_GPA's:",Highest_Student_GPA)

#لاعاد تعطونن واحب زي كذا بالله عليكم
# TODO: Implement the tasks above using nested dict access
