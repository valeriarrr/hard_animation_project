"""Отрисовка фрактала на холсте."""
import tkinter as tk
import random


class FractalRenderer:
    """Рисует зубочистки в виде квадратов."""

    BG_COLOR = "#fdf6f8"
    PALETTE = [
        "#f7e4ec",
        "#e8b8ce",
        "#d9a4b8",
        "#c58fb3",
        "#b389c5",
        "#a98298",
        "#8bb8cc",
    ]

    def __init__(self, canvas):
        """Сохранить ссылку на холст."""
        self.canvas = canvas
        self.size = 4
        self.scale = 1.0

    def draw(self, occupied):
        """Очистить холст и нарисовать все занятые точки."""
        self.canvas.delete("all")

        if not occupied:
            return

        # Границы для центрирования и авто-зума
        xs = [p[0] for p in occupied]
        ys = [p[1] for p in occupied]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)

        # Размеры холста
        cw = self.canvas.winfo_width()
        ch = self.canvas.winfo_height()
        if cw <= 1:
            cw, ch = 800, 600

        # Автоматический зум
        width_span = max(1, max_x - min_x + 1)
        height_span = max(1, max_y - min_y + 1)
        self.scale = min(cw * 0.8 / width_span, ch * 0.8 / height_span)
        self.scale = max(1.0, min(self.scale, 30.0))  # Ограничение

        # Смещение для центрирования
        offset_x = cw / 2 - (min_x + max_x) / 2 * self.scale
        offset_y = ch / 2 - (min_y + max_y) / 2 * self.scale

        size = self.size

        for x, y in occupied:
            color = random.choice(self.PALETTE)

            px = x * self.scale + offset_x
            py = y * self.scale + offset_y

            r = size * self.scale * 0.5

            self.canvas.create_rectangle(
                px - r, py - r, px + r, py + r,
                fill=color, outline=""
            )
