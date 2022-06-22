# """
#  *****************************************************************************
#    FILE:        marathon.py
#
#    AUTHOR:      {Gabriel Ventura}
#
#    ASSIGNMENT: A marathon calculator to determine if a U.S. participant can
#    run in the Tokyo Marathon. 
#
#    DATE:         {6/22/2022}
#
#    DESCRIPTION: {The code}
#
#  *****************************************************************************

# $1 = 134.28¥
JAPANESE_YEN = 134.28

# 1 mi = 1609.34 meters
METERS_IN_MILE = 1609.34 
JAPANESE_YEN=134.28
# Insert Code Below
def fitness():

  # This ignores our code so that we do not get an error Remove 'pass' when you want to start testing code.
  
  print("Tokyo Marathon Qualifiers")    
  
  #collect user information
  name=input("Please enter your name:")
  miles=float(input("how many miles can you run in 10 minutes?"))
  savings=input("how much u.s$ do you have save for the marathon?")
  savings_index=int(savings[1:])
  lastname=name.find(" ")
  #convert miles to kilometers
  miles_in_kilometer=METERS_IN_MILE/1000
  miles_to_kilometers=miles*miles_in_kilometer
  #print(miles_to_kilometers)
  kilometers_per_min=miles_to_kilometers/10
  #print(kilometers_per_min)
  #us_money_to_yen
  us_money_to_yens=savings_index*JAPANESE_YEN
  print(f"Dear {name[lastname:]}, you have a pace of {kilometers_per_min:.2f} km/min.")
  print(f"Additionally, you only have {us_money_to_yens:.2f}¥ to spend.")
  # python programs
  
if __name__ == "__main__":# This invokes the main function.  It is always included in o
 fitness()