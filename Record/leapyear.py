print("leap years from current year to end year")
start = int(input("Enter current year: "))
end = int(input("Enter final year: "))

for year in range(start, end + 1):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year)
          
