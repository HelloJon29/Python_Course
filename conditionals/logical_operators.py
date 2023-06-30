has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income or has_good_credit: #in Python AND/OR operators are written plainly
    print('Eligible for loan')
# for and, both conditions must be true
# for or, at least one condition must be true

if has_good_credit and not has_criminal_record: # NOT operator flips the value of the boolean, True -> False, False -> True
    print('Eligible for loan 2')