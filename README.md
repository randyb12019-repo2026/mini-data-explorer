# mini-data-explorer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mini-data-explorer-rb.streamlit.app)

App en Streamlit para explorar visualmente cualquier archivo CSV de forma interactiva.

## Funcionalidades

- **Carga de CSV** — Sube tu propio archivo o usa el dataset de ejemplo (canciones)
- **Métricas** — Filas, columnas y valores nulos
- **Vista previa** — Primeras 10 filas del dataset
- **Estadísticas descriptivas** — Resumen numérico con `df.describe()`
- **Gráfico interactivo** — Distribución de variable numérica o frecuencia de categórica
- **Mapa de correlación** — Heatmap de correlaciones entre columnas numéricas (opcional)

## Stack

| Tecnología | Uso |
|------------|-----|
| Python | Lenguaje |
| Streamlit | UI y visualización |
| Pandas | Manipulación de datos |
| Seaborn / Matplotlib | Gráficos y heatmap |

## Instalación

```bash
git clone https://github.com/randyb12019-repo2026/mini-data-explorer.git
cd mini-data-explorer
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Docker

```bash
docker build -t mini-data-explorer .
docker run -p 8501:8501 mini-data-explorer
```

## Licencia

MIT — ver [LICENSE](./LICENSE).

## Autor

Randy Bonucci — Proyecto educativo, Bootcamp Data & IA
 