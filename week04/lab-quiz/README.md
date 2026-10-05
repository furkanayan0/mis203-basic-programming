# Week 4 Lab: Weekly Sales Monitor

**Test Run:**
I tested the program with a daily target of 100. I entered the following values: 50, 120, -20 (the program successfully reprompted), 100, 0, 200, 90, and 150. Exactly seven valid values were counted. The total was 710, the average was 101.43, and 4 days met or exceeded the target (including the day that was exactly 100). The highest sale was correctly recorded as 200 on day 5. I also ran a separate test with seven 0 values, and it correctly output 0 for all metrics.

**Change After Testing:**
During initial testing, I realized I needed a way to track *which* day had the highest sale without using a list for the Stretch Task. I added a `highest_day` integer variable that updates simultaneously with `highest_sale` inside the loop whenever a new maximum is found.
