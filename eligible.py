def validate_age(age):
  if age.isnumeric()==True:
    age=int(age)
    if 0<=age<=110:
      return True
  return False
    
def check_eligibility (age):
  if age >= 18:
    return True
  else:
    return False
    