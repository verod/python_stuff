hours = raw_input("Enter number of hours: ")
rate = raw_input("Enter hourly rate ($): ")

try:
	hours = int(hours)
except:
	print "Please enter a number"
	exit()

try:
	rate = int(rate)
except:
	print "Please enter a number for rate"
	rate = 0

if hours > 40:
	pay = 40 * rate + (hours-40)*rate*1.5
else:
	pay = hours * rate

print "You deserve", str(pay), "$"
