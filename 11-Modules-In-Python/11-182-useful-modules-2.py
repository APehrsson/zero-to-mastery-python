import datetime
from array import array

print(datetime.time(9,58)) #Creates time objects
print(datetime.date.today()) 

arr = array('i', [1,2,3]) #Takes less memory than a list. Can be used insted of generaters to optimize code

print(arr[0])