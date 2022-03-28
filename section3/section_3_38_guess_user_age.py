
#Section 3, video 38: exercise asks you to find a user's age based on their date of birth input. 
#This was my code, may not be the same as shown in exercise

from datetime import date

date_of_birth = input( "what year were you born?")
todays_date = date.today()
current_year = todays_date.year
user_age = (current_year - int(date_of_birth))
print("your age is " + str(user_age))