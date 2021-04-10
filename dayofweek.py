import datetime

# Assigning either yes unfortunately or yay weekend
# Making weekdays equal each other to assign same variable, same with
Monday=Tuesday=Wednesday=Thursday=Friday = "Yes, unfortunately today is a weekday."
Saturday=Sunday = "It is the weekend, yay!"

# Make day of week into integer
dayasnumber = datetime.datetime.today().weekday()

# Assigining intergers to days of week
weekdays = {0:Monday,1:Tuesday, 2:Wednesday, 
           3:Thursday,4:Friday,5:Saturday,6:Sunday}

print (weekdays[dayasnumber])

# Referece: https://stackoverflow.com/questions/16348815/python-assigning-multiple-variables-to-same-value-list-behavior