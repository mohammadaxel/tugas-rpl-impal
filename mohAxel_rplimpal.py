computer_amount = int(input("How many of your computer that you want to service? "))
peripheral_amount = int(input("How many of your peripheral devices that you want to service? ")) 
service_time = str(input("In business hour?(yes/no) "))
drop_off = str(input("Willing to drop off and pick up yourself?(yes/no) "))
if computer_amount == 1 or computer_amount == 2:
    base_fee = 50
    additional_fee = 0 * peripheral_amount

elif computer_amount > 2 and computer_amount <= 10:
    base_fee = 100
    additional_fee = 10 * peripheral_amount

elif computer_amount > 10:
    base_fee = 500
    additional_fee = 10 * peripheral_amount

if service_time == "no" or service_time == "No" or service_time == "n" or service_time == "N" or service_time == "Not" or service_time == "not":
    base_fee = base_fee * 2

if drop_off == "yes" or drop_off == "Yes" or drop_off == "y" or drop_off == "Y":
    base_fee = base_fee / 2

total_fee = base_fee + additional_fee
print("Your total fee is $" + str(total_fee))