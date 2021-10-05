x=16637000000.0                     # distance traveled as of 9/25/09
print("how many days since 9/25/09?")
y = int(input())                    # y = amount of days since 9/25/09    
x = (y*38241*24)                    # x = amount of distance traveled by the Voyager
print (x,"miles") 
print(x*1.609344,"Kilometers")      #converting to KM
print(x/92955887.6,"Astronomical Units")    #converting to AU
print(x*1609.344*2/299792458*3600,"hours in a roundtrip at light speed")    # (Amount of distance traveled by Votager in miles)*(Conversion to meters)*(roundtrip)/(speed of light in meters/second)(converting to meters/hour)


