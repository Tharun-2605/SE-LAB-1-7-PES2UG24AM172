from board import Board
from ai import AI


class Battleship:
    def __init__(self):
        self.player = Board()
        self.enemy = Board()
        self.ai = AI()

        self._setup()

    def _setup(self):
        self.player.place_ship({
            (1, 1),
            (1, 2),
            (1, 3)
        })

        self.player.place_ship({
            (3, 3),
            (4, 3),
            (5, 3)
        })

        self.enemy.place_ship({
            (2, 2),
            (2, 3),
            (2, 4)
        })

        self.enemy.place_ship({
            (4, 1),
            (5, 1)
        })

    def show(self):
        remaining = 0

        for ship in self.enemy.ships:
            remaining += len(ship["cells"] - ship["hits"])

        print("\nYour shots are coordinates like 2,3.")
        print("Ship cells remaining:", remaining)

    def run(self):
        print("Battleship")

        while True:
            self.show()

            raw = input("> ").strip().lower()

            if raw == "q":
                print("Game ended.")
                return

            try:
                r, c = map(int, raw.split(","))
                pos = (r - 1, c - 1)

            except ValueError:
                print("Use row,col.")
                continue

            if not (
                0 <= pos[0] < Board.SIZE
                and 0 <= pos[1] < Board.SIZE
            ):
                print("Outside board.")
                continue

            result = self.enemy.fire(pos)

            if result == "already":
                print("Already fired there.")
                continue

            if result == "miss":
                print("MISS!")

            elif result == "hit":
                print("HIT!")

            elif result == "sunk":
                print("HIT! You sank a ship.")

            if self.enemy.all_sunk():
                print("You sank the fleet.")
                return

            # -------------------------
            # AI TURN
            # -------------------------

            ai_pos = self.ai.choose()

            if ai_pos is None:
                print("AI has no remaining moves.")
                return

            ar, ac = ai_pos

            display_pos = f"{ar + 1},{ac + 1}"

            print("AI fired at", display_pos)

            ai_result = self.player.fire(ai_pos)

            if ai_result == "already":
                # This should normally never happen because AI
                # keeps track of every coordinate it has tried.
                print("AI selected an already fired cell.")

            elif ai_result == "miss":
                print("AI missed.")

            elif ai_result == "hit":
                print("AI scored a hit.")
                self.ai.record_hit(ai_pos)

            elif ai_result == "sunk":
                print("AI scored a hit and sank your ship.")
                self.ai.record_sunk()

            if self.player.all_sunk():
                print("AI sank your fleet.")
                return