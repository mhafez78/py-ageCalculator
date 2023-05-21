
# Python3 code to  calculate age in years
from datetime import date
 
def calculateAge(born):
    today = date.today()
    try:
        birthday = born.replace(year = today.year)
 
    # raised when birth date is February 29
    # and the current year is not a leap year
    except ValueError:
        birthday = born.replace(year = today.year,
                  month = born.month + 1, day = 1)
 
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year
         
# Driver code
euyy = input('Year of Birth (xxxx): ')
euyy = int(euyy)
eumm= input('Enter Month of Birth (xx): ')
eumm = int(eumm)
eudd = input("Enter Day of Birth (xx): ")
eudd = int(eudd)

print("You are ", calculateAge(date(euyy, eumm, eudd)), "years")

def canBuyCigsOrAlcohol():
    eu_age = calculateAge(date(euyy, eumm, eudd))
    if eu_age > 18:
        answer = 'Your customer can buy cigs'
    if eu_age > 21:
        answer = 'Your customer can buy cigs and alcohol'
    else: answer = "Your customer is under age cannot buy either cigs nor alcohol"    
    return answer

print(canBuyCigsOrAlcohol())



    