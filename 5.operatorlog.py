has_high_incone = True
has_good_credit = True

if has_high_incone and has_good_credit:
    print('eligible for loan')

has_high_incone = False

if has_high_incone or has_good_credit:
    print('eligible for loan')