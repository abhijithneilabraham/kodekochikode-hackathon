# kodekochikode
repo to use for kodekochikode hacakthon
the chat1.py and chat2.py contains code for training with rasa nlu and dialgoues with rasa core.


Rasa is an open source framework we are using here.


We used Google Maps Api for calculating distance between the user and the hospitals nearby and using this data to suggest which hospital to consult based on the services they provide and the medical condition of the user.
It is in the folder googlemaps.
hezyra web has the html page for web service we plan to do




The major stuff we do using rasa are in rasa_stuff folder


The end product is a hospital traffic monitoring system using web service and a chatbot interface and google maps api is used to get location of all nearby hospitals.



Hospital traffic monitoring system here aims to provide the right information about the right hospital to be attended by a person,without distance being the first priority. A person should get the right treatment and the treatment probability and the admittance probability for each hospital is calculated and the hospital name and address and distance from the current location is shown. This is especially aimed in the situation where there is a breakout of an epidemic disease and peoplle rush to nearby hospitals and make it crowded. So, to avoid the rush to a possible level, the data is taken from all the hospitals in the are about the number of rooms which are available and also the availability of doctors are also taken and updated to a database. This database is then used by the chatbot interface to then respond to the user's query and find him/her the right hospital to get treated.
