"""Класс для отрисовки модели на экране."""
import random
import pygame
from src.models.animation_model import ToothpickModel

class Renderer:
    """Класс Renderer (отрисовка)."""

    def __init__(self, width: int, height: int) -> None:
        """Инициализация рендерера, цветов и параметров камеры."""
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
        
        # Палитра цветов (фиолетовые, пепельные, пурпурные, нежно-розовые, светло-голубые)
        self.palette = [
            (155, 89, 182),   # Фиолетовый
            (149, 165, 166),  # Пепельный
            (192, 57, 43),    # Пурпурный (темный)
            (255, 182, 193),  # Нежно-розовый
            (174, 214, 241),  # Светло-голубой
            (142, 68, 173),   # Аметистовый
        ]
        
        # Автоматический зум
        self.scale = 20.0
        self.min_scale = 2.0
        
        # Отслеживание отрисованных элементов для оптимизации
        self.drawn_count = 0

    def reset(self) -> None:
        """Сброс параметров рендерера."""
        self.scale = 20.0
        self.drawn_count = 0

    def draw(self, screen: pygame.Surface, model: ToothpickModel) -> None:
        """Отрисовка текущего состояния модели.

        Args:
            screen (pygame.Surface): Поверхность для отрисовки.
            model (ToothpickModel): Модель данных.
        """
        # Нежно-розовый фон
        screen.fill((255, 240, 245))

        # Автоматический зум: уменьшаем масштаб по мере роста фрактала
        if len(model.toothpicks) > 0:
            target_scale = max(self.min_scale, 800.0 / (len(model.toothpicks) ** 0.5))
            self.scale += (target_scale - self.scale) * 0.05

        # Отрисовка только новых элементов (для анимации появления)
        # Для простоты каждый кадр перерисовываем всё, но цвета берем из палитры случайно
        for i, (x, y, orient) in enumerate(model.toothpicks):
            # Преобразование координат модели в экранные
            screen_x = int(self.center_x + x * self.scale)
            screen_y = int(self.center_y + y * self.scale)
            
            length = int(self.scale * 0.9)
            if length < 2:
                length = 2
                
            # Выбираем цвет для каждой зубочистки
            color = self.palette[i % len(self.palette)]
            
            if orient == 0:  # Горизонтальная
                rect = pygame.Rect(screen_x - length // 2, screen_y - 2, length, 4)
            else:            # Вертикальная
                rect = pygame.Rect(screen_x - 2, screen_y - length // 2, 4, length)
                
            pygame.draw.rect(screen, color, rect)