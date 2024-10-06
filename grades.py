"""
Ben Phan
CSC 110
Project-2
This program has a function that calculates grades of students. 
"""

def letter_grade(grade):
  """
This function returns the letter grade of students.
Args:
  grade: numerical grade of students.
Returns:
  The letter grade of students. 
"""
  if float(grade) >= 90 and float(grade) <= 100:
    return "A"
  if float(grade) >= 80 and float(grade) < 90:
    return "B"
  if float(grade) >= 70 and float(grade) < 80:
    return "C"
  if float(grade) >= 60 and float(grade) < 70:
    return "D"
  if float(grade) < 60 and float(grade) >= 0:
    return "E"
  if float(grade) < 0 or float(grade) > 100:
    return "X"


def pass_or_fail(letter_grade):
  """
This function returns the grade outcome of students.
Args:
  letter_grade: letter grade of students.
Returns:
  The grade outcome of students. 
"""
  character=len(letter_grade)
  if character>1:
    return "Error"
  if letter_grade == "A" or letter_grade == "B" or letter_grade == "C" or letter_grade == "D":
    return "Pass"
  else:
    return "Fail"


def point_grade(score, total_points):
  """
This function returns the point grade of students.
Args:
 score: numerical grade students score.
 total_points: total numerical grade.
Returns:
  The point grade of students. 
  """
  percentage = float(round((score / total_points) * 100, 2))
  return percentage


def get_grade_results(score, total_points):
  """
This function returns the final results of students.
Args:
  score: numerical grade students score.
 total_points: total numerical grade.
Returns:
  The point grade of students, the letter grade of students, and whether or not if the students pass or fail.  
"""
  grade = point_grade(score, total_points)
  score = letter_grade(grade)
  end= pass_or_fail(score)
  return "Your grade is" +" "+ str(grade)+ " "+"("+str(score)+" "+"-"+ " "+str(end)+")"

def main():
  print(get_grade_results(59.9,100))

main()
  