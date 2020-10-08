while 3>2:
    r_num = int(input("Print your R num - "))
    if r_num >= 95 and r_num <= 100:
        print("Excellent")
    elif r_num >= 85 and r_num < 95:
        print("Very good")
    elif r_num >= 75 and r_num < 85:
        print("Good")
    elif r_num >= 65 and r_num < 75:
        print("Satisfactory")
    elif r_num >= 60 and r_num < 65:
        print("Marginal")
    elif r_num >= 0 and r_num < 60:
        print("Unsatisfactory")
    else:
        print("The number is incorrect")
