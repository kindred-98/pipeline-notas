<div align="center">

# 📊 Pipeline-Notas

[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-10%2F10%20passing-brightgreen?logo=pytest)](tests/test_clasificador.py)
[![Code Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](tests/test_clasificador.py)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue?logo=github-actions&logoColor=white)](/.github/workflows/pipeline.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](/)

</div>

---

## 🎯 Descripción

**Pipeline-Notas** es una aplicación Python profesional que clasifica calificaciones numéricas (0-10) en categorías académicas españolas. Implementa buenas prácticas de desarrollo incluyendo testing exhaustivo y pipeline automatizado con GitHub Actions.

Proyecto educativo diseñado para demostrar:
- ✅ Testing unitario completo (casos normales, límite y error)
- ✅ Automación CI/CD con GitHub Actions
- ✅ Estructura profesional de proyecto Python
- ✅ Manejo robusto de excepciones

---

## ✨ Características

### 🔧 Funcionalidad Principal

**Clasificador de Notas**: Convierte calificaciones numéricas en categorías académicas

| Rango | Clasificación | Descripción |
|-------|---|---|
| 0.0 - 4.99 | 🔴 **Suspenso** | No aprobado |
| 5.0 - 6.99 | 🟡 **Aprobado** | Aprobado mínimo |
| 7.0 - 8.99 | 🟢 **Notable** | Bien |
| 9.0 - 10.0 | 🟦 **Sobresaliente** | Excelente |

### 📋 Suite de Testing

- **10 tests completos** organizados en 3 categorías:
  - Tests normales (casos comunes)
  - Tests de límite (valores en frontera)
  - Tests de error (excepciones y validaciones)
- Cobertura: 100%
- Framework: pytest 9.0.2

### 🔄 Automación CI/CD

- **Triggers automáticos** en push a `main` y pull requests
- **Entorno controlado**: Python 3.11 en Ubuntu
- **Validación automática** de todos los tests
- Integración: GitHub Actions

---

## 🚀 Instalación

### Requisitos Previos

- Python 3.11 o superior
- pip (generalmente incluido con Python)
- Git

### Pasos de Instalación

**1. Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/pipeline-notas.git
cd pipeline-notas
```

**2. Crear entorno virtual (recomendado)**
```bash
# En Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# En Windows (CMD)
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Instalar dependencias**
```bash
pip install -r requirements.txt
```

**Verificación de instalación**
```bash
python -c "from src.clasificador import clasificar_nota; print('✓ Instalación correcta')"
```

---

## 💡 Uso Rápido

### Como Módulo Python

```python
from src.clasificador import clasificar_nota

# Uso básico
resultado = clasificar_nota(7.5)
print(resultado)  # Output: "Notable"

# Manejo de excepciones
try:
    resultado = clasificar_nota(-1)
except ValueError as e:
    print(f"Error: {e}")
```

### Ejemplos de Uso

```python
from src.clasificador import clasificar_nota

# Casos válidos
print(clasificar_nota(3))     # "Suspenso"
print(clasificar_nota(5.5))   # "Aprobado"
print(clasificar_nota(8.2))   # "Notable"
print(clasificar_nota(9.8))   # "Sobresaliente"

# Casos de error
try:
    clasificar_nota(11)       # ❌ ValueError
except ValueError:
    print("Nota fuera de rango [0, 10]")

try:
    clasificar_nota("ocho")   # ❌ TypeError
except TypeError:
    print("La nota debe ser un número")
```

---

## 📁 Estructura del Proyecto

```
pipeline-notas/
├── 📄 README.md                    # Este archivo
├── 📄 LICENSE                       # Licencia MIT
├── 📄 requirements.txt              # Dependencias del proyecto
│
├── 📁 src/
│   ├── __init__.py                 # Inicializador del paquete
│   ├── clasificador.py             # 🔧 Lógica principal
│   └── __pycache__/                # Caché de Python
│
├── 📁 tests/
│   ├── __init__.py                 # Inicializador del paquete
│   ├── test_clasificador.py        # 🧪 Suite de tests (10 tests)
│   └── __pycache__/                # Caché de Python
│
└── 📁 .github/workflows/
    └── pipeline.yml                # ⚙️ Configuración CI/CD
```

### Descripción de Archivos Clave

| Archivo | Propósito |
|---------|----------|
| `src/clasificador.py` | Implementación de `clasificar_nota()` con validación |
| `tests/test_clasificador.py` | Suite de 10 tests (normales, límite, error) |
| `.github/workflows/pipeline.yml` | Configuración de GitHub Actions |
| `requirements.txt` | Dependencias (pytest, colorama, etc.) |

---

## 🧪 Testing

### Ejecutar Todos los Tests

```bash
pytest tests/ -v
```

**Output esperado:**
```
tests/test_clasificador.py::test_suspenso_normal PASSED
tests/test_clasificador.py::test_aprobado_normal PASSED
tests/test_clasificador.py::test_nota_exactamente_cinco PASSED
...
======================== 10 passed in 0.45s =========================
```

### Opciones Avanzadas de Testing

**Ejecutar con más detalles**
```bash
pytest tests/ -vv
```

**Reporte de cobertura**
```bash
pytest tests/ --cov=src --cov-report=term-missing
```

