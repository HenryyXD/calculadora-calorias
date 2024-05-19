from enum import Enum

class Gender(Enum):
  MALE = "male"
  FEMALE = "female"

class Goal(Enum):
  LOSE_WEIGHT = "lose_weight"
  MAINTAIN_WEIGHT = "maintain_weight"
  GAIN_WEIGHT = "gain_weight"
  
  def get_goal_factor(goal):
    switcher = {
      Goal.LOSE_WEIGHT: -500,
      Goal.MAINTAIN_WEIGHT: 0,
      Goal.GAIN_WEIGHT: 500
    }
    
    return switcher.get(goal, 0)

class PhysicalActivity(Enum):
  SEDENTARY = "sedentary"
  LIGHT = "light"
  MODERATE = "moderate"
  ACTIVE = "active"
  VERY_ACTIVE = "very_active"

  def get_physical_activity_factor(physicalActivity):
    switcher = {
      PhysicalActivity.SEDENTARY: 1.2,
      PhysicalActivity.LIGHT: 1.375,
      PhysicalActivity.MODERATE: 1.55,
      PhysicalActivity.ACTIVE: 1.725,
      PhysicalActivity.VERY_ACTIVE: 1.9
    }

    return switcher.get(physicalActivity, 1.0)

class Person:
  def __init__(self, goal, gender, age, weightInKg, heightInCm, physicalActivity):
    self.goal = goal
    self.gender = gender
    self.age = age
    self.weightInKg = weightInKg
    self.heightInCm = heightInCm
    self.physicalActivity = physicalActivity
