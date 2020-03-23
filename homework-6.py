# William Chase Hamby
# 3/23/20
# homework-6.py
# -*- coding: utf-8 -*-
# This is the description for homework 6

# Part I
def merge_strings(stringcheese1, stringcheese2):
    stringcheese3 = stringcheese1 + " " + stringcheese2
    print(stringcheese3)
stringcheese1 = input("Please enter your first string of cheese: ")
stringcheese2 = input("Please enter your second string of cheese: ")

merge_strings(stringcheese1, stringcheese2)
print("\n")

# Part II
class Pet:
  def __init__(self, name, age, species):
    self.name = name
    self.age = age
    self.species = species
  def display_info(self):
    print("I have a {} named {} who is {} years old".format(self.species, self.name, self.age))
my_pet = Pet("Hermes", "75 million", "velociraptor")
my_pet.display_info()
