"""
Ben Phan
CSC 110
Project-1
This program has the function of calculating the area of different geometry shapes. 
"""

def rectangle_area(base,height):
  """
  This function returns the area of a rectangle.
  Args:
    base: base of a rectangle.
    height: height of a rectangle.
  Returns:
    The area of a rectangle.
  """
  return base * height
  
def triangle_area (a,b,c):
   """
  This function returns the area of a triangle.
  Args:
    a: first side of a triangle.
    b: second side of a triangle.
    c: third side of a triangle. 
  Returns:
    The area of a triangle.
  """
   s=(a+b+c)/2 #s is semiparameter of a triangle. 
   area= (s*(s-a)*(s-b)*(s-c))**0.5 
   return area

def trapezoid_area (base_1,base_2,height):
   """
  This function returns the area of a trapezoid.
  Args:
    base_1:first base of a trapezoid.
    base_2:second base of a trapezoid.
    height: height of a trapezoid.
  Returns:
    The area of a trapeozid.
  """
   return 0.5*(base_1+base_2)*height

def circle_area (radius):
   """
  This function returns the area of a circle.
  Args:
    radius: radius of a circle. 
  Returns:
    The area of a circle.
  """
   return round(3.1415*radius**2,2)

