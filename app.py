import streamlit as st
import pandas as pd

# Configuración de la página (estilo oscuro profesional)
st.set_page_config(page_title="PERCET | Subcontratas PRO", layout="wide", initial_sidebar_state="expanded")

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .big-font { font-size:24px !important; font-weight: bold; color: #E50914;}
    .status-verde { color: #00C851; font-weight: bold; }
    .status-rojo { color: #ff4444; font-weight: bold; }
    .card { background-color: #1E1E1E; padding: 20px; border-radius: 10px; margin-bottom: 10px; border-left: 4px solid #00C851;}
    .card-rojo { border-left: 4px solid #ff4444; }
    </style>
""", unsafe_allow_html=True)

# --- BASE DE DATOS SIMULADA ---
data = {
    'Empresa': ['Estructuras y Saneamiento SAC', 'Soldaduras HDPE Andes', 'Constructora Cimentar EIRL', 'Pinturas y Acabados Lima'],
    'Rubro': ['Saneamiento', 'Minería', 'Edificaciones', 'Edificaciones'],
    'Facturación_Max': ['S/. 1,500,000', 'S/. 850,000', 'S/. 2,000,000', 'S/. 150,000'],
    'RUC_Activo': ['✅ Sí', '✅ Sí', '✅ Sí', '✅ Sí'],
    'RNP_Vigente': ['✅ Sí', '✅ Sí', '✅ Sí', '❌ Vencido'],
    'Deuda_SUNAT': ['✅ Cero Deuda', '✅ Cero Deuda', '❌ Deuda Coactiva', '✅ Cero Deuda'],
    'SCTR_y_SSOMA': ['✅ Vigente', '❌ Falta Homologar', '✅ Vigente', '❌ Sin Póliza'],
    'Riesgo_Contratación': ['Bajo', 'Medio', 'Alto', 'Alto']
}
df = pd.DataFrame(data)

# --- SIDEBAR: Selector de Vista ---
st.sidebar.image("https://img.icons8.com/color/96/000000/engineering.png", width=80)
st.sidebar.title("Portal B2B")
vista = st.sidebar.radio("Selecciona tu perfil para el Demo:", 
                         ["🏢 Vista Contratista General", "👷 Vista Subcontratista", "🤝 Consorcios (Próximamente)"])

# ==========================================
# VISTA 1: CONTRATISTA GENERAL (El que contrata)
# ==========================================
if vista == "🏢 Vista Contratista General":
    st.title("Buscador de Subcontratistas Homologados")
    st.markdown("Filtra empresas auditadas en tiempo real para evitar penalidades y paralizaciones de obra.")
    
    col1, col2 = st.columns(2)
    with col1:
        filtro_rubro = st.selectbox("Especialidad requerida:", ["Todos", "Saneamiento", "Minería", "Edificaciones"])
    with col2:
        filtro_riesgo = st.selectbox("Nivel de Riesgo Aceptable:", ["Solo Riesgo Bajo (Compliance Total)", "Incluir Riesgo Medio"])

    st.markdown("---")
    
    # Filtrar datos de prueba
    if filtro_rubro != "Todos":
        df_mostrar = df[df['Rubro'] == filtro_rubro]
    else:
        df_mostrar = df
        
    if filtro_riesgo == "Solo Riesgo Bajo (Compliance Total)":
        df_mostrar = df_mostrar[df_mostrar['Riesgo_Contratación'] == 'Bajo']

    # Mostrar Tarjetas (Cards) de resultados
    for index, row in df_mostrar.iterrows():
        estilo_tarjeta = "card" if row['Riesgo_Contratación'] == 'Bajo' else "card card-rojo"
        
        st.markdown(f"""
        <div class="{estilo_tarjeta}">
            <h3 style='margin-top:0;'>{row['Empresa']} - {row['Rubro']}</h3>
            <p><b>Capacidad Demostrada:</b> {row['Facturación_Max']}</p>
            <p>RUC: {row['RUC_Activo']} | RNP: {row['RNP_Vigente']} | SUNAT: {row['Deuda_SUNAT']} | SSOMA/SCTR: {row['SCTR_y_SSOMA']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if row['Riesgo_Contratación'] == 'Bajo':
            st.button(f"Solicitar Cotización a {row['Empresa']}", key=f"btn_{index}")
        else:
            st.warning("⚠️ Esta empresa no cumple con los requisitos de Compliance para entrar a obra hoy.")

# ==========================================
# VISTA 2: SUBCONTRATISTA Y UPSELL (Tu negocio)
# ==========================================
elif vista == "👷 Vista Subcontratista":
    st.title("Mi Perfil Corporativo")
    st.subheader("Soldaduras HDPE Andes (Ejemplo)")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Licitaciones Disponibles", "14", "Minería")
    col2.metric("Perfil de Riesgo", "Medio", "-1 requisito")
    col3.metric("Visibilidad", "Oculto", "Para grandes mineras")

    st.markdown("---")
    st.markdown("### 🚨 Auditoría de Compliance (Tiempo Real)")
    
    st.success("✅ RUC Activo y Habido")
    st.success("✅ RNP Vigente")
    st.success("✅ Sin Deudas Coactivas SUNAT")
    st.error("❌ SCTR y Plan SSOMA (Minería) - FALTANTE")
    
    st.markdown("---")
    st.markdown("<p class='big-font'>No pierdas el contrato por falta de papeles.</p>", unsafe_allow_html=True)
    st.info("Para postular a la Licitación de 'Movimiento de Tierras - Antamina', necesitas regularizar tu SSOMA y pólizas.")
    
    # Aquí es donde entra tu prima / tu consultoría
    if st.button("🚀 Emitir SCTR y Homologar SSOMA Express (48h)"):
        st.success("¡Solicitud enviada! Un asesor de PERCET Seguros se comunicará contigo en 15 minutos al +51 981328639.")

# ==========================================
# VISTA 3: CONSORCIOS
# ==========================================
else:
    st.title("Match para Consorcios 🤝")
    st.info("Módulo en desarrollo: Encuentra socios estratégicos que complementen tu experiencia técnica o tu capacidad financiera para licitar en OSCE o ANIN.")
