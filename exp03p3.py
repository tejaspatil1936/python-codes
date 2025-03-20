# Get user input
year = int(input("Enter a year: "))

# Check if it's a leap year
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Check if the year is in the 21st century (2001-2100)
if is_leap:
    if 2001 <= year <= 2100:
        print(f"{year} is a 21st Century Leap Year.")
    else:
        print(f"{year} is a Leap Year.")
else:
    print(f"{year} is NOT a Leap Year.")
