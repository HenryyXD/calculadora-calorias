from models import *

def calculate_calories(person: Person):
  if(person.gender == Gender.MALE):
    bmr = 66.5 + (13.75 * person.weightInKg) + (5 * person.heightInCm) - (6.8 * person.age)
  elif(person.gender == Gender.FEMALE):
    bmr = 665 + (9.56 * person.weightInKg) + (1.8 * person.heightInCm) - (4.7 * person.age)
  
  wasted_daily = bmr * PhysicalActivity.get_physical_activity_factor(person.physicalActivity)
  to_consume_daily = wasted_daily + Goal.get_goal_factor(person.goal)
  return wasted_daily, to_consume_daily