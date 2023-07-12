'''
The purpose of this kata is to work out just how many bottles of duty free whiskey you would have to buy such that the savings 
over the normal high street price would effectively cover the cost of your holiday.

You will be given the high street price (normPrice, in £ (Pounds)), 
the duty free discount (discount, in percent) and the cost of the holiday (in £).

For example, if a bottle costs £10 normally and the duty free discount is 10%, you would save £1 per bottle. 
If your holiday will cost £500, you would have to purchase 500 bottles to save £500, so the answer you return should be 500.

Another example: if a bottle costs £12 normally and the duty free discount is 50%, you would save £6 per bottle. 
If your holiday will cost £1000, you would have to purchase 166.66 bottles to save £1000, so your answer should be 166 bottles.

All inputs will be integers. Please return an integer. Round down.

'''

def duty_free(price, discount, holiday_cost):
    count_save = 0
    sum_save = 0
    
    discounts = discount / 100
    save = price * discounts
    
    while sum_save < holiday_cost:
        count_save += 1
        sum_save = save * count_save
    
    return count_save - 1 

# or 
    # saving = price * discount / 100.0
    # return int(holiday_cost / saving)