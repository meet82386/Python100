def isLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else: 
                return False
        else:
            return True
    else:
        return False

def countDays(year, month):
    """Returns number of days in respected month of year."""
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month != 2:
        return days[month-1]
    else:
        if isLeap(year):
            return days[1]+1
        else:
            return days[1]

year = int(input("Enter Year: "))
month = int(input("Enter Month: "))

print(f"Days in month is {countDays(year, month)}")