from app_core.undo_redo_system import UndoRedoSystem


class _Uncopyable:
    def __deepcopy__(self, memo):  # noqa: ANN001 — interfaz estándar de copy
        raise RuntimeError("no copiable")


def test_register_non_deepcopyable_state_fails() -> None:
    sys = UndoRedoSystem(initial_state={})
    assert sys.register_action("bad", _Uncopyable()) is False
    assert sys.get_last_error() is not None
    assert "Estado inválido" in (sys.get_last_error() or "")


def test_undo_redo_basic_flow() -> None:
    sys = UndoRedoSystem(initial_state={"n": 0})
    assert sys.register_action("inc", {"n": 1}) is True
    assert sys.get_current_state() == {"n": 1}
    assert sys.get_history_descriptions() == ["inc"]
    assert sys.undo() is True
    assert sys.get_current_state() == {"n": 0}
    assert sys.redo() is True
    assert sys.get_current_state() == {"n": 1}


def test_undo_when_empty_returns_false() -> None:
    sys = UndoRedoSystem(initial_state=None)
    assert sys.undo() is False
    assert sys.get_last_error() == "No hay acciones para deshacer."


def test_redo_when_empty_returns_false() -> None:
    sys = UndoRedoSystem(initial_state={})
    assert sys.redo() is False
    assert sys.get_last_error() == "No hay acciones para rehacer."


def test_register_empty_description_fails() -> None:
    sys = UndoRedoSystem(initial_state={})
    assert sys.register_action("", {"x": 1}) is False
    assert sys.register_action("   ", {"x": 1}) is False
    assert sys.get_history_descriptions() == []


def test_new_action_clears_redo_stack() -> None:
    sys = UndoRedoSystem(initial_state={"v": 0})
    assert sys.register_action("a1", {"v": 1}) is True
    assert sys.undo() is True
    assert sys.redo() is True
    assert sys.get_current_state() == {"v": 1}
    assert sys.register_action("a2", {"v": 2}) is True
    assert sys.redo() is False
    assert sys.get_last_error() == "No hay acciones para rehacer."


def test_state_snapshots_independent() -> None:
    sys = UndoRedoSystem(initial_state={"items": [1]})
    shared: dict = {"items": [1]}
    assert sys.register_action("mut", shared) is True
    shared["items"].append(2)
    assert sys.get_current_state() == {"items": [1]}
    assert sys.undo() is True
    assert sys.get_current_state() == {"items": [1]}
