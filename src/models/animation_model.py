"""Математическая модель фрактала Омара Пола (Toothpick Sequence)."""
import random
from typing import List, Tuple

class ToothpickModel:
    """Класс Model (логика/математика)."""

    def __init__(self) -> None:
        """Инициализация начального состояния фрактала."""
        self.reset()

    def reset(self) -> None:
        """Сброс модели к начальному состоянию (одна зубочистка в центре)."""
        # Зубочистка задается кортежем: (x, y, orientation), где orientation: 0 - горизонт, 1 - вертикаль
        self.toothpicks: List[Tuple[int, int, int]] = [(0, 0, 0)]
        # Множество для быстрой проверки занятых позиций
        self.occupied: set = {(0, 0, 0)}
        self.step = 0

    def update(self) -> None:
        """Выполняет один шаг генерации новых зубочисток."""
        new_toothpicks = []
        step_scale = 1  # Масштаб для координат (можно увеличить для больших шагов)

        for x, y, orient in self.toothpicks:
            # Находим концы текущей зубочистки
            if orient == 0:  # Горизонтальная
                ends = [(x - 1, y), (x + 1, y)]
            else:            # Вертикальная
                ends = [(x, y - 1), (x, y + 1)]

            for ex, ey in ends:
                # Проверяем, свободен ли конец
                is_free = True
                for tx, ty, to in self.occupied:
                    if (tx == ex and ty == ey):
                        is_free = False
                        break
                    # Если конец совпадает с другим концом зубочистки (перекрестие)
                    if orient == 0:
                        if to == 1 and tx == ex and ty == ey:
                            is_free = False
                    else:
                        if to == 0 and tx == ex and ty == ey:
                            is_free = False
                
                # В простой модели проверка на пересечение концов упрощена
                if is_free:
                    # Создаем новую зубочистку, перпендикулярную текущей
                    new_orient = 1 - orient
                    new_tp = (ex, ey, new_orient)
                    new_toothpicks.append(new_tp)
                    self.occupied.add(new_tp)

        # Добавляем новые зубочистки к общему списку
        self.toothpicks.extend(new_toothpicks)
        self.step += 1