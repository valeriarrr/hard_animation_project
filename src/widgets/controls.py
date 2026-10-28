"""Виджеты интерфейса."""
import tkinter as tk


class OvalButton(tk.Canvas):
    """Кнопка-капсула с закруглёнными углами."""

    def __init__(self, master, text, command,
                 width=150, height=52,
                 bg="#e8b8ce", hover="#dba3bd",
                 text_color="#7a3d57",
                 master_bg="#fdf6f8", **kwargs):
        super().__init__(master, width=width, height=height,
                         highlightthickness=0, bd=0, bg=master_bg,
                         **kwargs)
        self.command = command
        self._bg = bg
        self._hover = hover
        self._fg = text_color
        self._cw = width
        self._ch = height
        self._build(text)

    def _build(self, text):
        """Нарисовать кнопку."""
        r = self._ch / 2
        points = [
            r, 1, self._cw - r, 1, self._cw - 1, r,
            self._cw - 1, self._ch - r, self._cw - r, self._ch - 1,
            r, self._ch - 1, 1, self._ch - r, 1, r
        ]
        self.create_polygon(points, smooth=True, fill=self._bg,
                            outline="", tags="oval")
        self.create_text(self._cw / 2, self._ch / 2, text=text,
                         fill=self._fg, font=("Segoe UI", 12, "bold"),
                         tags="label")
        for tag in ("oval", "label"):
            self.tag_bind(tag, "<Button-1>", lambda e: self.command())
            self.tag_bind(tag, "<Enter>",
                          lambda e: self.itemconfigure("oval", fill=self._hover))
            self.tag_bind(tag, "<Leave>",
                          lambda e: self.itemconfigure("oval", fill=self._bg))
        self.configure(cursor="hand2")
