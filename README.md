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

El texto listo para copiar al entregable en PDF está en [`docs/INFORME_PDF.md`](docs/INFORME_PDF.md). Complete el **enlace de Google Drive** del video y exporte a PDF; el enlace de GitHub ya figura allí y en este README (ajústelo si el nombre del repo en GitHub no coincide con `deshacer-y-rehacer`).

## Publicar en GitHub

1. Inicie sesión en GitHub con la cuenta correcta.
2. **Cree el repositorio vacío** en la web: **New repository** → nombre `deshacer-y-rehacer` → **Public** → **sin** marcar “Add a README” (el proyecto ya trae archivos).
3. Compruebe en el navegador que abre sin error:  
   `https://github.com/TU_USUARIO/deshacer-y-rehacer`  
   Si da **404**, el repo **aún no existe** o el **usuario** no coincide con `TU_USUARIO`.
4. En la carpeta del proyecto:

```powershell
git remote set-url origin https://github.com/TU_USUARIO/deshacer-y-rehacer.git
git push -u origin main
```

(Sustituya `TU_USUARIO` por su nombre de usuario real de GitHub.)

### Si aparece *Repository not found*

- El repositorio **no se ha creado** en esa cuenta, o el nombre/usuario está **mal escrito** (GitHub distingue mayúsculas solo en la URL mostrada; lo importante es que usuario y repo existan).
- Está intentando subir a **otra cuenta** distinta de la que tiene abierta en el navegador al crear el repo.
- Corrija el remoto: `git remote set-url origin https://github.com/USUARIO_CORRECTO/NOMBRE_REPO.git` y vuelva a hacer `git push -u origin main`.
