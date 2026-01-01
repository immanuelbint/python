# declare variable
name = "" # insert name here
age = 60

def age_classification(age):
  if age in range(1, 5):
    return "Toddler"
  elif age in range(7, 10):
    return "Children"
  elif age in range(11, 17):
    return "Teenager"
  elif age in range(18, 59):
    return "Adult"
  else:
    return "Elderly"

# Output
print(f"{name} you're {age_classification(age)}" )
