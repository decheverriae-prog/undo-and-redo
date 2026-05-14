from __future__ import annotations

import copy
from dataclasses import dataclass
from typing import Any

from app_core.deque import Deque


@dataclass(frozen=True, slots=True)
class Action:
    """Una acción registrada: descripción y transición de estado."""

    description: str
    state_before: Any
    state_after: Any


class UndoRedoSystem:
    """
    Historial de acciones y estado actual usando dos Deques:
    - undo_stack: acciones aplicadas (más reciente al final)
    - redo_stack: acciones deshechas listas para rehacer
    """

    __slots__ = ("_undo_stack", "_redo_stack", "_current_state", "_last_error")

    def __init__(self, initial_state: Any = None) -> None:
        self._undo_stack = Deque()
        self._redo_stack = Deque()
        self._current_state = copy.deepcopy(initial_state)
        self._last_error: str | None = None

    def _set_error(self, message: str) -> bool:
        self._last_error = message
        return False

    def get_last_error(self) -> str | None:
        return self._last_error

    def get_current_state(self) -> Any:
        return copy.deepcopy(self._current_state)

    def get_history_descriptions(self) -> list[str]:
        """Historial de acciones aplicadas, de la más antigua a la más reciente."""
        return [a.description for a in self._undo_stack]

    def register_action(self, description: str, new_state: Any) -> bool:
        self._last_error = None
        if description is None or not str(description).strip():
            return self._set_error("La descripción de la acción no puede estar vacía.")
        try:
            state_after = copy.deepcopy(new_state)
        except Exception as exc:  # noqa: BLE001 — estados arbitrarios del usuario
            return self._set_error(f"Estado inválido o no copiable: {exc}")

        action = Action(
            description=str(description).strip(),
            state_before=copy.deepcopy(self._current_state),
            state_after=state_after,
        )
        self._undo_stack.add_rear(action)
        self._current_state = state_after
        self._redo_stack.clear()
        return True

    def undo(self) -> bool:
        self._last_error = None
        if self._undo_stack.is_empty():
            return self._set_error("No hay acciones para deshacer.")
        action = self._undo_stack.remove_rear()
        self._redo_stack.add_rear(action)
        self._current_state = copy.deepcopy(action.state_before)
        return True

    def redo(self) -> bool:
        self._last_error = None
        if self._redo_stack.is_empty():
            return self._set_error("No hay acciones para rehacer.")
        action = self._redo_stack.remove_rear()
        self._undo_stack.add_rear(action)
        self._current_state = copy.deepcopy(action.state_after)
        return True
