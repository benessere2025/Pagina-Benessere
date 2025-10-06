import streamlit as st
from datetime import datetime
import csv
from pathlib import Path

# ---------- CONFIG ----------
st.set_page_config(
    page_title="Benessere Açai • Sin azúcar",
    page_icon="🍇",
    layout="wide"
)

# ---------- ESTILOS ----------
BRAND = "#4b1a5a"
BRAND_2 = "#6a2583"
BRAND_3 = "#e9e1f0"
WHATSAPP_LINK = "https://wa.me/0000000000?text=Hola%20Benessere,%20quiero%20Açai%20sin%20azúcar%20en%20mi%20campus"

css = f"""
<style>
html, body, [class*="st-"] {{
  font-family: -apple-system, system ui, "Segoe UI", Roboto, Ubuntu, "Helvetica Neue", Arial, "Noto Sans";
}}

/* Navbar */
.navbar {{
  position: sticky; top: 0; z-index: 999;
  background: #fff; border-bottom: 1px solid rgba(0,0,0,.06);
  padding: .75rem 0;
}}
.nav-inner {{
  display:flex; align-items:center; justify-content:space-between;
  max-width: 1200px; margin: 0 auto; padding: 0 1rem;
}}
.nav-left {{ display:flex; align-items:center; gap:.6rem; }}
.brand-name {{ font-weight: 800; color:{BRAND}; font-size: 1.05rem; }}
.nav-right a {{ margin-left: 1rem; font-weight:600; text-decoration:none; color:#333; }}
.nav-right a:hover {{ color:{BRAND}; }}

/* Botones */
.btn {{ display:inline-block; padding:.7rem 1rem; border-radius:.6rem; font-weight:700; text-decoration:none; }}
.btn-light {{ background:#fff; color:{BRAND}; }}
.btn-dark {{ background:#111; color:#fff; }}
.btn-brand {{ background:{BRAND}; color:#fff; }}
.btn-outline {{ border:1px solid #fff; color:#fff; background:transparent; }}
.btn-outline:hover {{ background: rgba(255,255,255,.1); }}

/* HERO */
.hero {{
  position: relative; min-height: 84vh; color:#fff; display:flex; align-items:center;
  background: radial-gradient(1200px 600px at 70% 20%, {BRAND_2} 0%, {BRAND} 40%, #2d0f37 100%);
  overflow:hidden;
}}
.hero::before {{
  content:""; position:absolute; inset:0;
  background: url('https://images.unsplash.com/photo-1549122728-f519709caa9c?q=80&w=2000&auto=format&fit=crop') center/cover no-repeat;
  filter: blur(3px) saturate(1.1) brightness(.65); transform: scale(1.05);
}}
.hero::after {{
  content:""; position:absolute; inset:0; background: linear-gradient(180deg, rgba(20,0,30,.35), rgba(20,0,30,.7));
}}
.hero-inner {{ position:relative; z-index:2; max-width: 1200px; margin: 0 auto; padding: 4rem 1rem; }}
.hero h1 {{ font-weight:900; letter-spacing:.2px; line-height:1.04; font-size: clamp(2rem, 5vw, 3.2rem); }}
.hero p.lead {{ font-size: 1.15rem; opacity:.95; }}

/* Secciones */
.section {{ padding: 3.5rem 0; }}
.section-title {{ color:{BRAND}; font-weight:900; font-size: clamp(1.6rem, 3vw, 2rem); }}
.subtle {{ color:#555; }}

/* Cards */
.card {{ border:1px solid #eee; border-radius: 14px; padding: 1.1rem; background:#fff; }}
.badge {{ background:{BRAND}; color:#fff; padding:.2rem .6rem; border-radius:.5rem; font-size:.8rem; font-weight:700; }}

/* Footer */
.footer {{ background:#0f0b12; color:#cfc6d8; padding: 1.2rem 0; }}
.footer a {{ color:#cfc6d8; text-decoration:none; margin-left:1rem; }}
.footer a:hover {{ color:#fff; text-decoration:underline; }}

/* WhatsApp flotante */
.wa-float {{
  position: fixed; right: 16px; bottom: 18px; z-index: 9999;
  width:56px; height:56px; border-radius:50%; display:flex; align-items:center; justify-content:center;
  background:#25d366; color:#fff; box-shadow:0 8px 30px rgba(0,0,0,.25);
  font-size: 24px; text-decoration:none;
}}
.wa-float:hover {{ transform: translateY(-2px); }}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# ---------- NAVBAR ----------
nav_html = """
<div class="navbar">
  <div class="nav-inner">
    <div class="nav-left">
      <img src="logo.png" alt="Benessere" height="28">
      <span class="brand-name">Benessere</span>
    </div>
    <div class="nav-right">
      <a href="#quienes">Quiénes somos</a>
      <a href="#hacemos">Qué hacemos</a>
      <a href="#porque">¿Por qué sin azúcar?</a>
      <a href="#campus">Campus</a>
      <a class="btn btn-brand" href="#contacto">Saber más</a>
    </div>
  </div>
