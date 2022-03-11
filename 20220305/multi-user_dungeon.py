import itertools
import readline
import shlex
import cmd

class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    def auch(self):
        self.hp -= 10

    def is_dead(self):
        return self.hp <= 0

field = [[[] for j in range(10)] for i in range(10)]
player = (0, 0)


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
        for mnstr in field[x % 10][y % 10]:
            if mnstr.name == monster.name:
                mnstr.hp = monster.hp
                break
        else:
            field[x % 10][y % 10].append(monster)

    def do_show(self, args):
        if args != 'monsters':
            print("Unknown operation")
            return
        for x, line in enumerate(field):
            for y, monsters in enumerate(line):
                for monster in monsters:
                    print(f"{monster.name} at ({x} {y}) hp {monster.hp}")
    
    def do_move(self, arg):
        if arg not in ('up', 'down', 'left', 'right'):
            print("Unknown direction.")
            return
        global player
        mv = {
            'up': (player[0], player[1] - 1),
            'down': (player[0], player[1] + 1),
            'left': (player[0] - 1, player[1]),
            'right': (player[0] + 1, player[1]),
        }
        np = mv[arg]
        if np[0] not in range(10) or np[1] not in range(10):
            print("cannot move")
            return
        player = np
        print(f"player at {np[0]} {np[1]}")
        if field[np[0]][np[1]]:
            monsters_str = ", ".join(f"{monster.name} {monster.hp} hp" for monster in field[np[0]][np[1]])
            print('encountered:', monsters_str)
            
    def complete_move(self, prefix, s, idxstart, idxend):
        return [direction for direction in ('up', 'down', 'left', 'right') if direction.startswith(prefix)]

    def do_attack(self, arg):
        monsters = field[player[0]][player[1]]
        arg = shlex.split(arg)
        arg = arg[0] if len(arg) > 0 else ""
        monster = tuple(filter(lambda m: m.name == arg, monsters))
        if not monster:
            print(f"no {arg} here")
            return 
        monster = monster[0]
        monster.auch()
        if monster.is_dead():
            monsters.remove(monster)
            print(f"{monster.name} dies")
        else:
            print(f"{monster.name} lost 10 hp, now has {monster.hp} hp")

    __last_attack_pos = (-1,-1)
    __compl_att_it = None
    def complete_attack(self, prefix, s, idxstart, idxend):
        monsters = field[player[0]][player[1]]
        prefix = shlex.split(s)
        prefix = prefix[1] if len(prefix) > 1 else ""
        t = [mnstr.name.replace(' ', '\\ ') for mnstr in monsters if mnstr.name.startswith(prefix)]
        return t

    def do_EOF(self, arg):
        print("bye")
        return 1
        


Dungeon().cmdloop()
