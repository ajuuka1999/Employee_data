# Employee_data
Create a class Employee, and create and test a function to compute net pay from payment, work and tax credit information.

Employee should have the following attributes:
StaffID, LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand,

For Example:

jg= Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)

Create a method computePayment in class Employee which takes HoursWorked and date as input, and returns a payment information dictionary as follows: (if jg is an Employee object for worker Joe Green)

We will assume a standard rate of 20% and a higher rate of 40%, and that PRSI at 4% is not subject to allowances. (we will ignore USC etc.)

>>>jg.computePayment(42, '31/10/2021')