</div>
"""
st.markdown(nav_html, unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown(
    f"""
<section class="hero" id="inicio">
  <div class="hero-inner">
    <h1>Açai sin azúcar para <u>tu campus</u></h1>
    <p class="lead">Apoyamos a los estudiantes que quieren comer rico, limpio y rápido. Recetas con 0 azúcar añadida, fruta real y toppings funcionales.</p>
    <div style="display:flex; gap:.6rem; flex-wrap:wrap;">
      <a href="#contacto" class="btn btn-light">Cotizar para mi universidad</a>
      <a href="#porque" class="btn btn-outline">Conoce nuestros ingredientes</a>
    </div>
  </div>
</section>
""",
    unsafe_allow_html=True
)

# ---------- QUIENES SOMOS ----------
st.markdown('<section id="quienes" class="section">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown(f"### <span class='section-title'>Quiénes somos</span>", unsafe_allow_html=True)
    st.write(
        "Benessere es una cadena de snacks enfocada en açai **sin azúcar añadida**. "
        "Operamos dentro de campus universitarios con módulos compactos, servicio en menos de 2 minutos "
        "y menús diseñados por nutrición."
    )
with col2:
    st.image("https://images.unsplash.com/photo-1526312426976-593c2b999c1a?q=80&w=1600&auto=format&fit=crop", use_container_width=True, caption="Açai")
    st.image("https://images.unsplash.com/photo-1492684223066-81342ee5ff30?q=80&w=1600&auto=format&fit=crop", use_container_width=True, caption="Estudiantes")
st.markdown('</section>', unsafe_allow_html=True)

# ---------- LO QUE HACEMOS ----------
st.markdown('<section id="hacemos" class="section" style="background:#f7f7fb;">', unsafe_allow_html=True)
st.markdown(f"### <span class='section-title'>Lo que hacemos</span>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        f"""
<div class="card">
  <div style="font-size:1.4rem; color:{BRAND};">🥤</div>
  <h5>Bowls & Smoothies</h5>
  <p>Bases de açai sin azúcar, toppings funcionales (granola sin azúcar, frutas, mantequilla de maní natural) y proteínas vegetales.</p>
</div>""",
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        f"""
<div class="card">
  <div style="font-size:1.4rem; color:{BRAND};">⏱️</div>
  <h5>Servicio en 2 minutos</h5>
  <p>Operación pensada para entre-clases: flujo rápido, POS móvil y pedidos por QR.</p>
</div>""",
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        f"""
<div class="card">
  <div style="font-size:1.4rem; color:{BRAND};">📍</div>
  <h5>Módulos para campus</h5>
  <p>Islas compactas de 6–10 m² con instalación eléctrica estándar y cero gas.</p>
</div>""",
        unsafe_allow_html=True,
    )
st.markdown('</section>', unsafe_allow_html=True)

# ---------- POR QUÉ SIN AZÚCAR ----------
st.markdown('<section id="porque" class="section">', unsafe_allow_html=True)
colA, colB = st.columns([1, 1])
with colA:
    st.markdown(f"### <span class='section-title'>¿Por qué sin azúcar?</span>", unsafe_allow_html=True)
    st.markdown(
        """
