#LeetCode 1732- Highest Altitude

#Solution

gain = [-5, 1, 5, 0, -7]
 
altitude = 0
highest = 0

for number in gain: 
    altitude = altitude + number

    if altitude > highest:
        highest = altitude

print (highest)