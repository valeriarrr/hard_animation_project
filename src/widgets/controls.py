"""Виджеты управления (текстовая информация)."""
import pygame

class Controls:
    """Класс Controls (Слайдеры, кнопки)."""

    def __init__(self) -> None:
        """Инициализация шрифтов."""
        self.font = pygame.font.SysFont("Arial", 18)

    def draw(self, screen: pygame.Surface) -> None:
        """Отрисовка подсказок по управлению.

        Args:
            screen (pygame.Surface): Поверхность для отрисовки.
        """
        text_lines = [
            "Управление:",
            "ESC - Выход",
            "SPACE - Пауза/Продолжить",
            "R - Сброс",
        ]
        
        y_offset = 10
        for line in text_lines:
            text_surf = self.font.render(line, True, (100, 100, 100))
            screen.blit(text_surf, (10, y_offset))
            y_offset += 25