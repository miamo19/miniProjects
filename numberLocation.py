import phonenumbers

number = input("Enter your phone number + country code: ")

from phonenumbers import geocoder

import folium

#from opencagedata.com create an acccount and get an API key
key ="9382d94028664034ac5e405b725a0e99"

#get the country to which this number belong
sanNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(sanNumber, "en")
print("This is the Country to which this number belong: ",yourLocation)

#get the service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
service_name = carrier.name_for_number(service_provider, "en")
print("This is the service provider for your number: ",service_name)

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)
qeury = str(yourLocation)
results = geocoder.geocode(qeury)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

#folium package takeover

myMap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

#Save Map in html file

myMap.save("mylocation.html")
