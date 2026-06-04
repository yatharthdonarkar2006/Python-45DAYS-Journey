# Online Shopping Discount

purchase = int(input("Enter Purchase Amount: "))
coupon = input("Do you have a Coupon? (Y/N): ").upper()
prime_member = input("Are you a Prime Member? (Y/N): ").upper()

if purchase > 10000:

    if prime_member == "Y":

        if coupon == "Y":
            discount = purchase * 30 / 100

        elif coupon == "N":
            discount = purchase * 20 / 100

        else:
            print("Invalid Coupon Input (Y/N)")
            exit()

    elif prime_member == "N":

        if coupon == "Y":
            discount = purchase * 15 / 100

        elif coupon == "N":
            discount = purchase * 10 / 100

        else:
            print("Invalid Coupon Input (Y/N)")
            exit()

    else:
        print("Invalid Prime Member Input (Y/N)")
        exit()

else:

    if prime_member == "Y":
        discount = purchase * 5 / 100

    elif prime_member == "N":
        discount = 0

    else:
        print("Invalid Prime Member Input (Y/N)")
        exit()

final_price = purchase - discount

print("\nDiscount Amount:", discount)
print("Final Price:", final_price)