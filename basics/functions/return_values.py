def sum_weights(beep_weight, boop_weight):
    total_weight = beep_weight + boop_weight
    return total_weight

#
def calc_weights(beep_weight, boop_weight):
    avarage_weight = (beep_weight + boop_weight) /2
    return avarage_weight

def run():
    #retrieve required data
    print("What is the weight of Beep")
    beep_weight = float(input())

    print("What is the weight of Boop?")
    boop_weight = float(input())


    print("Would you like the sum or the avarage")
    answer = input()
    if answer == "sum":
         answer = sum_weights(beep_weight, boop_weight) #variable need to be declared
         print(f"The sum of Beep's and Boop's weight is {answer:.2f}")
    elif answer == "avarage":
        answer = calc_weights(beep_weight, boop_weight)
        print(f"The avarage weight of them is {answer:.2f}")
    else:
        print("I am not sure what is this")

run()
