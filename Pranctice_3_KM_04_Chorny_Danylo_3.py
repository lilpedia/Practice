while 3>2:
    calendar_years = float(input("Input calendar years - "))

    if calendar_years > 0 and calendar_years <= 2:
        print("Dog years - ", calendar_years * 10.5)
    elif calendar_years <= 0:
        print("Error number")
    elif calendar_years > 2:
        answer = (calendar_years - 2) * 4 + 2 * 10.5
        print("Dog years - ", answer)
