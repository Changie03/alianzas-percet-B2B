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
        border-left: 6px solid #EF4444 !important;
    }
    .card-title {
        color: #FFFFFF !important;
        font-size: 20px !important;
        font-weight: 700 !important;
        margin-bottom: 4px !important;
    }
    .card-meta {
        color: #94A3B8 !important;
        font-size: 13px !important;
        margin-bottom: 12px !important;
    }
    .card-amount {
        color: #38BDF8 !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        margin-bottom: 12px !important;
    }
    .badge-ok {
        background-color: #064E3B;
        color: #34D399 !important;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
        margin-right: 6px;
        margin-bottom: 6px;
        border: 1px solid #059669;
    }
    .badge-err {
        background-color: #450A0A;
        color: #F87171 !important;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
        margin-right: 6px;
        margin-bottom: 6px;
        border: 1px solid #DC2626;
    }
    .badge-info {
        background-color: #1E3A8A;
        color: #93C5FD !important;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
        margin-right: 6px;
        margin-bottom: 6px;
    }
    .kpi-box {
        background-color: #1E293B;
        padding: 16px;
        border-radius: 10px;
        border-top: 3px solid #E50914;
        text-align: center;
    }
    .kpi-num {
        color: #FFFFFF !important;
        font-size: 24px !important;
        font-weight: 800 !important;
        margin: 0 !important;
    }
    .kpi-label {
        color: #94A3B8 !important;
        font-size: 12px !important;
        margin: 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- BASE DE DATOS REALISTA B2B ---
empresas_data = [
    {
        "Empresa": "Estructuras y Saneamiento del Norte S.A.C.",
        "RUC": "20608451231",
        "Nivel": "Subcontratista Especializado",
        "Rubro": "Saneamiento y Redes",
        "Especialidades": "Redes de agua y alcantarillado, Termofusión HDPE, Estaciones de bombeo",
        "Region": "Lima / Lambayeque",
        "Facturacion_Num": 1500000,
        "Facturacion_Txt": "S/ 1,500,000",
        "RUC_Activo": True,
        "RNP_Vigente": True,
        "Sin_Deuda_SUNAT": True,
        "SSOMA_SCTR": True,
        "REMYPE": True,
        "Score": 98,
        "Riesgo": "Bajo",
        "Personal": "35 operarios homologados (SCTR Salud/Pensión vigente)",
        "Equipos": "3 Máquinas de Termofusión McElroy, 2 Retroexcavadoras, Topografía completa",
        "Ultimas_Obras": "1) Cambio de colectores SEDAPAL Surco (S/ 620,000 - Acta Conforme) | 2) Línea de impulsión HDPE Olmos (S/ 880,000 - Acta Conforme)"
    },
    {
        "Empresa": "Ingeniería y Soldaduras Mineras Andes S.A.C.",
        "RUC": "20559102348",
        "Nivel": "Subcontratista Especializado",
        "Rubro": "Minería",
        "Especialidades": "Montaje electromecánico, Tuberías de relaves HDPE, Mantenimiento de planta",
        "Region": "Áncash / Arequipa / Moquegua",
        "Facturacion_Num": 2800000,
        "Facturacion_Txt": "S/ 2,800,000",
        "RUC_Activo": True,
        "RNP_Vigente": True,
        "Sin_Deuda_SUNAT": True,
        "SSOMA_SCTR": True,
        "REMYPE": False,
        "Score": 96,
        "Riesgo": "Bajo",
        "Personal": "48 técnicos certificados (Pases médicos mineros e inducción Anexo 4 vigente)",
        "Equipos": "Camiones grúa 12TN, Equipos de electrofusión, Andamios normados Layher",
        "Ultimas_Obras": "1) Mantenimiento línea de relaves Antamina (S/ 1,450,000) | 2) Montaje estructural Las Bambas (S/ 1,350,000)"
    },
    {
        "Empresa": "Consorcio Edificador Pacífico S.A.C.",
        "RUC": "20601122994",
        "Nivel": "Contratista / Subcontratista",
        "Rubro": "Edificaciones",
        "Especialidades": "Casco estructural, Concreto armado, Remodelación de agencias bancarias y retail",
        "Region": "Lima / Nivel Nacional",
        "Facturacion_Num": 3500000,
        "Facturacion_Txt": "S/ 3,500,000",
        "RUC_Activo": True,
        "RNP_Vigente": True,
        "Sin_Deuda_SUNAT": True,
        "SSOMA_SCTR": True,
        "REMYPE": True,
        "Score": 95,
        "Riesgo": "Bajo",
        "Personal": "60 operarios en planilla + Staff de Ingenieros Residentes y Prevencionistas SSOMA",
        "Equipos": "Encofrados metálicos Ulma, Vibradoras, Equipos láser de nivelación",
        "Ultimas_Obras": "1) Remodelación integral 8 sedes bancarias Lima/Norte (S/ 1,200,000) | 2) Edificio Multifamiliar 12 pisos Surco (S/ 2,300,000)"
    },
    {
        "Empresa": "Acabados Corporativos, Drywall y Pintura Lima E.I.R.L.",
        "RUC": "20609988112",
        "Nivel": "Cuadrilla / Subcontratista",
        "Rubro": "Acabados y Drywall",
        "Especialidades": "Tabiquería Drywall RF, Cielo raso acústico, Pintura epóxica e industrial, Carpintería metálica",
        "Region": "Lima",
        "Facturacion_Num": 320000,
        "Facturacion_Txt": "S/ 320,000",
        "RUC_Activo": True,
        "RNP_Vigente": True,
        "Sin_Deuda_SUNAT": True,
        "SSOMA_SCTR": False,
        "REMYPE": True,
        "Score": 72,
        "Riesgo": "Medio",
        "Personal": "18 operarios especialistas en acabados rápidos retail y oficinas",
        "Equipos": "Equipos Airless Graco para pintura, Andamios multidireccionales, Herramientas inalámbricas",
        "Ultimas_Obras": "1) Acondicionamiento oficinas San Isidro (S/ 180,000) | 2) Acabados y pintura centro comercial Miraflores (S/ 140,000)"
    },
    {
        "Empresa": "Movimiento de Tierras y Pavimentos del Perú S.A.C.",
        "RUC": "20541122339",
        "Nivel": "Subcontratista Especializado",
        "Rubro": "Infraestructura Vial",
        "Especialidades": "Movimiento de tierras masivo, Conformación de subrasante, Pavimento rígido y flexible",
        "Region": "Lambayeque / Piura / La Libertad",
        "Facturacion_Num": 1850000,
        "Facturacion_Txt": "S/ 1,850,000",
        "RUC_Activo": True,
        "RNP_Vigente": False,
        "Sin_Deuda_SUNAT": False,
        "SSOMA_SCTR": True,
        "REMYPE": True,
        "Score": 55,
        "Riesgo": "Alto",
        "Personal": "25 operadores de maquinaria pesada",
        "Equipos": "Motoniveladora CAT, Rodillo compactador 10TN, 4 Volquetes 15m3",
        "Ultimas_Obras": "1) Habilitación urbana y pavimentación Chiclayo (S/ 950,000) | 2) Defensa ribereña y descolmatación (S/ 900,000)"
    }
]

df_empresas = pd.DataFrame(empresas_data)

# --- SIDEBAR: NAVEGACIÓN COMERCIAL ---
st.sidebar.markdown("## 🏗️ ALIANZAS PERCET B2B")
st.sidebar.caption("Ecosistema de Homologación, Subcontratación, Seguros y Consorcios en Perú.")
st.sidebar.markdown("---")

vista = st.sidebar.radio(
    "Selecciona el Módulo de Demostración:",
    [
        "🏢 1. Buscador B2B (Contratistas)",
        "👷 2. Portal Subcontratista y Seguros",
        "🤝 3. Consorcios e Inversionistas"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🛡️ Respaldo Operativo")
st.sidebar.info(
    "**Verificación en Tiempo Real:**\n"
    "• Consulta RUC y Deuda SUNAT\n"
    "• Vigencia RNP (OSCE) y REMYPE\n"
    "• Auditoría SSOMA (Ley 29783)\n"
    "• Emisión Express de SCTR y Vida Ley"
)

# ==============================================================================
# VISTA 1: BUSCADOR SOFISTICADO PARA CONTRATISTAS GENERALES
# ==============================================================================
if vista == "🏢 1. Buscador B2B (Contratistas)":
    st.markdown("""
        <div class="header-box">
            <p class="header-title">Buscador Inteligente de Subcontratistas y Cuadrillas Homologadas</p>
            <p class="header-sub">Audita capacidad financiera, actas de recepción de obra, cumplimiento SUNAT y pólizas SSOMA/SCTR antes de contratar.</p>
        </div>
    """, unsafe_allow_html=True)

    # KPIs Ejecutivos
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown('<div class="kpi-box"><p class="kpi-num">142</p><p class="kpi-label">Empresas y Cuadrillas Auditadas</p></div>', unsafe_allow_html=True)
    with k2:
        st.markdown('<div class="kpi-box"><p class="kpi-num">S/ 48.5M</p><p class="kpi-label">Capacidad de Obra Verificada</p></div>', unsafe_allow_html=True)
    with k3:
        st.markdown('<div class="kpi-box"><p class="kpi-num">100%</p><p class="kpi-label">Trazabilidad SSOMA / SUNAFIL</p></div>', unsafe_allow_html=True)
    with k4:
        st.markdown('<div class="kpi-box"><p class="kpi-num">< 24 hrs</p><p class="kpi-label">Tiempo de Homologación y SCTR</p></div>', unsafe_allow_html=True)

    st.write("")

    # --- PANEL DE FILTROS AVANZADOS ---
    with st.container(border=True):
        st.markdown("#### 🔍 Filtros de Búsqueda Técnica y Financiera")
        f1, f2, f3 = st.columns([2, 1.5, 1.5])
        with f1:
            busqueda_txt = st.text_input(
                "Buscar por RUC, empresa o partida específica:",
                placeholder="Ej. HDPE, Drywall, Saneamiento, 20608451231, Antamina..."
            )
        with f2:
            filtro_rubro = st.selectbox(
                "Sector / Especialidad:",
                ["Todos los sectores", "Saneamiento y Redes", "Minería", "Edificaciones", "Acabados y Drywall", "Infraestructura Vial"]
            )
        with f3:
            filtro_nivel = st.selectbox(
                "Tipo de Proveedor:",
                ["Todos", "Subcontratista Especializado", "Contratista / Subcontratista", "Cuadrilla / Subcontratista"]
            )

        f4, f5 = st.columns([1.5, 2.5])
        with f4:
            monto_min = st.slider(
                "Capacidad Demostrada Mínima en Obra (S/):",
                min_value=0,
                max_value=3000000,
                value=150000,
                step=50000,
                format="S/ %d"
            )
        with f5:
            st.markdown("**Exigencias de Compliance Obligatorias:**")
            c1, c2, c3, c4 = st.columns(4)
            req_rnp = c1.checkbox("RNP Vigente", value=False)
            req_sunat = c2.checkbox("Cero Deuda SUNAT", value=False)
            req_ssoma = c3.checkbox("SSOMA + SCTR Activo", value=False)
            req_remype = c4.checkbox("Inscrito REMYPE", value=False)

    # --- LÓGICA DE FILTRADO ---
    df_filtrado = df_empresas.copy()

    if busqueda_txt:
        mask = (
            df_filtrado["Empresa"].str.contains(busqueda_txt, case=False, na=False) |
            df_filtrado["RUC"].str.contains(busqueda_txt, case=False, na=False) |
            df_filtrado["Especialidades"].str.contains(busqueda_txt, case=False, na=False) |
            df_filtrado["Region"].str.contains(busqueda_txt, case=False, na=False)
        )
        df_filtrado = df_filtrado[mask]

    if filtro_rubro != "Todos los sectores":
        df_filtrado = df_filtrado[df_filtrado["Rubro"] == filtro_rubro]

    if filtro_nivel != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Nivel"] == filtro_nivel]

    df_filtrado = df_filtrado[df_filtrado["Facturacion_Num"] >= monto_min]

    if req_rnp:
        df_filtrado = df_filtrado[df_filtrado["RNP_Vigente"] == True]
    if req_sunat:
        df_filtrado = df_filtrado[df_filtrado["Sin_Deuda_SUNAT"] == True]
    if req_ssoma:
        df_filtrado = df_filtrado[df_filtrado["SSOMA_SCTR"] == True]
    if req_remype:
        df_filtrado = df_filtrado[df_filtrado["REMYPE"] == True]

    st.markdown(f"**Resultados encontrados:** `{len(df_filtrado)}` empresas verificadas en la plataforma")

    # --- RENDERIZADO DE TARJETAS EJECUTIVAS ---
    for idx, row in df_filtrado.iterrows():
        clase_borde = "b2b-card"
        if row["Riesgo"] == "Medio":
            clase_borde = "b2b-card b2b-card-warn"
        elif row["Riesgo"] == "Alto":
            clase_borde = "b2b-card b2b-card-danger"

        badge_ruc = '<span class="badge-ok">✅ RUC 20 Activo/Habido</span>' if row["RUC_Activo"] else '<span class="badge-err">❌ RUC Observado</span>'
        badge_rnp = '<span class="badge-ok">✅ RNP OSCE Vigente</span>' if row["RNP_Vigente"] else '<span class="badge-err">❌ RNP Suspendido/Vencido</span>'
        badge_sunat = '<span class="badge-ok">✅ Cero Deuda Coactiva SUNAT</span>' if row["Sin_Deuda_SUNAT"] else '<span class="badge-err">⚠️ Con Deuda Coactiva</span>'
        badge_ssoma = '<span class="badge-ok">🛡️ SCTR + Plan SSOMA Activo</span>' if row["SSOMA_SCTR"] else '<span class="badge-err">🚨 Falta SCTR / Homologar SSOMA</span>'
        badge_remype = '<span class="badge-info">📋 REMYPE Acreditado</span>' if row["REMYPE"] else ''

        st.markdown(f"""
            <div class="{clase_borde}">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <p class="card-title">{row['Empresa']}</p>
                        <p class="card-meta"><b>RUC:</b> {row['RUC']} | <b>Categoría:</b> {row['Nivel']} | <b>Sector:</b> {row['Rubro']} | <b>Región:</b> {row['Region']}</p>
                    </div>
                    <div style="text-align:right;">
                        <span class="badge-info" style="font-size:14px;">Score PERCET: {row['Score']}/100</span>
                    </div>
                </div>
                <p class="card-amount">📊 Experiencia Facturada Auditada: {row['Facturacion_Txt']} — <span style="color:#E2E8F0; font-weight:normal;">{row['Especialidades']}</span></p>
                <div>
                    {badge_ruc} {badge_rnp} {badge_sunat} {badge_ssoma} {badge_remype}
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Brochure y Dossier Desplegable
        col_exp, col_btn = st.columns([3.5, 1.5])
        with col_exp:
            with st.expander(f"📂 Ver Brochure Corporativo, Maquinaria y Actas de Obra de {row['Empresa']}"):
                st.markdown(f"**👷 Personal y Seguridad:** {row['Personal']}")
                st.markdown(f"**🚜 Maquinaria y Equipos Propios:** {row['Equipos']}")
                st.markdown(f"**📜 Obras Ejecutadas (Respaldadas con Facturas y Actas de Recepción):**\n{row['Ultimas_Obras']}")
        with col_btn:
            if row["Riesgo"] == "Bajo":
                if st.button(f"📩 Invitar a Licitación", key=f"inv_{idx}", use_container_width=True):
                    st.success(f"Invitación enviada a {row['Empresa']}. Copia remitida a la Mesa de Control de PERCET.")
            else:
                if st.button(f"⚡ Solicitar Regularización", key=f"reg_{idx}", use_container_width=True):
                    st.warning("Alerta enviada: Nuestro equipo legal/seguros regularizará a este proveedor en 48h para habilitar su ingreso a obra.")


# ==============================================================================
# VISTA 2: PORTAL SUBCONTRATISTA, FORMALIZACIÓN Y SEGUROS (EL MOTOR DE INGRESOS)
# ==============================================================================
elif vista == "👷 2. Portal Subcontratista y Seguros":
    st.markdown("""
        <div class="header-box">
            <p class="header-title">Portal de Homologación, Licitaciones Privadas y Seguros de Obra</p>
            <p class="header-sub">Acredita tu experiencia real en soles, regulariza tu SSOMA/SCTR y postula directamente a obras de contratistas generales y mineras.</p>
        </div>
    """, unsafe_allow_html=True)

    perfil_simulado = st.selectbox(
        "Simular vista como:",
        [
            "Caso 1: Subcontratista Formal con SCTR/SSOMA pendiente (Venta cruzada de Seguros)",
            "Caso 2: Maestro Contratista / Cuadrilla que busca Formalizarse (Servicio de Constitución + Brochure)"
        ]
    )

    if "Caso 1" in perfil_simulado:
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Empresa", "Acabados y Drywall Lima EIRL")
        c2.metric("Capacidad Auditada", "S/ 320,000", "2 Actas validadas")
        c3.metric("Score de Compliance", "72 / 100", "-28 pts por SSOMA")
        c4.metric("Estado para Minería/Retail", "BLOQUEADO", delta_color="inverse")

        st.markdown("---")
        col_izq, col_der = st.columns([1.4, 1.6])

        with col_izq:
            st.markdown("#### 🛡️ Mi Semáforo de Homologación")
            st.success("✅ **RUC 20609988112:** Activo y Habido")
            st.success("✅ **RNP Servicios y Obras:** Vigente")
            st.success("✅ **REMYPE:** Acreditado como Micro/Pequeña Empresa")
            st.success("✅ **Reporte Tributario SUNAT:** Sin deuda en cobranza coactiva")
            st.error("❌ **Póliza SCTR (Salud/Pensión) y Vida Ley:** VENCIDA / NO REGISTRADA")
            st.error("❌ **Plan Anual SSOMA y Matriz IPERC (Ley 29783):** PENDIENTE DE FIRMA")

            st.info(
                "💡 **¿Sabías que?** Una multa de SUNAFIL por ingresar personal a obra sin SCTR ni IPERC supera las **26 UIT (más de S/ 130,000)** y bloquea los pagos de valorizaciones del Contratista General."
            )

        with col_der:
            st.markdown("#### 📋 Licitaciones Privadas Disponibles en tu Rubro")
            with st.container(border=True):
                st.markdown("**1. Remodelación de 5 Agencias Bancarias (Tabiquería Drywall RF, Cielo Raso y Pintura)**")
                st.caption("Contratista General: Consorcio Edificador Pacífico | Presupuesto Referencial: S/ 240,000 | Ubicación: Lima")
                st.warning("⚠️ Requisito excluyente: SCTR activo de los 18 operarios + Plan SSOMA aprobado.")
                st.button("🔒 Postulación Bloqueada (Regularizar SSOMA/SCTR primero)", disabled=True, key="b_lock1")

            with st.container(border=True):
                st.markdown("**2. Mantenimiento de Campamento Minero y Oficinas Técnicas**")
                st.caption("Cliente: Compañía Minera en Áncash | Presupuesto Referencial: S/ 410,000 | Duración: 45 días")
                st.warning("⚠️ Requisito excluyente: SCTR Minería, Póliza CAR/Responsabilidad Civil y Homologación SSOMA.")
                st.button("🔒 Postulación Bloqueada (Regularizar Pólizas primero)", disabled=True, key="b_lock2")

            st.markdown("### 🚀 Desbloquea tus Licitaciones Hoy")
            if st.button("🛡️ Cotizar y Emitir SCTR + Plan SSOMA Express (Alianza Seguros PERCET)", type="primary", use_container_width=True):
                st.success(
                    "¡Solicitud prioritaria generada! Nuestra corredora de seguros aliada y el área SSOMA de PERCET emitirán tus pólizas SCTR, Vida Ley y dossier SSOMA en menos de 24 horas para desbloquear tu postulación."
                )

    else:
        st.markdown("#### 🛠️ Programa de Formalización e Incubación de Cuadrillas y Nuevos Subcontratistas")
        st.write("¿Tienes personal calificado (fierreros, soldadores HDPE, pintores, gasfiteros, maestros de obra) pero pierdes contratos grandes por no tener empresa formal ni brochure corporativo?")

        p1, p2, p3 = st.columns(3)
        with p1:
            with st.container(border=True):
                st.markdown("### 1️⃣ Pack Formalización Legal")
                st.markdown("- Constitución de empresa S.A.C. o E.I.R.L.\n- Activación de RUC 20 y Clave SOL\n- Inscripción en REMYPE (Régimen Laboral Especial)\n- Inscripción en el RNP (OSCE)")
        with p2:
            with st.container(border=True):
                st.markdown("### 2️⃣ Pack Imagen y Brochure B2B")
                st.markdown("- Diseño de Brochure Corporativo de Ingeniería\n- Sistematización de experiencia y presupuestos ejecutados\n- Correo corporativo y ficha técnica en la App")
        with p3:
            with st.container(border=True):
                st.markdown("### 3️⃣ Pack Blindaje SSOMA + Seguros")
                st.markdown("- Emisión de SCTR Salud y Pensión para tu cuadrilla\n- Póliza Vida Ley y Responsabilidad Civil\n- Elaboración de Matriz IPERC y Reglamento SSOMA")

        if st.button("📲 Solicitar Paquete de Formalización e Ingreso a la Red PERCET", type="primary"):
            st.success("Solicitud registrada. Un consultor de negocios B2B se contactará contigo para estructurar tu empresa y habilitar tu perfil en la plataforma.")


# ==============================================================================
# VISTA 3: CONSORCIOS E INVERSIONISTAS (LICITACIONES Y CAPITAL DE TRABAJO)
# ==============================================================================
else:
    st.markdown("""
        <div class="header-box">
            <p class="header-title">Mesa de Consorcios B2B e Inversionistas de Obra</p>
            <p class="header-sub">Conecta empresas con alta capacidad técnica y RNP con socios capitalistas o empresas con línea de fianzas para ganar licitaciones públicas y privadas.</p>
        </div>
    """, unsafe_allow_html=True)

    tab_consorcio, tab_inversion = st.tabs(["🤝 Buscador de Socios para Consorcio", "💼 Oportunidades para Inversionistas Calificados"])

    with tab_consorcio:
        st.markdown("#### Oportunidades Activas de Consorcio (Auditadas por PERCET)")
        with st.container(border=True):
            st.markdown("##### 📍 Licitación Pública: Mejoramiento de Redes de Agua Potable y Alcantarillado - Norte del Perú")
            st.markdown("**Valor Referencial:** `S/ 6,800,000` | **Entidad:** Ministerio / Gobierno Regional")
            st.markdown("**Empresa Proponente:** Constructora con S/ 5M en experiencia de saneamiento certificada y plantel técnico completo.")
            st.markdown("**Socio Buscado:** Empresa con RNP de Obras vigente que aporte **Capacidad Libre de Contratación (S/ 2M)** y solvencia para **Carta Fianza de Fiel Cumplimiento (10%)**.")
            st.button("Solicitar Reunión Confidencial de Consorcio (NDA)", key="cons_1")

        with st.container(border=True):
            st.markdown("##### 📍 Proyecto Privado: Construcción de Almacén Industrial y Losa de Concreto 8,000 m² - Lurín")
            st.markdown("**Valor Referencial:** `S/ 2,400,000` | **Cliente:** Operador Logístico Internacional")
            st.markdown("**Empresa Proponente:** Contratista con línea de crédito aprobada y relación comercial directa con el cliente.")
            st.markdown("**Socio Buscado:** Subcontratista / Consorciado especialista en movimiento de tierras y pisos industriales con maquinaria propia en Lima.")
            st.button("Solicitar Reunión Confidencial de Consorcio (NDA)", key="cons_2")

    with tab_inversion:
        st.markdown("#### Proyectos con Orden de Servicio / Contrato Adjudicado que requieren Capital de Trabajo")
        st.info("🔒 Todos los proyectos listados cuentan con contrato firmado, flujo de valorizaciones auditado en cuenta fideicomiso o cesión de derechos de cobro.")
        with st.container(border=True):
            st.markdown("##### 💰 Financiamiento de Capital de Trabajo - Obra de Montaje Electromecánico Minero")
            st.markdown("- **Contrato Adjudicado:** S/ 1,450,000 (Orden de Servicio emitida por minera de primer nivel)\n- **Capital Requerido (Tramo 1):** S/ 250,000 para compra de tuberías HDPE y movilización de cuadrilla\n- **Plazo de Retorno:** 60 días (Contra pago de Valorización N° 01 y N° 02)\n- **Garantía:** Factura Negociable registrada en CAVALI + Póliza de Caución")
            st.button("Descargar Dossier Financiero del Proyecto", key="inv_1")
