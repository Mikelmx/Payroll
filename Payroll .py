'''
Michael Mcmanimon
Total Weekly Pay
'''

weekHours = float(input("Enter regular hours worked: "))

overTime = float(input("Enter overtime hours worked: "))

hourlyWage =  18

overTimeWage = hourlyWage * 1.5

regularPay = weekHours * hourlyWage

overTimePay = overTime * overTimeWage

totalWage = regularPay + overTimePay

print ("Your pay for this week equals ", totalWage)
