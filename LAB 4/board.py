class Board:
    SIZE = 6

    def __init__(self):
        self.ships = []
        self.shots = set()

    def place_ship(self, cells):
        ship = {
            "cells": set(cells),
            "hits": set()
        }
        self.ships.append(ship)

    def fire(self, pos):
        if pos in self.shots:
            return "already"

        self.shots.add(pos)

        for ship in self.ships:
            if pos in ship["cells"]:
                ship["hits"].add(pos)

                if ship["hits"] == ship["cells"]:
                    return "sunk"

                return "hit"

        return "miss"

    def all_sunk(self):
        return all(ship["hits"] == ship["cells"] for ship in self.ships)

    def ship_sunk(self, pos):
        for ship in self.ships:
            if pos in ship["cells"]:
                return ship["hits"] == ship["cells"]

        return False