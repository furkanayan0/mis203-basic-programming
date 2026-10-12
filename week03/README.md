### Week 03

**AI Tool Used:** Gemini
**Prompt Used:** "Help me write a Python program for a cinema ticket office that calculates prices based on age, day, and student status using loops and conditions, and update my README file for Week 03."
**What did you change?:** I reviewed the conditions and loop structure to ensure it perfectly matches the exact output format and rules requested in the assignment. I also tested the boundary limits.

**Tests:**
1. Input: Age 150 -> Result: "Invalid age." (Boundary test)
2. Input: Age 26, weekday, Student yes -> Result: "200.00 TRY (Standard)" (Tests student age limit)
3. Input: Age 5, weekend, Student no -> Result: "0.00 TRY (Free)" (Tests under 6 boundary)

**Why does the order of the rules matter?:**
The order of the rules matters because the `if/elif` structure executes the very first condition that evaluates to True and skips the rest. If the "Student" rule was placed before the "Child" rule, a 10-year-old student would trigger the 30% student discount instead of getting the 40% child discount, resulting in the customer overpaying.


# Week 3 Lab: Weekly Sales Monitor

**Test Run:**
I tested the program with a daily target of 100. I entered the following values: 50, 120, -20 (the program successfully reprompted), 100, 0, 200, 90, and 150. Exactly seven valid values were counted. The total was 710, the average was 101.43, and 4 days met or exceeded the target (including the day that was exactly 100). The highest sale was correctly recorded as 200 on day 5. I also ran a separate test with seven 0 values, and it correctly output 0 for all metrics.

**Change After Testing:**
During initial testing, I realized I needed a way to track *which* day had the highest sale without using a list for the Stretch Task. I added a `highest_day` integer variable that updates simultaneously with `highest_sale` inside the loop whenever a new maximum is found.
