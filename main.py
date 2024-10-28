def total_calc(bill_amount,tip perc):
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total,2)
    print(f"pleasea pay ${total}")
total_calc(150,20)