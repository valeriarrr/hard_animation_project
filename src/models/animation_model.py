"""Мат модель фрактала Омара Пола."""


class ToothpickModel:
    """Хранит состояние фрактала и вычисляет новые точки."""

    def __init__(self):
        """Инициализировать модель с центральной точкой."""
        self.step = 0
        self.occupied = {(0, 0)}
        self.active_tips = []

        # Первый шаг - это одна зубочистка от (-1, 0) до (1, 0)
        self._add_toothpick(0, 0, "h")

    def _add_toothpick(self, x, y, direction):
        """Добавить зубочистку в модель и обновить концы."""
        self.occupied.add((x, y))
        if direction == "h":
            self.occupied.add((x - 1, y))
            self.occupied.add((x + 1, y))
            self.active_tips.append((x - 1, y, "v"))
            self.active_tips.append((x + 1, y, "v"))
        else:
            self.occupied.add((x, y - 1))
            self.occupied.add((x, y + 1))
            self.active_tips.append((x, y - 1, "h"))
            self.active_tips.append((x, y + 1, "h"))

    def next_step(self):
        """Выполнить один шаг эволюции фрактала."""
        new_tips = []
        for x, y, direction in self.active_tips:
            if direction == "h":
                if (x - 1, y) not in self.occupied and \
                        (x + 1, y) not in self.occupied:
                    self._add_toothpick(x, y, "h")
                    new_tips.append((x - 1, y, "v"))
                    new_tips.append((x + 1, y, "v"))
            else:
                if (x, y - 1) not in self.occupied and \
                        (x, y + 1) not in self.occupied:
                    self._add_toothpick(x, y, "v")
                    new_tips.append((x, y - 1, "h"))
                    new_tips.append((x, y + 1, "h"))

        self.active_tips = new_tips
        self.step += 1
