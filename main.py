#Author: Dominic Savaglio djs7129@psu.edu
def getGradePoint(grade):
  if grade == "A":
    return 4.0
  elif grade == "A-":
    return 3.67
  elif grade == "B+":
    return 3.33
  elif grade == "B":
    return 3.0
  elif grade == "B-":
    return 2.67
  elif grade == "C+":
    return 2.33
  elif grade == "C":
    return 2.0
  elif grade == "D":
    return 1.0
  else:
    return 0.0
def run():
  grade = (input("Enter your course 1 letter grade: "))
  grade_one = getGradePoint(grade)
  credit_one = float((input("Enter your course 1 credit: ")))
  print(f"Grade point for course 1 is: {grade_one}")
  grade = (input("Enter your course 2 letter grade: "))
  grade_two = getGradePoint(grade)
  credit_two = float((input("Enter your course 2 credit: ")))
  print(f"Grade point for course 2 is: {grade_two}")
  grade = (input("Enter your course 3 letter grade: "))
  grade_three = getGradePoint(grade)
  credit_three = float((input("Enter your course 3 credit: ")))
  print(f"Grade point for course 3 is: {grade_three}")
  GPA = ((grade_one * credit_one + grade_two * credit_two + grade_three * credit_three)/(credit_one + credit_two + credit_three))
  print(f"Your GPA is: {GPA}")
if __name__ == "__main__":
  run()


