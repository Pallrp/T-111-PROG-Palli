#Start by asking the user to input days
days_past = int(input("Number of days after 9/25/1977: "))
#A few helpful, long numbers to prevent me from misspelling later
miles_to_km = 1.609344
miles_to_AU = 92955877.6
#Since 25th September 1977 Voyager has travelled 16,637,000,000 miles
distance_1977_miles = float(16637000000)
distance_1977_km = float(distance_1977_miles * miles_to_km)
#Voyager 1 travels 38,241 mp/h
speed_mph = 38241
#To convert miles to km I will need to multiply miles by 1,609344
speed_km = speed_mph * miles_to_km

#Converting the days to hours
days_past_hours = days_past * 24 

#To find out how far Voyager has travelled total I'll first need to find out how far it has travelled in (input) many days
dist_travelled_input_miles = speed_mph * days_past_hours
dist_travelled_input_km = speed_km * days_past_hours


#To find the total distance travelled I'll simply add distance_1977 to the distance it has travelled in (input) days, then round down
total_dist_miles =int(dist_travelled_input_miles+distance_1977_miles)
total_dist_km = round(dist_travelled_input_km + distance_1977_km)

#Converting to AU and rounding down
total_dist_AU = round((dist_travelled_input_miles + distance_1977_miles)/ miles_to_AU)

print("Miles from the sun:" , total_dist_miles)
print("Kilometers from the sun:", total_dist_km)
print("AU from the sun:" , total_dist_AU)

