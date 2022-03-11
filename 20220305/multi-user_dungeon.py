import readline
import shlex
import cmd

class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

field = [[[] for j in range(10)] for i in range(10)]

class Dungeon(cmd.Cmd):
    prompt = "(ง^-^)ง "

    def do_add(self, arg):
        """Add monster"""
        args = shlex.split(arg)
        if len(args) != 8:
            print("Wrong arguments count.")
            return
        if args[0] != "monster":
            print("Unknown operation.")
            return
        if args[1] != "name":
            print("Set name.")
            return
        name = args[2]
        if args[3] != "hp":
            print("Set HP in integer.")
            return
        try:
            hp = int(args[4])
        except ValueError:
            print("HP must be integer.")
            return
        if args[5] != "coords":
            print("Specify coordinates.")
            return
        try:
            x, y = int(args[6]), int(args[7])
        except ValueError:
            print("Coordinates must be integer")
            return
        monster = Monster(name, hp)
        field[x % 10][y % 10].append(monster)

    def do_show(self, args):
        if args != 'monsters':
            print("Unknown operation")
            return
        for x, line in enumerate(field):
            for y, monsters in enumerate(line):
                for monster in monsters:
                    print(f"{monster.name} at ({x} {y}) hp {monster.hp}")

    def do_EOF(self, arg):
        print("bye")
        return 1
        


Dungeon().cmdloop()
