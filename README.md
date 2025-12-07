Question 1 from my college assignment. (Since I'm Brazilian, some parts of my code are in Brazilian Portuguese, but that's only a requirement of the assignment.)

Statement:
Imagine you are one of the programmers responsible for building an app for company X that sells health insurance plans. One of company X's strategies is to charge a different price based on the client's age, as listed below:

If the age is greater than or equal to 0 and less than 19, the price will be 100% of the base price of the plan (100 / 100);

If the age is greater than or equal to 19 and less than 29, the price will be 150% of the base price of the plan (150 / 100);

If the age is greater than or equal to 29 and less than 39, the price will be 225% of the base price of the plan (225 / 100);

If the age is greater than or equal to 39 and less than 49, the price will be 240% of the base price of the plan (240 / 100); If the age is greater than or equal to 49 and less than 59, the value will be 350% of the plan's base value (350 / 100);

If the age is greater than or equal to 59, the value will be 600% of the plan's base value (600 / 100);

The monthly plan value is calculated as follows:

monthlyValue = baseValue * percentage

Example: If the baseValue is 100.00 and the age is 45 years (240% according to the table above)
monthlyValue = 100.00 * 240 / 100 = R$ 240.00

Develop a Python program that:
Implements a print statement with a welcome message displaying your first and last name (print only, do not use input here). [CODE REQUIREMENT 1 of 6];

The plan's base value and the client's age must be implemented [CODE REQUIREMENT 2 of 6];
The value rules must be implemented as stated above (note: pay attention to the less than, equal to, and greater than conditions) [CODE REQUIREMENT 3 of 6];
The monthly value must be implemented [CODE REQUIREMENT 4 of 6];
The if, elif, and else structures (all of them) must be implemented [CODE REQUIREMENT 5 of 6];
Relevant comments must be inserted in the code [CODE REQUIREMENT 6 of 6];
