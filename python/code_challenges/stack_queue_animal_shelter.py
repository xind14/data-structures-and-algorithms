from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.dogs_queue=Queue()
        self.cats_queue=Queue()

    def enqueue(self, animal):
        if animal.name=='dog':
            self.dogs_queue.enqueue(animal)
        if animal.name=='cat':
            self.cats_queue.enqueue(animal)

    def dequeue(self,pref):
        if pref=='dog':
            if not self.dogs_queue.is_empty():
                return self.dogs_queue.dequeue()
        elif pref=='cat':
            if not self.cats_queue.is_empty():
                return self.cats_queue.dequeue()
        return None


class Animal:
    def __init__(self, species, name):
        self.species=species
        self.name=name


class Dog:
    def __init__(self, name='dog'):
        self.name=name



class Cat:
    def __init__(self, name='cat'):
        self.name=name



# Create a class called AnimalShelter which holds only dogs and cats.
# The shelter operates using a first-in, first-out approach.
# Implement the following methods:
# enqueue
# Arguments: animal
# animal can be either a dog or a cat object.
# It must have a species property that is either "cat" or "dog"
# It must have a name property that is a string.
# dequeue
# Arguments: pref
# pref can be either "dog" or "cat"
# Return: either a dog or a cat, based on preference.
# If pref is not "dog" or "cat" then return null.

