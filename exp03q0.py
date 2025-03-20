# Get user input
salary = int(input("Enter the employee's salary: "))
experience = int(input("Enter the employee's years of experience: "))
performance_rating = float(input("Enter the employee's performance rating (1 to 5): "))

# Initialize bonus percentage
bonus_percentage = 0

# Check performance rating condition first
if performance_rating < 3:
    print("Employee is not eligible for a bonus due to low performance rating.")
    bonus = 0  # No bonus if performance is below 3
else:
    # Determine bonus percentage based on experience
    if experience > 10:
        bonus_percentage = 20
    if 5 <= experience <= 10:
        bonus_percentage = 10
    if experience < 5:
        bonus_percentage = 5

    # Calculate bonus
    bonus = (bonus_percentage / 100) * salary
    print(f"Bonus Amount: {bonus}")

# Final salary calculation
final_salary = salary + bonus
print(f"Final Salary after Bonus: {final_salary}")
