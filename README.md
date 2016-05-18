<<<<<<< HEAD
## Combination Geocoder
###Brute force checking of accuracy for unfamiliar location data. 

The aim here is to run an address through several geocoders at once. This will tell us if this location, which may or may not be spelled correctly, is good enough to be geocoded. 

This works, because the geocoders used here all behave differently when given bogus addresses. However, all return predictable and similar results for good addresses. So, if my script gives your address a range that's too big, your address needs to be looked at more closely.

###This code is terrible (being honest)

This is one of the first Python programs I ever made. I made it out of necessity to work with a problematic dataset. I'm now trying to use it for a different purpose and finding my code hard to read. So, this is going through a major refactor while I restructure the program so it's:

- easier to read
- more reliable

I'm keeping this in the same repo as a record of how much my Python skills have improved.

###Technology used

```Python 2.7.8``` is my flavour.

I'm using a virtual environment to isolate the packages this program requires. This uses the ```requests``` and ```pytest``` modules and you can install them with pip in your virtualenv. All other packages are standard python packages.

#### To use this script - 
- Create your own config.py file to store your API keys. Note, all services have a cap on requests per day before they ask for money.
- Go to the ```application/geocoder``` file and alter the filename of your csv
- In the same file, set the ```app.range_iter_limits``` to focus on the files for geocoding.
- The program will open your csv, alter the line with its results, and save it again. This helps if you suddenly lose your connection.

#### Notes on geocoders - 
- They all seem to favour addresses that are fed in with the most specific detail first. 
=======
# Combination Geocoder
Python 2.7 script for checking the accuracy/spelling of locations in a CSV by using several geocoding APIs at once. 
Similar results indicate accurate addresses.

#### The reason for this project -
Geocoding is messy. 
If you have incorrect or innaccurate addresses, some geocoders will return results regardless.
If you're geocoding locations that you aren't familiar with, it's hard to know if the geocoding was successful.

#### Using several geocoders at once serves as a kind of acid test -
When geocoders are fed accurate locations, they all return similar and predictable results.
When innacurate locations are fed, the geocoders behave differently.
Observing these differences can be a quick way to check if your locations are accurate enough for a geocoder to return accurate coordinates.

#### To use this script - 
- Get the API keys from every geocoding service, save them in the API functions (line 45).
- Load this script with Python.
- It will prompt you to enter a file name. Enter .csv on the end. - Eg ```csvToGeocode.csv```
- The next prompt is for location columns (0 = first, 1 = second, 2 = third etc). Enter them as a string. - EG ```2,3,6```. For each row, the script will concatenate those strings and feed those to the APIs.
- If all goes well, you will see a file called 'results_...' in the same directory.

#### Notes on geocoders - 
- They all seem tofavour addresses that are fed in with the most specific detail first. 
>>>>>>> c5013041d460ad99424f3ec7f7734a6da58552ba
- This is good ```1, Smith Street, Town, State, Country``` Not good - ```State, Country, 1, Smith Stree, Town```
- Pick Point will often not return results for incorrect or misspelt addresses.
- All have terms of service. 
- Bing is accurate, but has usage limits. The free account allows 50 requests per day.

<<<<<<< HEAD
=======
#### Features to add
- Get estimates of location accuracy from geocoders, and use that to make a weighted average. (Self-admitted innacurate coordinates will have less weighting).

>>>>>>> c5013041d460ad99424f3ec7f7734a6da58552ba
#### Examples of API requests -
- bingMapsTemplate = http://dev.virtualearth.net/REST/v1/Locations/PLACENAME?o=xml&key=BINGMAPSKEY
- mapQuestTemplate = http://www.mapquestapi.com/geocoding/v1/address?key=YOUR_KEY_HERE&location=PLACENAME&callback=renderGeocode
- openCageTemplate = http://api.opencagedata.com/geocode/v1/json?q=PLACENAME&key=YOURKEY
- pickPointTemplate = https://pickpoint.io/api/v1/forward?key=APIKEY&q=PLACENAME
- googleMapsTemplate = https://maps.googleapis.com/maps/api/geocode/xml?address=PLACENAME&key=APIKEY
<<<<<<< HEAD

=======
>>>>>>> c5013041d460ad99424f3ec7f7734a6da58552ba