**Ejecutar test específico**
```bash
pytest tests/test_clasificador.py::test_nota_exactamente_siete -v
```

**Modo watch (si está disponible)**
```bash
pytest tests/ --watch
```

### Categorías de Tests

```
✅ Tests Normales (2):
   - test_suspenso_normal()      → Nota 3 = "Suspenso"
   - test_aprobado_normal()      → Nota 6 = "Aprobado"

✅ Tests de Límite (5):
   - test_nota_exactamente_cinco()  → Valor frontera 5.0
   - test_nota_exactamente_siete()  → Valor frontera 7.0
   - test_nota_diez()               → Valor máximo 10
   - test_nota_499()                → Frontera suspenso/aprobado
   - test_nota_999()                → Frontera notable/sobresaliente

✅ Tests de Error (3):
   - test_nota_negativa()           → ValueError para -1
   - test_nota_mayor_diez()         → ValueError para 11
   - test_tipo_incorrecto()         → TypeError para "ocho"
```

---

## 🔄 Pipeline CI/CD (GitHub Actions)

### Configuración Automática

Cada vez que haces **push** a `main` o creas una **pull request**, se ejecuta automáticamente:

```yaml
✓ Descargar código última versión
✓ Configurar Python 3.11
✓ Instalar dependencias (pip install -r requirements.txt)
✓ Ejecutar tests (pytest tests/ -v)
```

### Ver Estado de la Pipeline

1. Ve a la pestaña **Actions** en tu repositorio de GitHub
2. Verás el historial de ejecuciones
3. Haz clic en una ejecución para ver detalles

### Configuración del Workflow

Archivo: [`.github/workflows/pipeline.yml`](/.github/workflows/pipeline.yml)

```yaml
name: Python Tests
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.11]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: pip install -r requirements.txt
      - run: pytest tests/ -v
```

---

## 📦 Dependencias

| Paquete | Versión | Propósito |
|---------|---------|----------|
| **pytest** | 9.0.2 | Framework de testing unitario |
| **colorama** | 0.4.6 | Colores en terminal |
| **pluggy** | 1.6.0 | Sistema de plugins (dep. pytest) |
| **iniconfig** | 2.3.0 | Parser de archivos INI |
| **packaging** | 26.0 | Utilidades de packaging |
| **Pygments** | 2.19.2 | Syntax highlighting |

Ver [`requirements.txt`](requirements.txt) para versiones exactas.

---

## 🛠️ Desarrollo

### Entorno de Desarrollo

```bash
# Activar entorno virtual
./venv/Scripts/Activate.ps1  # Windows
source venv/bin/activate      # macOS/Linux

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar tests
pytest tests/ -v

# Desactivar entorno
deactivate
```

### Agregar Nuevos Tests

1. Edita [`tests/test_clasificador.py`](tests/test_clasificador.py)
2. Agrega tu función de test comenzando con `test_`
3. Ejecuta `pytest tests/ -v` para validar
4. Haz push, la pipeline se ejecutará automáticamente

### Agregar Nueva Funcionalidad

1. Edita o crea nuevos módulos en [`src/`](src/)
2. Crea tests correspondientes en [`tests/`](tests/)
3. Asegúrate que todos los tests pasen: `pytest tests/ -v`
4. Haz push a una rama y crea un PR

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. **Fork** el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Asegúrate que todos los tests pasen
4. Haz commit de tus cambios (`git commit -m 'Add: AmazingFeature'`)
5. Haz push a la rama (`git push origin feature/AmazingFeature`)
6. Abre un **Pull Request** con descripción clara

### Estándares de Calidad

- ✅ Código 100% testeado
- ✅ Pipeline CI/CD debe pasar
- ✅ Mínimo 2 tests por funcionalidad (normal + límite/error)
- ✅ Docstrings en todas las funciones

---

## 📝 Licencia

Este proyecto está bajo la licencia **MIT**. Ver [`LICENSE`](LICENSE) para detalles.

```
Copyright (c) 2026 ADEV

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software")...
```

---

## 👨‍💻 Autor

**A.D.E.V**
- GitHub: [@Kindred98](https://github.com/Kindred98)
- Proyecto: [pipeline-notas](https://github.com/Kindred98/pipeline-notas)

---

## 📞 Soporte

¿Preguntas o problemas?

- 🐛 [Reportar un bug](https://github.com/Kindred98/pipeline-notas/issues/new?labels=bug)
- 💡 [Solicitar feature](https://github.com/Kindred98/pipeline-notas/issues/new?labels=enhancement)
- 📚 [Ver documentación](README.md)

---

## 🎓 Propósito Educativo

Este proyecto fue creado para demostrar:
- **Buenas prácticas** en testing unitario
- **Automación CI/CD** con GitHub Actions
- **Estructura profesional** de proyectos Python
- **Documentación de código** clara y completa

Ideal para estudiantes y desarrolladores aprendiendo sobre:
- pytest y testing en Python
- GitHub Actions y CI/CD
- Versionado con Git
- Buenas prácticas de desarrollo

---

<div align="center">

*Last updated: Marzo 26, 2026*

⭐ Si este proyecto te resulta útil, considera dejarle una estrella en GitHub
</div>