- **Salud metabólica**: Menos picos de glucosa, más energía estable para estudiar.  
- **Ingredientes reales**: Fruta entera y dulzor natural de la baya.  
- **Sustentable**: Packaging reciclable y cadena de frío eficiente.  
"""
    )
with colB:
    st.image("https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=1600&auto=format&fit=crop", use_container_width=True, caption="Ingredientes")
st.markdown('</section>', unsafe_allow_html=True)

# ---------- CAMPUS ----------
st.markdown('<section id="campus" class="section" style="background:#f7f7fb;">', unsafe_allow_html=True)
st.markdown(f"### <span class='section-title'>Campus donde operamos</span>", unsafe_allow_html=True)
cc1, cc2, cc3 = st.columns(3)
with cc1:
    st.markdown(
        """
<div class="card">
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <h5 style="margin:0;">Universidad Central</h5>
    <span class="badge">Activo</span>
  </div>
  <p class="subtle">Pabellón A • Patio principal</p>
  <p>Horario: Lun–Vie 8:00–17:00</p>
</div>""",
        unsafe_allow_html=True,
    )
with cc2:
    st.markdown(
        """
<div class="card">
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <h5 style="margin:0;">Tecnológico Norte</h5>
    <span class="badge">Próximo</span>
  </div>
  <p class="subtle">Centro Deportivo</p>
  <p>Inicio previsto: Noviembre</p>
</div>""",
        unsafe_allow_html=True,
    )
with cc3:
    st.markdown(
        """
<div class="card">
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <h5 style="margin:0;">USalud</h5>
    <span class="badge">Explorando</span>
  </div>
  <p class="subtle">Facultad de Medicina</p>
  <p>Contactando a Dirección de Bienestar</p>
</div>""",
        unsafe_allow_html=True,
    )
st.markdown('</section>', unsafe_allow_html=True)

# ---------- CONTACTO ----------
st.markdown(
    f"""
<section id="contacto" class="section" style="color:#fff; background:
radial-gradient(1200px 600px at 70% 20%, {BRAND_2} 0%, {BRAND} 40%, #2d0f37 100%);">
  <div style="max-width:1200px; margin:0 auto;">
    <h2 style="font-weight:900;">¿Lo llevamos a tu universidad?</h2>
    <p class="subtle" style="color:#eee;">Escríbenos por WhatsApp o deja tus datos y te contactamos hoy.</p>
    <a class="btn btn-light" href="{WHATSAPP_LINK}" target="_blank">💬 Hablar por WhatsApp</a>
  </div>
</section>
""",
    unsafe_allow_html=True,
)

st.markdown("### Déjanos tus datos")
with st.form("lead_form", clear_on_submit=True):
    nombre = st.text_input("Nombre")
    email = st.text_input("Email")
    campus = st.text_input("Universidad / Campus")
    mensaje = st.text_area("Mensaje")
    enviado = st.form_submit_button("Enviar")

    if enviado:
        path = Path("leads.csv")
        write_header = not path.exists()
        with path.open("a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if write_header:
                w.writerow(["timestamp", "nombre", "email", "campus", "mensaje"])
            w.writerow([datetime.utcnow().isoformat(), nombre, email, campus, mensaje])
        st.success("¡Gracias! Recibimos tus datos. Te contactaremos pronto.")

# ---------- FOOTER ----------
year = datetime.now().year
st.markdown(
    f"""
<div class="footer">
  <div class="nav-inner" style="max-width:1200px; margin:0 auto;">
    <div style="display:flex; align-items:center; gap:.6rem;">
      <img src="logo.png" alt="Benessere" height="22">
      <span>© {year} Benessere • Açai sin azúcar</span>
    </div>
    <div>
      <a href="#quienes">Quiénes somos</a>
      <a href="#hacemos">Qué hacemos</a>
      <a href="#porque">Ingredientes</a>
      <a href="#campus">Campus</a>
    </div>
  </div>
</div>

<a class="wa-float" href="{WHATSAPP_LINK}" target="_blank" title="Escríbenos por WhatsApp">✆</a>
""",
    unsafe_allow_html=True,
)
