import phonenumbers

from myNumber import  number

from phonenumbers import geocoder

import folium

#from opencagedata.com create an acccount and get an API key
key ="9382d94028664034ac5e405b725a0e99"

#get the country to which this number belong
sanNumber = phonenumbers.parse(number)
#yourLocation = geocoder.description_for_number(sanNumber, "en")
#print("This is the Country to which this number belong: ",yourLocation)

#get the service provider

from phonenumbers import carrier

#service_provider = phonenumbers.parse(number)
service_name = carrier.name_for_number(sanNumber, "en")
print("This is the service provider for your number: ",service_name)