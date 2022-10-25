# (5 points): As a developer, I want to make at least three commits with descriptive messages 
# (5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, 
# and entertainment in their own separate Lists. 
# (5 points): As a user, I want a destination to be randomly selected for my day trip. 
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation,
#  and/or form of entertainment if I don’t like one or more of those things.
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
# (10  points): As a user, I want to display my completed trip in the console
# (5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility.
#  Remember, each function should do just one thing! 






import time
import random

destinations = ['Florida', 'New Mexico', 'New York', 'Montana', 'California']
restaurants = ['McDonalds', 'Taco Bell', 'Wendys', 'KFC', 'Chik-Fil-A']
transportation_options = ['Car', 'Plane', 'Train', 'Roller-Blades', 'Pogo-Stick']
entertainment_options = ['some Live Music', 'the Aquarium', 'a State Park', 'the Zoo', 'the Theo Von Comedy Show']

destination = random.choice(destinations)
restaurant = random.choice(restaurants)
transport = random.choice(transportation_options)
entertainment = random.choice(entertainment_options)
greeting_statement = (f'For your trip we have picked {destination}, you will be traveling there by {transport} and you will be enjoying {entertainment} while eating {restaurant}!')

print(greeting_statement)
time.sleep(1)   

confirm_trip = input('Please type Y/N in the console to let us know if you are happy with your trip.')

def first_choice(confirm_trip):
    while confirm_trip == 'Y':
        print(f'Enjoy your trip to {destination}, traveling by {transport}, while visiting {entertainment} and eating {restaurant}!!!')
        time.sleep(1)
    return 
    
first_choice(confirm_trip)


def dif_destination(confirm_trip):
    while confirm_trip != 'Y':
        destination = random.choice(destinations)
        confirm_trip = input(f'Sorry you werent happy with the destination we picked for you. Does {destination} sound better for you?')
    else:
        print(f'Enjoy your vacation in {destination}!!!')
        time.sleep(2)
        return destination
   

destination = dif_destination(confirm_trip)


def dif_transportation(confirm_trip):
    while confirm_trip != 'Y':
        transport = random.choice(transportation_options)
        confirm_trip = input(f'Sorry you werent happy with the transportation we picked for you. Does {transport} sound better?')
    else:
        print(f'Enjoy your trip traveling by {transport}')
        time.sleep(2)
    return transport

transport = dif_transportation(confirm_trip)


def dif_entertainment(confirm_trip):
    while confirm_trip != 'Y':
        entertainment = random.choice(entertainment_options)
        confirm_trip = input(f'Sorry you werent happy with your entertainment choice. Does {entertainment} sound better?')
    else:
        print(f'Enjoy your trip in {destination} with {entertainment} as your entertainment!')
        time.sleep(2)
    return entertainment

entertainment = dif_entertainment(confirm_trip)


def dif_restaurant(confirm_trip):
    while confirm_trip != 'Y':
        restaurant = random.choice(restaurants)
        confirm_trip = input(f'Sorry you werent happy with the restaurant we picked for you. Does {restaurant} sound better?')
    else:
        print(f'Enjoy your vacation in {destination} eating {restaurant} while enjoying {entertainment}')
        time.sleep(2)
    return restaurant
        
restaurant = dif_restaurant(confirm_trip)




