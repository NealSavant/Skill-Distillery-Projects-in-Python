import math

change = [20, 10, 5, 1, .25, .10, .05, .01]
printer_map = {
    20: " Twenty Dollar Bill",
    10: " Ten Dollar Bill",
    5:  " Five Dollar Bill",
    1:  " One Dollar Bill",
    .25: " Quarter",
    .10: " Dime",
    .05: " Nickel",
    .01: " Penny"
}


def make_change(amount_owed: float) -> str:
    result = "Your change is: "
    for i in change:
        if amount_owed - i > 0:
            remainder = int((amount_owed / i).__floor__())
            result = result + f" {remainder}{printer_map[i]}"
            if remainder > 1: 
                result = result + "s,"
            else:
                result = result + ","
            amount_owed = amount_owed - (remainder * i)

    return result

def start():
    not_paid = True
    while(not_paid):
        print("How much does it cost?")
        cost = float(input())
        print("How much will you pay?")
        paid = float(input())
        if paid >= cost:
            not_paid=False

    if math.isclose(paid, cost):
        print("No change")
    else:
        print(make_change(paid - cost))


start()