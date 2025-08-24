from __future__ import annotations

import sys
import tkinter as tk
from tkinter import ttk

APP_TITLE = "Cursor Tracker"
BG = "#1e1e1e"
FG = "#dddddd"
ACCENT = "#0e639c"


class CursorTrackerApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title(APP_TITLE)
        self.configure(bg=BG)
        self.resizable(False, False)
        self.geometry("+60+60")

        self._topmost = tk.BooleanVar(value=True)
        self.attributes("-topmost", True)

        self._build_ui()

        self._running = True
        self._poll_interval_ms = 50
        self.after(self._poll_interval_ms, self._tick)

        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _build_ui(self) -> None:
        try:
            self.iconbitmap(default=None)
        except Exception:
            pass

        container = ttk.Frame(self, padding=(10, 10, 10, 8))
        container.pack(fill=tk.BOTH, expand=True)

        s = ttk.Style(self)
        s.theme_use(s.theme_use())
        s.configure("TFrame", background=BG)
        s.configure("TLabel", background=BG, foreground=FG)
        s.configure("TCheckbutton", background=BG, foreground=FG)

        self.coords_var = tk.StringVar(value="X: 0   Y: 0")
        self.coords_lbl = ttk.Label(container, textvariable=self.coords_var, font=("Segoe UI", 14, "bold"))
        self.coords_lbl.grid(row=0, column=0, columnspan=2, sticky="w")

        self.topmost_chk = ttk.Checkbutton(
            container,
            text="Always on top",
            variable=self._topmost,
            command=self._apply_topmost,
        )
        self.topmost_chk.grid(row=1, column=0, sticky="w", pady=(8, 0))

        self.quit_btn = ttk.Button(container, text="Close", command=self._on_close)
        self.quit_btn.grid(row=1, column=1, sticky="e", pady=(8, 0))

        for i in range(2):
            container.columnconfigure(i, weight=1)

    def _apply_topmost(self) -> None:
        try:
            self.attributes("-topmost", bool(self._topmost.get()))
        except Exception:
            pass

    def _tick(self) -> None:
        if not self._running:
            return
        try:
            x = self.winfo_pointerx()
            y = self.winfo_pointery()
            self.coords_var.set(f"X: {x}   Y: {y}")
        except Exception:
            pass
        finally:
            self.after(self._poll_interval_ms, self._tick)

    def _on_close(self) -> None:
        self._running = False
        self.destroy()


def main() -> int:
    app = CursorTrackerApp()
    app.mainloop()
    return 0


if __name__ == "__main__":
    sys.exit(main())
