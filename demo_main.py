from demo_room import Room
from demo_item import Item
from demo_character import Enemy, Friendly, Character

print()

print('***********************************************')
print('***** WELCOME TO THE TEXT-BASED ADVENTURE *****')
print('***********************************************')
print()
#print('Input name here:')
#user_name = input('>')


kitchen = Room('Kitchen')
ballroom = Room('Ballroom')
dining_hall = Room('Dining Hall')
main_hall = Room('Main Hall')
hallway = Room('Hallway')

kitchen.set_description('A dark and dirty room buzzing with flies')
ballroom.set_description('An eerie room with a single piano in the middle')
dining_hall.set_description('Broken plates were scattered across the floor')
main_hall.set_description('Tattered curtains and broken floor tiles')
hallway.set_description('')

kitchen.set_name('Kitchen')
ballroom.set_name('Ballroom')
dining_hall.set_name('Dining Hall')
main_hall.set_name('Main Hall')
hallway.set_name('Hallway')

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(hallway, 'west')
hallway.link_room(dining_hall, 'east')
hallway.link_room(ballroom, 'west')
ballroom.link_room(hallway, 'east')
ballroom.link_room(main_hall, 'south')
main_hall.link_room(ballroom, 'north')

#user = Character(user_name, 'A new challenger')

dave = Enemy('Dave', 'A smelly zombie')
dave.set_conversation('brains!!!!')
dave.set_weakness('Light')
main_hall.set_character(dave)

gary = Enemy('Gary', 'A small goblin')
gary.set_conversation('Grawwwwwg')
gary.set_weakness('Money')
hallway.set_character(gary)

tory = Friendly('Tory', 'A wise wizard')
dining_hall.set_character(tory)
tory.set_conversation('Welcome to the maze. \nHow can I help?')

current_room = kitchen


while True:
    print('\n')
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is dave:
        inhabitant.describe()
        dave.fight()
    if inhabitant is tory:
        inhabitant.describe()
        tory.talk()
    if inhabitant is gary:
        inhabitant.describe()
        gary.fight()
    command = input('>')
    current_room = current_room.move(command)
    if command == 'exit':
        print("You've exited")
        quit()
