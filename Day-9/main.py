# Task-1
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades={}

# # TODO-2: Write your code below to add the grades to student_grades.👇
# for name in student_scores:
#   if(student_scores[name]>90 and student_scores[name]<=100):
#     student_grades[name]="Outstanding"
#   elif(student_scores[name]>80 and student_scores[name]<=90):
#     student_grades[name]="Exceeds Expectations"
#   elif(student_scores[name]>70 and student_scores[name]<=80):
#     student_grades[name]="Acceptable"
#   elif(student_scores[name]<70):
#      student_grades[name]="Fail"
  

# # 🚨 Don't change the code below 👇
# print(student_grades)

#Task-2
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# # TODO: Write the function that will allow new countries
# # to be added to the travel_log. 
# def add_new_country(country,visits,list_of_cities):
#   new_log={}
#   new_log["country"]=country
#   new_log["visits"]=visits
#   new_log["cities"]=list_of_cities
#   travel_log.append(new_log)
# # Do not change the code below 👇
# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")