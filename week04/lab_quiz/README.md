# Lab 4: Savings Goal Planner

**Test Run:** 
I tested the program with a starting balance of `1000`, a monthly deposit of `500`, an interest rate of `1%`, and a goal of `3000`. The program successfully stopped at month 4, outputting a final balance of `3070.80` and a total interest of `70.80`.

**Changes After Testing:**
Initially, I forgot to account for cases where the starting balance was already greater than or equal to the goal. After running a test with a starting balance of `5000` and a goal of `3000`, it printed an extra month row. I added an `if balance >= goal:` check right before the loop to fix this and print 0 months correctly.
