# Entregable en PDF — *Undo and redo* (Deque propia)

Use este archivo como **contenido del PDF** que entregan. Complete solo lo marcado con *[…]* y el enlace del video; el resto puede copiarse tal cual.

---

## Checklist: qué debe llevar el PDF (según consigna)

| # | Requisito | Dónde está en este documento |
|---|-------------|--------------------------------|
| **1** | Descripción breve: qué hace el programa, uso de **Deque**, cómo se resolvió **undo/redo**, consola o **GUI**, **validaciones** | Sección **1** más abajo |
| **2** | **Link** a video en **Google Drive** (máx. **3 min**), código + ejecución, permiso de **lectura** | Sección **2** (pegue su URL) |
| **3** | **Link** a repositorio **público** GitHub con código, **README** e instrucciones, **pruebas mínimas** | Sección **3** (enlace ya indicado) |

**Datos de portada (complételos arriba del PDF):**

- **Autor(es):** *[Indique nombres completos]*  
- **Asignatura / fecha:** *[Indique]*  

---

## 1) Descripción breve

### ¿Qué hace el programa?

Es una aplicación de **escritorio** que simula un editor con **historial de cambios**: el usuario registra acciones (cada una con una **descripción** y un **nuevo estado** en texto plano), puede **deshacer** y **rehacer** esos cambios, y ver el **historial de descripciones** y el **estado actual**. Toda la lógica está en la clase `UndoRedoSystem` (`app_core/undo_redo_system.py`); la interfaz (`ui/tkinter_app.py`) solo muestra datos y llama a esa clase.

### ¿Cómo se utilizó la estructura Deque?

Se implementó la clase **`Deque`** en `app_core/deque.py`, con una **lista interna** y los métodos requeridos: `add_front`, `add_rear`, `remove_front`, `remove_rear`, `is_empty`, `size` (y `clear` donde hace falta). **No** se usa `collections.deque` ni otra cola prefabricada para sustituir esa lógica.

En `UndoRedoSystem` hay **dos instancias de `Deque`**:

- **`_undo_stack`**: acciones ya aplicadas; la más reciente está al **final** (`add_rear` al registrar, `remove_rear` al deshacer).
- **`_redo_stack`**: acciones deshechas, listas para rehacer (`add_rear` al deshacer, `remove_rear` al rehacer).

Cada `Deque` se usa como **pila (LIFO)** por el extremo trasero, cumpliendo el requisito de estructura propia.

### ¿Cómo se resolvió undo y redo?

Cada registro es un objeto **`Action`**: descripción, **estado anterior** y **estado posterior** (con `copy.deepcopy`).

- **Registrar:** validación de descripción y estado; se crea `Action`; `add_rear` en `_undo_stack`; estado actual = nuevo estado; `_redo_stack.clear()`.
- **Undo:** si la pila undo está vacía, error; si no, `remove_rear`, `add_rear` en redo, estado actual = `state_before`.
- **Redo:** si la pila redo está vacía, error; si no, se recupera la acción, vuelve a undo y el estado = `state_after`.

### ¿Consola o interfaz gráfica?

**Interfaz gráfica con Tkinter**: campos de texto, botones **Registrar acción**, **Undo** y **Redo**, y áreas de historial y estado actual.

### ¿Qué validaciones se implementaron?

- **Undo** sin historial: `False` y mensaje *"No hay acciones para deshacer."*
- **Redo** sin pila redo: `False` y *"No hay acciones para rehacer."*
- **Descripción** vacía o solo espacios: registro rechazado.
- **Estado no copiable** (`deepcopy` falla): registro rechazado con mensaje de causa.
- Tras **nueva acción**, se limpia redo para evitar estado incoherente.
- En la UI: **messagebox** y **etiqueta de estado** para errores o avisos.

---

## 2) Link a video en Google Drive

**Requisitos del video:** máximo **3 minutos**; debe verse **código** y **ejecución** de la aplicación; enlace con permiso de **lectura** para quien califique.

**Su enlace (complételo después de subir el video a Drive):**

- **Video:** *[PEGUE AQUÍ EL ENLACE DE GOOGLE DRIVE — “Cualquier persona con el enlace” como lector]*

*Cómo compartir en Drive:* archivo → **Compartir** / clic derecho → **Obtener enlace** → acceso **Lector** para “Cualquier persona con el enlace” (o lo que pida su docente).

---

## 3) Link a repositorio público de GitHub

**Contenido del repositorio (cumplimiento):**

- **Código fuente:** `app_core/` (Deque + `UndoRedoSystem`), `ui/`, `main.py`
- **README** con instrucciones: `README.md` en la raíz
- **Pruebas mínimas:** carpeta `tests/` (`test_deque.py`, `test_undo_redo_system.py`), ejecutables con `pytest`

**Enlace al repositorio:**

- **Repositorio:** https://github.com/decheverriae-prog/undo-and-redo  

---

## Cómo generar el archivo PDF

1. Abra este archivo (`docs/INFORME_PDF.md`) en **Word**, **Google Docs**, **Typora** o **VS Code**.
2. Rellene **autores**, **asignatura/fecha** y el **enlace del video** (sección 2).
3. **Exporte o guarde como PDF**  
   - Word: *Archivo → Guardar como → PDF*  
   - Navegador / Docs: *Descargar como PDF*  
   - Windows: *Imprimir → Microsoft Print to PDF*

**Con Pandoc (opcional):** desde la carpeta `docs/`, si tiene Pandoc instalado:  
`pandoc INFORME_PDF.md -o informe_entrega.pdf`
