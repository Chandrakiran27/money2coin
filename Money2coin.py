# converting money to coins
given_amount = int(input("Enter the amount given"))
actual_amount = int(input("ENTER THE PURCHASE AMOUNT"))
if actual_amount == given_amount:
    print("Thank you!!, come again")
elif actual_amount > given_amount:
    print("THE PURCHASE AMOUNT IS OF RS", actual_amount, "\n PLEASE GIVE ME AMOUNT OF RS", actual_amount-given_amount, "MORE")
else:
    n = given_amount-actual_amount
    print("the number of coins to be given is: ")
    rupee = [10, 5, 2, 1]
    y = 0
    z = 0
    u = 0
    s = 0
    f = 0
    e = 0
    for x in range(0, n + 1):

        if rupee[0] * x <= n:
            y = rupee[0] * x
    print(rupee[0], "Rs x ", y // rupee[0], "COINS", "=", y)
    if y == n is True:
        print("IN TRUE", y)

    elif y != n:
        a = n - y
        for z in range(0, a + 1):

            if rupee[1] * z <= a:
                s = rupee[1] * z
        print(rupee[1], "RS x", z // rupee[1], "COINS", "=", s)
    if s + y == n is True:
        print("TOTAL=", s + y)

    else:

        d = n - (y + s)
        for e in range(0, d + 1):
            if rupee[2] * e <= d:
                f = rupee[2] * e
        print(rupee[2], "RS x", e // rupee[2], "COINS", "=", f)
    if s + y + f == n is True:
        print("TOTAL=", s + y + f)
    else:
        c = n - (f + s + y)
        for u in range(0, c + 1):
            if rupee[3] * u <= c:
                u = rupee[3] * u
        print(rupee[3], "RS x", u // rupee[3], "COINS", "=", u)
        print("---------")
        print("TOTALLY:", y + s + f + u)
