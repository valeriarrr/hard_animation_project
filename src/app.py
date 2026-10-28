"""Главный класс приложения, управляющий окном и циклом."""
import pygame
from src.models.animation_model import ToothpickModel
from src.renderers.renderer import Renderer
from src.widgets.controls import Controls

class App:
    """Класс App (окно, главный цикл)."""

    def __init__(self) -> None:
        """Инициализация окна, модели и рендерера."""
        pygame.init()
        self.width = 1000
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Фрактал Омара Пола (Toothpick Sequence)")
        self.clock = pygame.time.Clock()
        
        self.model = ToothpickModel()
        self.renderer = Renderer(self.width, self.height)
        self.controls = Controls()
        
        self.running = True
        self.paused = False

    def run(self) -> None:
        """Главный цикл приложения."""
        while self.running:
            self._handle_events()
            
            if not self.paused:
                self.model.update()
                
            self.renderer.draw(self.screen, self.model)
            self.controls.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(60)  # 60 FPS

        pygame.quit()

    def _handle_events(self) -> None:
        """Обработка событий клавиатуры и закрытия окна."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_r:
                    self.model.reset()
                    self.renderer.reset()