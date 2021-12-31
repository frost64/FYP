

def polarity_scaling(pol_review):
    # 0  nutral
    if pol_review == 0:
        return 0
    # greater then 0  positive
    elif pol_review > 0:
        return 1
    else:
        # less then 0  negative
        return -1  
