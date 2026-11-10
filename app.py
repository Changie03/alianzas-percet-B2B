import streamlit as st
import pandas as pd

# Configuración de página ejecutiva
st.set_page_config(
    page_title="Alianzas PERCET B2B | Homologación y Construcción",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS CORPORATIVOS (Alto Contraste Garantizado) ---
st.markdown("""
    <style>
    /* Forzar estilos limpios en tarjetas sin importar Modo Claro/Oscuro */
    .header-box {
        background: linear-gradient(90deg, #0F172A 0%, #1E293B 100%);
        padding: 24px;
        border-radius: 12px;
        border-left: 6px solid #E50914;
        margin-bottom: 20px;
    }
    .header-title {
        color: #FFFFFF !important;
        font-size: 28px !important;
        font-weight: 800 !important;
        margin: 0 !important;
    }
    .header-sub {
        color: #CBD5E1 !important;
        font-size: 15px !important;
        margin-top: 6px !important;
    }
    .b2b-card {
        background-color: #0F172A !important;
        border: 1px solid #334155;
        border-left: 6px solid #10B981;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.15);
    }
    .b2b-card-warn {
        border-left: 6px solid #F59E0B !important;
    }
    .b2b-card-danger {
        border-left: 6px solid #EF4
