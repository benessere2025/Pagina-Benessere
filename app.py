import streamlit as st
from datetime import datetime

# =================== CONFIG ===================
st.set_page_config(page_title="Benessere • Açai sin azúcar", page_icon="🍇", layout="wide")

# Paleta (morado + blanco)
PRIMARY = "#4b1a5a"      # morado principal
PRIMARY_DARK = "#3a1446"  # morado oscuro
TEXT = "#2b2b2b"          # texto
MUTED = "#5a5a5a"

# =================== MENÚ (EDITABLE) ===================
# Cambia estos precios/descripciones cuando quieras
MENU = {
    "Bowls de Açaí": [
        {"Producto": "Bowl Clásico (350 ml)",  "Precio": 4.50, "Incluye": "Açaí sin azúcar, banana, granola sin azúcar"},
        {"Producto": "Bowl Proteico (450 ml)", "Precio": 5.90, "Incluye": "Açaí sin azúcar, proteína veg., mantequilla de maní, chía"},
        {"Producto": "Bowl Benessere (500 ml)","Precio": 6.50, "Incluye": "Açaí sin azúcar, mix de frutas, granola, crema de coco"},
    ],
    "Zumos Naturales": [
        {"Producto": "Maracuyá + Piña (400 ml)", "Precio": 2.80, "Incluye": "Fruta natural, agua filtrada"},
        {"Producto": "Naranja exprimida (400 ml)", "Precio": 3.00, "Incluye": "100% naranja, sin azúcar"},
        {"Producto": "Fresa + Mango (400 ml)",     "Precio": 3.20, "Incluye": "Fruta natural, sin azúcar"},
    ],
    "Cereales / Granolas": [
        {"Producto": "Granola sin azúcar (100 g)",   "Precio": 1.90, "Incluye": "Avena, frutos secos, semillas"},
        {"Producto": "Mix crunchy cacao (100 g)",    "Precio": 2.20, "Incluye": "Cacao puro, avena, almendras"},
    ],
    "Toppings / Extras": [
        {"Producto": "Mantequilla de maní (1 porción)", "Precio": 0.70, "Incluye": ""},
        {"Producto": "Proteína vegana (1 scoop)",       "Precio": 0.90, "Incluye": ""},
        {"Producto": "Fruta extra",                     "Precio": 0.60, "Incluye": ""},
        {"Producto": "Chía / Linaza",                   "Precio": 0.40, "Incluye": ""},
    ],
}

# =================== ESTILOS ===================
CSS = f"""
<style>
:root {{
  --primary: {PRIMARY};
  --primary-dark: {PRIMARY_DARK};
}}
html, body, [class*="st-"] {{
  font-family: Inter, -apple-system, system-ui, "Segoe UI", Roboto, Ubuntu, "Helvetica Neue", Arial;
  color: {TEXT};
}}
/* NAV */
.navbar {{
  position: sticky; top:0; z-index:1000; background:#fff; border-bottom:1px solid #eee;
}}
.nav-inner {{
  max-width:1200px; margin:0 auto; padding:.8rem 1rem;
  display:flex; align-items:center; justify-content:space-between;
}}
.nav-left {{ display:flex; align-items:center; gap:.6rem; }}
.brand {{ color: var(--primary); font-weight: 800; letter-spacing:.2px; }}
.nav-right a {{
  margin-left:1rem; text-decoration:none; color:#444; font-weight:600;
}}
.nav-right a:hover {{ color: var(--primary); }}

/* HERO minimal */
.hero {{ background: var(--primary); color:#fff; }}
.hero-inner {{ max-width:1200px; margin:0 auto; padding:3.2rem 1rem; }}
.hero h1 {{ font-weight:900; margin:0 0 .3rem 0; }}
.hero p {{ opacity:.95; }}

/* Sections */
.section {{ max-width:1200px; margin:0 auto; padding: 2.6rem 1rem; }}
.section h2 {{ color: var(--primary); font-weight:900; margin-bottom:.6rem; }}

/* Table */
.table {{ width:100%; border-collapse:collapse; }}
.table th, .table td {{ padding:.65rem .6rem; border-bottom:1px solid #eee; }}
.table th {{ text-align:left; color:{MUTED}; font-size:.88rem; }}
.table tr:hover td {{ background:#faf8fb; }}

/* Cards resumen */
.card {{
  border:1px solid #eee; border-radius:14px; padding:1rem; background:#fff; text-align:center;
}}
.card .price {{ font-size:1.6rem; font-weight:900; color: var(--primary-dark); }}

/* Footer */
footer {{ background:#fff; border-top:1px solid #eee; }}
.footer-inner {{
  max-width:1200px; margin:0 auto; padding:1rem;
  display:flex; align-items:center; justify-content:space-between; color:#666;
}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# =================== NAVBAR ===================
nav = """
<div class="navbar">
  <div class="nav-inner">
    <div class="nav-left">
      <img src="logo.png" height="26" alt="Benessere"/>
      <span class="brand">Benessere</span>
    </div>
    <div class="nav-right">
      <a href="#sobre-nosotros">Sobre nosotros</a>
      <a href="#menu">Menú</a>
      <a href="#precios">Precios</a>
      <a href="#ubicaciones">Ubicaciones</a>
    </div>
  </div>
