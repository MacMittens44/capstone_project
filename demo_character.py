class Character():

    # Creates Character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    #Describes Character
    def describe(self):
        print(f'{self.name} is here!')
        print(self.description)
    
    #Waht the charater will say 
    def set_conversation(self, conversation):
        self.conversation = conversation
    
    def get_conversation(self):
        return self.conversation

    #Talk to the character
    def talk(self):
        if self.conversation is not None:
            print(f'[{self.name} says] {self.conversation}')
        else:
            print(f"{self.name} doesn't want to talk to you")
    
    #Fight with this charater
    def fight(self, combat_item):
        print(f"{self.name} doesn't want to fight with you")
        return True

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
    
    def get_weakness(self):
        return self.weakness
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness
    
    def fight(self):
        print('What item do you use?')
        combat_item = input('>')
        if combat_item == self.weakness:
            print(f'You fend {self.name} off with the {combat_item}')
            return True
        else:
            print(f'Your {combat_item} is useless')
            print(f'{self.name} crushes you, puny adventurer')
            print('Game Over')
            quit()
    
    def talk(self):
        print(f'Talk to {self.name} [Y] / [N]')
        reply = input('>')
        if reply == 'Y':
            print(f'{self.name} says: {self.conversation}')
            print(f'{self.name} starts a fight!!')
            self.fight()
        if reply == 'N':
            print(f"You can't run from {self.name}")
            print(f'{self.name} starts a fight!!')
            self.fight()

class Friendly(Character):
    def __init__(self, char_name, char_description):
        super(). __init__(char_name, char_description)
    
    def talk(self):
        print(f'{self.conversation}')
        print('Ask for information? [Y] / [N]')
        answer = input('>')
        if answer == 'Y':
            print('There are two more rooms ahead of you')
            print('For what is small you need Money and for what is undead you need Light')
            print('Go east')
            print('I cannot give more information')
        if answer == 'N':
            print('north or east')