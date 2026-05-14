"""Interfaz Tkinter que delega toda la lógica en UndoRedoSystem."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk

from app_core.undo_redo_system import UndoRedoSystem


def _read_plain_state(widget: scrolledtext.ScrolledText) -> str:
    """Estado = contenido del área de texto, sin el salto final que añade Tk."""
    return widget.get("1.0", "end-1c")


class UndoRedoTkApp:
    def __init__(self) -> None:
        self._system = UndoRedoSystem(initial_state="")
        self._root = tk.Tk()
        self._root.title("Undo and redo — custom Deque")
        self._root.minsize(640, 480)

        main = ttk.Frame(self._root, padding=10)
        main.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main, text="Descripción de la acción").grid(row=0, column=0, sticky=tk.W)
        self._desc = ttk.Entry(main, width=50)
        self._desc.grid(row=1, column=0, columnspan=2, sticky=tk.EW, pady=(0, 6))

        ttk.Label(main, text="Nuevo estado (texto plano)").grid(row=2, column=0, sticky=tk.W)
        self._state_input = scrolledtext.ScrolledText(main, height=6, wrap=tk.WORD)
        self._state_input.grid(row=3, column=0, columnspan=2, sticky=tk.NSEW, pady=(0, 6))
        self._state_input.insert("1.0", "")

        btn_row = ttk.Frame(main)
        btn_row.grid(row=4, column=0, columnspan=2, pady=6)
        ttk.Button(btn_row, text="Registrar acción", command=self._on_register).pack(
            side=tk.LEFT, padx=(0, 6)
        )
        ttk.Button(btn_row, text="Undo", command=self._on_undo).pack(side=tk.LEFT, padx=(0, 6))
        ttk.Button(btn_row, text="Redo", command=self._on_redo).pack(side=tk.LEFT)

        ttk.Label(main, text="Historial (más antiguo → más reciente)").grid(
            row=5, column=0, sticky=tk.W, pady=(8, 0)
        )
        self._history = scrolledtext.ScrolledText(main, height=8, state=tk.DISABLED, wrap=tk.WORD)
        self._history.grid(row=6, column=0, sticky=tk.NSEW, pady=(0, 6))

        ttk.Label(main, text="Estado actual").grid(row=7, column=0, sticky=tk.W)
        self._current = scrolledtext.ScrolledText(main, height=8, state=tk.DISABLED, wrap=tk.WORD)
        self._current.grid(row=8, column=0, sticky=tk.NSEW)

        self._status = ttk.Label(main, text="", foreground="#555")
        self._status.grid(row=9, column=0, columnspan=2, sticky=tk.W, pady=(8, 0))

        main.columnconfigure(0, weight=1)
        main.rowconfigure(3, weight=1)
        main.rowconfigure(6, weight=1)
        main.rowconfigure(8, weight=1)

        self._refresh_views()

    def _set_status(self, ok: bool, msg: str | None) -> None:
        if ok:
            self._status.configure(text="OK", foreground="green")
        else:
            self._status.configure(text=msg or "Error", foreground="red")

    def _write_disabled(self, widget: scrolledtext.ScrolledText, text: str) -> None:
        widget.configure(state=tk.NORMAL)
        widget.delete("1.0", tk.END)
        widget.insert("1.0", text)
        widget.configure(state=tk.DISABLED)

    def _format_state_for_display(self, state: object) -> str:
        if isinstance(state, str):
            return state
        return repr(state)

    def _sync_state_input_from_system(self) -> None:
        text = self._format_state_for_display(self._system.get_current_state())
        self._state_input.delete("1.0", tk.END)
        self._state_input.insert("1.0", text)

    def _refresh_views(self) -> None:
        hist = self._system.get_history_descriptions()
        self._write_disabled(self._history, "\n".join(hist) if hist else "(vacío)")
        state = self._system.get_current_state()
        self._write_disabled(self._current, self._format_state_for_display(state))
        self._sync_state_input_from_system()

    def _on_register(self) -> None:
        desc = self._desc.get()
        new_state = _read_plain_state(self._state_input)
        ok = self._system.register_action(desc, new_state)
        if not ok:
            messagebox.showwarning("No se pudo registrar", self._system.get_last_error() or "")
            self._set_status(False, self._system.get_last_error())
        else:
            self._set_status(True, None)
        self._refresh_views()

    def _on_undo(self) -> None:
        ok = self._system.undo()
        if not ok:
            messagebox.showinfo("Undo", self._system.get_last_error() or "")
            self._set_status(False, self._system.get_last_error())
        else:
            self._set_status(True, None)
        self._refresh_views()

    def _on_redo(self) -> None:
        ok = self._system.redo()
        if not ok:
            messagebox.showinfo("Redo", self._system.get_last_error() or "")
            self._set_status(False, self._system.get_last_error())
        else:
            self._set_status(True, None)
        self._refresh_views()

    def run(self) -> None:
        self._root.mainloop()


def main() -> None:
    UndoRedoTkApp().run()


if __name__ == "__main__":
    main()
