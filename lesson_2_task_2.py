def is_year_leap (year):
    if year % 4 == 0:
        return True
    else:
        return False

year = int(input("Введите год: "))
result = is_year_leap(year)
print("год " + str(year) + ": " + str(result))