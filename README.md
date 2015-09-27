# Combination Geocoder
Python script for checking the accuracy/spelling of locations in a CSV by using several geocoding APIs at once. 
Similar results indicate accurate addresses.

#### The reason for this project -
Geocoding is messy. 
If you have incorrect or innaccurate addresses, some geocoders will return results regardless.
If you're geocoding locations that you aren't familiar with, it's hard to know if the geocoding was successful.

#### Using several geocoders at once serves as a kind of acid test -
When geocoders are fed accurate locations, they all return similar and predictable results.
When innacurate locations are fed, the geocoders behave differently.
Observing these differences can be a quick way to check if your locations are accurate enough for a geocoder to return accurate coordinates.
If you get bad results, you can change the addresses and run the process again.

#### To use this script - 
- Get the API keys from every geocoding service, save them in the API functions (line 45).
- Load this script with Python.
- It will prompt you to enter a file name. Enter .csv on the end. - Eg ```csvToGeocode.csv```
- The next prompt is for location columns (0 = first, 1 = second, 2 = third etc). Enter them as a string. - EG ```2,3,6```. For each row, the script will concatenate those strings and feed those to the APIs.
- If all goes well, you will see a file called 'results_...' in the same directory.

#### Notes on geocoders - 
- They all seem tofavour addresses that are fed in with the most specific detail first. 
- This is good ```1, Smith Street, Town, State, Country``` Not good - ```State, Country, 1, Smith Stree, Town```
- Pick Point will often not return results for incorrect or misspelt addresses.
- All have terms of service. 
- Bing is accurate, but has usage limits. The free account allows 50 requests per day.

#### Examples of API requests -
- bingMapsTemplate = http://dev.virtualearth.net/REST/v1/Locations/PLACENAME?o=xml&key=BINGMAPSKEY
- mapQuestTemplate = http://www.mapquestapi.com/geocoding/v1/address?key=YOUR_KEY_HERE&location=PLACENAME&callback=renderGeocode
- openCageTemplate = http://api.opencagedata.com/geocode/v1/json?q=PLACENAME&key=YOURKEY
- pickPointTemplate = https://pickpoint.io/api/v1/forward?key=APIKEY&q=PLACENAME
- googleMapsTemplate = https://maps.googleapis.com/maps/api/geocode/xml?address=PLACENAME&key=APIKEY
