from demo_character import Character
from demo_character import Enemy
import demo_room

dave = Enemy('Dave', 'A smelly zombie')
dave.describe()

dave.set_conversation('brains!!!!')
#dave.talk()

dave.set_weakness('cheese')


dave.fight()

