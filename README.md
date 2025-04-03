# Movie Ticket Pricing Program

## Overview
This program calculates the ticket price for a movie based on the user's age and the time of the movie. It ensures that input values are valid and applies discounts for morning showtimes.


## Features
- **Age Group Classification**: Categorizes users into `senior`, `adult`, `teenager`, or `child` based on their age.
- **Price Calculation**: Assigns ticket prices based on the age group.
- **Morning Discount**: Reduces ticket price by KES 200 for showtimes before 12:00 PM.
- **Error Handling**: Validates user input to ensure age is greater than 0 and time is in the correct 24-hour format.

---

## Instructions
1. Run the program.
2. Enter your age when prompted.
   - If your age is less than or equal to 0, the program will display an error message and terminate.
3. Enter the movie's start time in 24-hour format (e.g., 1300 for 1:00 PM).
   - If the time is invalid, the program will display an error message and terminate.
4. The program will calculate and display the ticket price based on your age and the time of the movie.

---

## Example Outputs

### Input:
```
Enter your age: 
30
Enter time of movie in 24-hour format (e.g., 1300 for 1:00 PM): 
1000
```

### Output:
```
Discounted ticket price for adult is: 800 KES
```
--
## Notes
- This program assumes valid numeric inputs for age and time.
- Time must be entered in a 24-hour format between 0000 and 2359
