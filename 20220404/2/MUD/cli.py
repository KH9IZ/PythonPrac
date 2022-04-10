"""Shell-like interface for game."""

import readline  # noqa: F401
import shlex
import cmd
import core


class Dungeon(cmd.Cmd):
    """Game object."""

    prompt = "(ง^-^)ง "

    def do_add(self, arg):
        """Add monster."""
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
        core.add_monster(name=name, hp=hp, coords=(x, y))

    def do_show(self, args):
        """Show all monsters on field."""
        if args != 'monsters':
            print("Unknown operation")
            return
        for monster, (x, y) in core.get_monsters():
            print(f"{monster.name} at ({x} {y}) hp {monster.hp}")

    def do_move(self, arg):
        """Move player by direction."""
        if arg not in ('up', 'down', 'left', 'right'):
            print("Unknown direction.")
            return
        global player
        try:
            player_pos, monsters = core.move_player(direction=arg)
        except ValueError as err:
            print(err.args[0])
            return

        print(f"player at {player_pos[0]} {player_pos[1]}")
        if monsters:
            monsters_str = ", ".join(f"{monster.name} {monster.hp} hp"
                                     for monster in monsters)
            print('encountered:', monsters_str)

    def complete_move(self, prefix, s, idxstart, idxend):
        """Completion when typing move."""
        return [direction
                for direction in ('up', 'down', 'left', 'right')
                if direction.startswith(prefix)]

    def do_attack(self, arg):
        """Attack monster in currect cell."""
        arg = shlex.split(arg)
        arg = arg[0] if len(arg) > 0 else ""
        try:
            monster = core.attack_monster(name=arg)
        except ValueError as err:
            print(err.args[0])
            return
        if monster.is_dead():
            print(f"{monster.name} dies")
        else:
            print(f"{monster.name} lost 10 hp, now has {monster.hp} hp")

    __last_attack_pos = (-1, -1)
    __compl_att_it = None

    def complete_attack(self, prefix, s, idxstart, idxend):
        """Completion for attack command."""
        monsters = core.get_available_monsters()
        prefix = shlex.split(s)
        prefix = prefix[1] if len(prefix) > 1 else ""
        t = [mnstr.name.replace(' ', '\\ ')
             for mnstr in monsters
             if mnstr.name.startswith(prefix)]
        return t

    def do_EOF(self, arg):
        """End of game by ^D escape command."""
        print("bye")
        return 1
