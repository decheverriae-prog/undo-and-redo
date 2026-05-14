"""Deque propia: la lógica usa solo esta API; el almacenamiento interno es una lista."""


class DequeEmptyError(Exception):
    """Se lanza al quitar de una deque vacía (opcional para llamadas internas)."""


class Deque:
    """Cola de doble extremo. Índice 0 = frente, -1 = final."""

    __slots__ = ("_items",)

    def __init__(self) -> None:
        self._items: list[object] = []

    def add_front(self, item: object) -> None:
        self._items.insert(0, item)

    def add_rear(self, item: object) -> None:
        self._items.append(item)

    def remove_front(self) -> object:
        if self.is_empty():
            raise DequeEmptyError("remove_front en deque vacía")
        return self._items.pop(0)

    def remove_rear(self) -> object:
        if self.is_empty():
            raise DequeEmptyError("remove_rear en deque vacía")
        return self._items.pop()

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def clear(self) -> None:
        self._items.clear()

    def __iter__(self):
        """Orden de frente a final (solo lectura sobre copia)."""
        return iter(tuple(self._items))
