# Price of house is $1M
# if buyer has good credit, put down 10%
# otherwise put down %20
# print the down payment

good_credit = False
home_price = 1_000_000
down_payment = 0

if good_credit:
    down_payment = home_price * .10
else:
    down_payment = home_price * .20
print(f"Down payment {down_payment}")