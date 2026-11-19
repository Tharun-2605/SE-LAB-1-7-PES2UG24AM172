class AI:
    def __init__(self, size=6):
        self.size = size
        self.tried = set()
        self.targets = []

    def choose(self):
        # First use cells next to previous hits
        while self.targets:
            pos = self.targets.pop(0)

            if pos not in self.tried and self._valid(pos):
                self.tried.add(pos)
                return pos

        # Otherwise choose any untried cell
        options = [
            (r, c)
            for r in range(self.size)
            for c in range(self.size)
            if (r, c) not in self.tried
        ]

        if not options:
            return None

        pos = options[0]
        self.tried.add(pos)
        return pos

    def record_hit(self, pos):
        r, c = pos

        neighbours = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1)
        ]

        for neighbour in neighbours:
            if self._valid(neighbour) and neighbour not in self.tried:
                if neighbour not in self.targets:
                    self.targets.append(neighbour)

    def record_sunk(self):
        self.targets.clear()

    def _valid(self, pos):
        r, c = pos
        return 0 <= r < self.size and 0 <= c < self.size