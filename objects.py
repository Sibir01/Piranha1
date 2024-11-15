# objects.py

class Apple:
    def __init__(self):
        self.name = "Apple"
        self.shape = "Round"
        self.color = "Green"
        self.weight = "Light"

    def eat(self):
        return "Eating the apple"


class Pizza:
    def __init__(self):
        self.name = "Pizza"
        self.shape = "Round"
        self.type = "Cheese"
        self.temperature = "Hot"

    def eat(self):
        return "Eating the pizza"


class Car:
    def __init__(self):
        self.name = "Car"
        self.speed = "Fast"
        self.color = "Green"
        self.material = "Hard"

    def drive(self):
        return "Driving the car"

class Egg:
    def __init__(self):
        self.name = "Egg"
        self.color = "White"
        self.fragility = "Fragile"
        self.temperature = "Cold"

    def eat(self):
        return "Eating the egg"

    def throw(self):
        return "Throwing the egg"


class Ball:
    def __init__(self):
        self.name = "Ball"
        self.shape = "Round"
        self.color = "White"

    def throw(self):
        return "Throwing the ball"


# Новые объекты

class Dog:
    def __init__(self):
        self.name = "Dog"
        self.breed = "Labrador"
        self.color = "Brown"

    def bark(self):
        return "Barking"

    def fetch(self):
        return "Fetching the ball"


class Phone:
    def __init__(self):
        self.name = "Phone"
        self.brand = "Apple"
        self.color = "Black"

    def call(self):
        return "Calling someone"

    def text(self):
        return "Sending a text"


class Table:
    def __init__(self):
        self.name = "Table"
        self.material = "Wood"
        self.shape = "Rectangular"

    def use(self):
        return "Using the table"


class Refrigerator:
    def __init__(self):
        self.name = "Refrigerator"
        self.color = "Silver"
        self.capacity = "Large"

    def cool(self):
        return "Cooling items"

    def store(self):
        return "Storing food"


class Television:
    def __init__(self):
        self.name = "Television"
        self.brand = "Samsung"
        self.size = "55 inches"

    def watch(self):
        return "Watching TV"

    def turn_on(self):
        return "Turning on the TV"


class Lamp:
    def __init__(self):
        self.name = "Lamp"
        self.color = "Yellow"
        self.type = "LED"

    def light_up(self):
        return "Lighting up the room"


class Bicycle:
    def __init__(self):
        self.name = "Bicycle"
        self.color = "Red"
        self.type = "Mountain"

    def ride(self):
        return "Riding the bicycle"


class Book:
    def __init__(self):
        self.name = "Book"
        self.author = "J.K. Rowling"
        self.genre = "Fantasy"

    def read(self):
        return "Reading the book"


class Chair:
    def __init__(self):
        self.name = "Chair"
        self.material = "Plastic"
        self.color = "Blue"

    def sit(self):
        return "Sitting on the chair"


class Watch:
    def __init__(self):
        self.name = "Watch"
        self.brand = "Rolex"
        self.color = "Gold"

    def watch_time(self):
        return "Checking the time"


class Airplane:
    def __init__(self):
        self.name = "Airplane"
        self.type = "Aircraft"

    def fly(self):
        return "Flying in the sky"

    def land(self):
        return "Landing on the runway"


class Bicycle:
    def __init__(self):
        self.name = "Bicycle"
        self.type = "Vehicle"

    def pedal(self):
        return "Pedaling the bicycle"

    def ring_bell(self):
        return "Ringing the bell"


class Refrigerator:
    def __init__(self):
        self.name = "Refrigerator"
        self.type = "Appliance"

    def cool(self):
        return "Cooling items"

    def freeze(self):
        return "Freezing food"


class Guitar:
    def __init__(self):
        self.name = "Guitar"
        self.type = "Musical Instrument"

    def play(self):
        return "Playing guitar"

    def strum(self):
        return "Strumming the strings"


class VacuumCleaner:
    def __init__(self):
        self.name = "Vacuum Cleaner"
        self.type = "Appliance"

    def vacuum(self):
        return "Vacuuming the floor"

    def clean_filter(self):
        return "Cleaning the filter"


class Helicopter:
    def __init__(self):
        self.name = "Helicopter"
        self.type = "Aircraft"

    def hover(self):
        return "Hovering in the air"

    def land(self):
        return "Landing"


class Microwave:
    def __init__(self):
        self.name = "Microwave"
        self.type = "Appliance"

    def heat(self):
        return "Heating food"

    def defrost(self):
        return "Defrosting food"


class Laptop:
    def __init__(self):
        self.name = "Laptop"
        self.type = "Electronics"

    def browse(self):
        return "Browsing the internet"

    def type(self):
        return "Typing on the keyboard"


class WashingMachine:
    def __init__(self):
        self.name = "Washing Machine"
        self.type = "Appliance"

    def wash(self):
        return "Washing clothes"

    def spin(self):
        return "Spinning the clothes"


class Refrigerator:
    def __init__(self):
        self.name = "Refrigerator"
        self.type = "Appliance"

    def cool(self):
        return "Cooling food"

    def store(self):
        return "Storing perishable goods"


class Telescope:
    def __init__(self):
        self.name = "Telescope"
        self.type = "Instrument"

    def zoom(self):
        return "Zooming in on a distant object"

    def focus(self):
        return "Focusing the lens"


class Printer:
    def __init__(self):
        self.name = "Printer"
        self.type = "Electronics"

    def print(self):
        return "Printing a document"

    def scan(self):
        return "Scanning a document"


class Radio:
    def __init__(self):
        self.name = "Radio"
        self.type = "Electronics"

    def tune(self):
        return "Tuning to a station"

    def play(self):
        return "Playing music"


class Fridge:
    def __init__(self):
        self.name = "Fridge"
        self.type = "Appliance"

    def cool(self):
        return "Cooling food"

    def store(self):
        return "Storing perishable goods"


class Fan:
    def __init__(self):
        self.name = "Fan"
        self.type = "Appliance"

    def turn_on(self):
        return "Turning on the fan"

    def turn_off(self):
        return "Turning off the fan"


class Camera:
    def __init__(self):
        self.name = "Camera"
        self.type = "Electronics"

    def capture(self):
        return "Capturing a photo"

    def zoom_in(self):
        return "Zooming in on the subject"


class Printer:
    def __init__(self):
        self.name = "Printer"
        self.type = "Electronics"

    def print(self):
        return "Printing a document"

    def scan(self):
        return "Scanning a document"


class Fan:
    def __init__(self):
        self.name = "Fan"
        self.type = "Appliance"

    def start(self):
        return "Turning on the fan"

    def stop(self):
        return "Turning off the fan"


class Refrigerator:
    def __init__(self):
        self.name = "Refrigerator"
        self.type = "Appliance"

    def cool(self):
        return "Cooling food"

    def freeze(self):
        return "Freezing items"


class Mixer:
    def __init__(self):
        self.name = "Mixer"
        self.type = "Appliance"

    def mix(self):
        return "Mixing ingredients"

    def blend(self):
        return "Blending food"


class Smartphone:
    def __init__(self):
        self.name = "Smartphone"
        self.type = "Electronics"

    def call(self):
        return "Making a phone call"

    def text(self):
        return "Sending a text message"

