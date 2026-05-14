# Deshacer y rehacer

Sistema **Undo / Redo** en Python con **cola de doble extremo (`Deque`) propia**, lógica encapsulada en `UndoRedoSystem` e **interfaz gráfica** con Tkinter. La UI no contiene la lógica principal: solo consume las clases de `app_core`.

**Repositorio en GitHub:** [https://github.com/decheverriae-prog/deshacer-y-rehacer](https://github.com/decheverriae-prog/deshacer-y-rehacer)  
*(Cree el repositorio con ese nombre en la cuenta `decheverriae-prog` y suba este código; si eligió otro slug en GitHub, cambie el enlace en el README y en el PDF.)*

## Requisitos

- Python **3.12+** (probado también en 3.14)
- Tkinter (incluido con la instalación estándar de Python en Windows; en algunas distribuciones Linux puede hacer falta el paquete `python3-tk`)

## Estructura del proyecto

```
app_core/
  deque.py              # Clase Deque (lista interna, API encapsulada)
  undo_redo_system.py   # UndoRedoSystem: historial, estado, undo/redo
ui/
  tkinter_app.py        # Ventana y botones
tests/
  test_deque.py
  test_undo_redo_system.py
main.py                 # Arranque de la aplicación
requirements.txt        # pytest (pruebas)
pytest.ini
```

## Instalación

Desde la raíz del repositorio:

```powershell
py -3 -m pip install -r requirements.txt
```

(Linux/macOS: puede usarse `python3` en lugar de `py -3`.)

## Ejecutar la interfaz gráfica

```powershell
py -3 main.py
```

Equivalente:

```powershell
py -3 -m ui.tkinter_app
```

## Ejecutar las pruebas

```powershell
py -3 -m pytest tests -v
```

## Uso rápido de la aplicación

1. Escriba una **descripción** de la acción.
2. Edite el **nuevo estado** como texto plano en el área correspondiente.
3. Pulse **Registrar acción**.
4. Use **Deshacer** y **Rehacer**; el historial y el estado actual se muestran en pantalla.

## Nota sobre el informe en PDF

El texto listo para copiar al entregable en PDF está en [`docs/INFORME_PDF.md`](docs/INFORME_PDF.md). Complete el **enlace de Google Drive** del video y exporte a PDF; el enlace de GitHub ya figura allí y en este README (ajístelo si el nombre del repo en GitHub no coincide con `deshacer-y-rehacer`).
