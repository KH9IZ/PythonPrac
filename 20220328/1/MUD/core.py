"""Realiztion of multi-user dungeon logic."""
from typing import List, Iterator


class Monster:
    """
    Monster class.

    :param name: Name of monster
    :type name: str
    :param hp: Count of monster's health points
    :type hp: int
    """

    def __init__(self, name: str, hp: int):
        """
        Monster class.

        :param name: Name of monster
        :type name: str
        :param hp: Count of monster's health points
        :type hp: int
        """
        self.name = name
        self.hp = hp

    def auch(self):
        """Hit monster by fixed amount of hp."""
        self.hp -= 10

    def is_dead(self) -> bool:
        """
        Check has monster more then 0 hp or not.

        :return: True if monster is dead and False if monster still alive
        :rtype: bool
        """
        return self.hp <= 0


field = [[[] for j in range(10)] for i in range(10)]
player = (0, 0)


def add_monster(name: str, hp: int, coords: tuple[int]):
    """
    Add new monster on field.

    :param name: Monster's name
    :type name: str
    :param hp: Amount of monster's hps
    :type hp: int
    :param coords: 2D coordinates of monster on the field
    :type coords: tuple[int] size of 2
    """
    x, y = coords
    monster = Monster(name, hp)
    for mnstr in field[x % 10][y % 10]:
        if mnstr.name == monster.name:
            mnstr.hp = monster.hp
            break
    else:
        field[x % 10][y % 10].append(monster)


def get_monsters() -> Iterator[Monster]:
    """
    Return generator yielding all monsters from field.

    :return: Generator yielding each monster
    :rtype: Iterator[Monster]
    """
    for x, line in enumerate(field):
        for y, monsters in enumerate(line):
            for monster in monsters:
                yield monster, (x, y)


def get_available_monsters() -> List[Monster]:
    """
    Return Monsters in player's cell.

    :returns: List of all monsters available to attack
    :rtype: List[Monster]
    """
    return field[player[0]][player[1]]


def move_player(direction):
    """
    Move player on one cell by direction.

    :param direction: Direction for move
    :type direction: str
    :raises ValueError: Error raised when trying to move outside the field
    """
    global player
    mv = {
        'up': (player[0], player[1] - 1),
        'down': (player[0], player[1] + 1),
        'left': (player[0] - 1, player[1]),
        'right': (player[0] + 1, player[1]),
    }
    np = mv[direction]
    if np[0] not in range(10) or np[1] not in range(10):
        raise ValueError("cannot move")
    player = np
    return np, get_available_monsters()


def attack_monster(name: str) -> Monster:
    """
    Attack monster with :name:.

    :param name: Name of attacked monster
    :type name: str
    :raises ValueError: Raised if current cell hasn't monster with such name
    :returns: Attacked monster
    :rtype: Monster
    """
    monsters = field[player[0]][player[1]]
    monster = tuple(filter(lambda m: m.name == name, monsters))
    if not monster:
        raise ValueError(f"no {name} here")
    monster = monster[0]
    monster.auch()
    if monster.is_dead():
        monsters.remove(monster)
    return monster
