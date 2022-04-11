class Employee:
    def __init__(self,StaffID,LastName,FirstName,RegHours,HourlyRate,OTMultiple,TaxCredit,StandardBand):
        self.StaffID = StaffID
        self.LastName = LastName
        self.FirstName = FirstName
        self.RegHours = RegHours
        self.HourlyRate = HourlyRate
        self.OTMultiple = OTMultiple
        self.TaxCredit = TaxCredit
        self.StandardBand = StandardBand

    def computePayment(self,hours,date):
        overtime = 0
        dict1 = dict()
        regular = hours

        if hours > self.RegHours:
            overtime=hours-self.RegHours
            regular = hours - overtime
        dict1['name'] = self.FirstName+" "+self.LastName
        dict1['Date'] = date
        dict1['Regular Hours Worked'] = regular
        dict1['Overtime Hours Worked'] = overtime
        dict1['Regular Rate'] = self.HourlyRate
        dict1['Overtime Rate'] = int(self.HourlyRate*self.OTMultiple)
        dict1['Regular Pay'] = regular*self.HourlyRate
        dict1['Overtime Pay'] = int(self.HourlyRate*self.OTMultiple)*overtime
        gross = regular*self.HourlyRate + int(self.HourlyRate*self.OTMultiple)*overtime
        dict1['Gross Pay'] = gross
        standardratepay = gross
        higerratepay=0
        if standardratepay > self.StandardBand:
            standardratepay = self.StandardBand
            higerratepay = gross - standardratepay

        dict1['Standard Rate Pay'] = int(standardratepay)
        dict1['Higher Rate Pay'] = int(higerratepay)
        dict1['Standard Tax'] = int(standardratepay*0.2)
        dict1['Higher Tax'] = higerratepay*0.4
        dict1['Total Tax'] = standardratepay*0.2 + higerratepay*0.4
        dict1['Tax Credit'] = self.TaxCredit
        nettax = 0
        if standardratepay*0.2 + higerratepay*0.4 > self.TaxCredit:
            nettax = (standardratepay*0.2 + higerratepay*0.4) - self.TaxCredit
        dict1['Net Tax'] = round(nettax, 1)
        prsi = round((gross*0.04),2)
        dict1['PRSI'] = prsi
        deductions = round((prsi + nettax),2)
        dict1['Net Deductions'] = deductions
        dict1['Net Pay'] = round((gross - deductions),2)

        return dict1


P= Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
print(P.computePayment(42,'31/10/2021'))
