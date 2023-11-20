yes_no = input("Do you need help with how long to cook your turkey?")
while yes_no == "Yes":
    print("alright lets get started! ")
    turk_weight = 0
    number_of_turks = int(input("How many turkeys do you have? "))
    for i in range(number_of_turks):
        next = int(input("Enter a turkey weight Or type 0 to skip:"))
        if next == 0:
            print("this turkey was skipped don,t worry if this was a mistake you can always rerun this at the end!")
            continue
        else:

            turk_weight = turk_weight + next * 13
            print("Your turkey needs to cook for " + str(turk_weight) + " minutes")
            turk_weight = 0
    yes_no = input("Do you need anything else?")
    while yes_no == "No":
        print("Have A Happy Thanksgiving!")
        break
        
        






#next = int(input("Enter a turkey weight: "))
#turk_weight = turk_weight + next * 13
#print("Your turkey needs to cook for " + str(turk_weight) + " minutes")4