</div>
"""
st.markdown(nav, unsafe_allow_html=True)

# =================== HERO ===================
st.markdown(
    """
<div class="hero">
  <div class="hero-inner">
    <h1>Açai sin azúcar, sin rodeos</h1>
    <p>Snacks limpios, simples y rápidos para tu campus. Carta clara, sin imágenes ruidosas ni formularios.</p>
  </div>
</div>
""",
    unsafe_allow_html=True
)

# =================== SOBRE NOSOTROS ===================
st.markdown('<div class="section" id="sobre-nosotros">', unsafe_allow_html=True)
st.markdown("## Sobre nosotros")
st.write(
    "Benessere nace para ofrecer una alternativa *saludable y transparente* dentro de los campus universitarios. "
    "Trabajamos con *bases de açai sin azúcar añadida*, toppings funcionales y zumos naturales. "
    "Priorizamos logística simple, tiempos de espera cortos y una carta fácil de entender."
)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### Enfoque")
    st.write("- Ingredientes simples.\n- Operación ágil.\n- Precios claros.")
with col2:
    st.markdown("### Lo que no hacemos")
    st.write("- Azúcar añadida.\n- Promesas vacías.\n- Esperas eternas.")
with col3:
    st.markdown("### Valores")
    st.write("- Honestidad.\n- Consistencia.\n- Respeto por tu tiempo.")
st.markdown('</div>', unsafe_allow_html=True)

# =================== MENÚ ===================
st.markdown('<div class="section" id="menu">', unsafe_allow_html=True)
st.markdown("## Menú")
st.write("Estructura base. Luego actualizamos con tus datos oficiales de costos y gramajes.")

for categoria, items in MENU.items():
    st.markdown(f"### {categoria}")
    st.markdown('<table class="table">', unsafe_allow_html=True)
    st.markdown("<thead><tr><th>Producto</th><th>Incluye</th><th>Precio (USD)</th></tr></thead>", unsafe_allow_html=True)
    st.markdown("<tbody>", unsafe_allow_html=True)
    for it in items:
        incluye = it.get("Incluye", "")
        precio = f"{it['Precio']:.2f}"
        st.markdown(f"<tr><td>{it['Producto']}</td><td>{incluye}</td><td><strong>${precio}</strong></td></tr>", unsafe_allow_html=True)
    st.markdown("</tbody></table>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# =================== PRECIOS RESUMEN ===================
st.markdown('<div class="section" id="precios">', unsafe_allow_html=True)
st.markdown("## Precios (resumen)")
c1, c2, c3, c4 = st.columns(4)
for col, (name, price) in zip([c1, c2, c3, c4], [
    ("Bowl Clásico", 4.50),
    ("Bowl Proteico", 5.90),
    ("Bowl Benessere", 6.50),
    ("Zumos (desde)", 2.80),
]):
    with col:
        st.markdown(
            f"""
<div class="card">
  <div style="font-weight:800; color:{PRIMARY}; margin-bottom:.2rem;">{name}</div>
  <div class="price">${price:.2f}</div>
</div>
""",
            unsafe_allow_html=True,
        )
st.markdown('</div>', unsafe_allow_html=True)

# =================== UBICACIONES ===================
st.markdown('<div class="section" id="ubicaciones">', unsafe_allow_html=True)
st.markdown("## Ubicaciones")
colu1, colu2, colu3 = st.columns(3)
with colu1:
    st.markdown("*Universidad Central*\n\nPabellón A – Patio principal\n\n_Lun–Vie 8:00–17:00_")
with colu2:
    st.markdown("*Tecnológico Norte*\n\nCentro Deportivo – Próxima apertura\n\n_Lun–Vie 9:00–16:00_")
with colu3:
    st.markdown("*USalud*\n\nFacultad de Medicina – Exploración\n\n_Horarios por definir_")
st.markdown('</div>', unsafe_allow_html=True)

# =================== FOOTER ===================
st.markdown(
    f"""
<footer>
  <div class="footer-inner">
    <div style="display:flex; align-items:center; gap:.5rem;">
      <img src="logo.png" height="20" alt="Benessere"/>
      <span>© {datetime.now().year} Benessere</span>
    </div>
    <div>Hecho con cuidado: morado + blanco, sin azúcar añadida.</div>
  </div>
</footer>
""",
    unsafe_allow_html=True
)
