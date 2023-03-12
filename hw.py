name = "Vihaan"
weekdays = 5
hw_per_weekday = 3
weekenddays = 2
hw_per_weekend = 2
hw_per_week = hw_per_weekday * weekdays + hw_per_weekend * weekenddays
print("%s did %s hours of hw in a week" %(name, hw_per_week))