"""Главное окно приложения."""
import tkinter as tk
from tkinter import font as tkfont

from src.models.animation_model import ToothpickModel
from src.renderers.renderer import FractalRenderer
from src.widgets.controls import OvalButton


class App:
    """Управляет окном, анимацией и кнопками."""

    def __init__(self):
        """Создать окно и запустить интерфейс."""
        self.root = tk.Tk()
        self.root.title("Фрактал Омара Пола")
        self.root.geometry("800x600")
        self.root.configure(bg="#fdf6f8")

        self.model = ToothpickModel()
        self.is_animating = False

        self._build_ui()

    def _build_ui(self):
        """Собрать интерфейс."""
        title_font = tkfont.Font(family="Segoe UI Semibold", size=18, weight="bold")
        tk.Label(self.root, text="Фрактал Омара Пола",
                 bg="#fdf6f8", fg="#7a3d57", font=title_font).pack(pady=(15, 5))

        self.canvas = tk.Canvas(self.root, bg="#fdf6f8", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=20, pady=10)

        self.canvas.after(100, lambda: self.renderer.draw(self.model.occupied))

        self.btn = OvalButton(
            self.root, text="Старт / Сброс", command=self.toggle_animation,
            width=160, height=50, master_bg="#fdf6f8"
        )
        self.btn.pack(side="bottom", pady=20)

        self.renderer = FractalRenderer(self.canvas)

    def toggle_animation(self):
        """Запустить или остановить анимацию."""
        if self.is_animating:
            self.is_animating = False
        else:
            self.is_animating = True
            self.animate()

    def animate(self):
        """Выполнять шаги анимации с задержкой."""
        if not self.is_animating:
            return
        if self.model.step >= 50:
            self.is_animating = False
            return

        self.model.next_step()
        self.renderer.draw(self.model.occupied)
        self.root.after(200, self.animate)

    def run(self):
        """Запустить главный цикл."""
        self.root.mainloop()
