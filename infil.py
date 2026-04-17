import streamlit as st
# Importamos la base de datos desde tu otro archivo
from datos_cff import infracciones_79_80, quiz_79_80, infracciones_81_82, quiz_81_82

# Configuración de la página (Pestaña del navegador)
st.set_page_config(page_title="Simulador CFF - Infracciones y Multas", page_icon="⚖️", layout="wide")

# ==========================================
# MENÚ LATERAL DE NAVEGACIÓN
# ==========================================
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Escudo_de_la_Suprema_Corte_de_Justicia_de_la_Naci%C3%B3n_%28M%C3%A9xico%29.svg/1200px-Escudo_de_la_Suprema_Corte_de_Justicia_de_la_Naci%C3%B3n_%28M%C3%A9xico%29.svg.png", width=150)
    st.header("📚 Módulos de Estudio")
    modulo_seleccionado = st.radio(
        "Selecciona el bloque a analizar:", 
        ["Art. 79 y 80: Registro Federal de Contribuyentes", 
         "Art. 81 y 82: Declaraciones y Avisos"]
    )
    st.markdown("---")
    st.info("💡 **Instrucciones:** Revisa la literalidad de la norma en el Catálogo y luego pon a prueba tu análisis en la Evaluación Práctica.")

# ==========================================
# LÓGICA PRINCIPAL (MÓDULOS)
# ==========================================

# Módulo 1: RFC (79 y 80)
if modulo_seleccionado == "Art. 79 y 80: Registro Federal de Contribuyentes":
    st.title("🏛️ Infracciones del RFC (Art. 79 y 80 CFF)")
    
    tab1, tab2 = st.tabs(["📖 Catálogo Exhaustivo", "📝 Evaluación Práctica"])
    
    with tab1:
        st.header("Estudio Literal de la Norma")
        for item in infracciones_79_80:
            with st.expander(f"⚖️ {item['fraccion']}"):
                st.write(f"**Tipicidad:** {item['infraccion']}")
                st.error(f"**Parámetro de Multa:**\n{item['multa']}")
                st.info(f"**Caso Hipotético:** {item['ejemplo']}")
                
    with tab2:
        st.header("Análisis de Casos Prácticos")
        if 'eval_79' not in st.session_state:
            st.session_state.eval_79 = False

        respuestas_usuario = {}
        with st.form("form_79"):
            for i, q in enumerate(quiz_79_80):
                st.write(f"**{q['pregunta']}**")
                respuestas_usuario[i] = st.radio("Elige el encuadre legal:", q['opciones'], key=f"q79_{i}", index=None)
                st.markdown("---")
                
            btn_calificar = st.form_submit_button("✅ Calificar Actividad")
            if btn_calificar:
                st.session_state.eval_79 = True

        if st.session_state.eval_79:
            aciertos = 0
            st.subheader("Resultados de la Subsunción")
            for i, q in enumerate(quiz_79_80):
                if respuestas_usuario[i] == q['respuesta']:
                    aciertos += 1
                    st.success(f"Caso {i+1}: Correcto. Fundamento aplicable: '{q['respuesta']}'.")
                else:
                    st.error(f"Caso {i+1}: Incorrecto. El encuadre legal exacto es: '{q['respuesta']}'.")
            
            st.metric(label="Calificación", value=f"{aciertos} / 10")
            if aciertos >= 8:
                st.balloons()
            
            if st.button("Reiniciar Actividad"):
                st.session_state.eval_79 = False
                st.rerun()

# Módulo 2: Declaraciones (81 y 82)
elif modulo_seleccionado == "Art. 81 y 82: Declaraciones y Avisos":
    st.title("📋 Infracciones por Declaraciones y Avisos (Art. 81 y 82 CFF)")
    
    tab1, tab2 = st.tabs(["📖 Catálogo Exhaustivo", "📝 Evaluación Práctica"])
    
    with tab1:
        st.header("Estudio Literal de la Norma")
        for item in infracciones_81_82:
            with st.expander(f"📌 {item['fraccion']}"):
                st.write(f"**Tipicidad:** {item['infraccion']}")
                st.error(f"**Parámetro de Multa:**\n{item['multa']}")
                st.info(f"**Caso Hipotético:** {item['ejemplo']}")
                
    with tab2:
        st.header("Análisis de Casos Prácticos")
        if 'eval_81' not in st.session_state:
            st.session_state.eval_81 = False

        respuestas_usuario = {}
        with st.form("form_81"):
            for i, q in enumerate(quiz_81_82):
                st.write(f"**{q['pregunta']}**")
                respuestas_usuario[i] = st.radio("Elige el encuadre legal:", q['opciones'], key=f"q81_{i}", index=None)
                st.markdown("---")
                
            btn_calificar = st.form_submit_button("✅ Calificar Actividad")
            if btn_calificar:
                st.session_state.eval_81 = True

        if st.session_state.eval_81:
            aciertos = 0
            st.subheader("Resultados de la Subsunción")
            for i, q in enumerate(quiz_81_82):
                if respuestas_usuario[i] == q['respuesta']:
                    aciertos += 1
                    st.success(f"Caso {i+1}: Correcto. Fundamento aplicable: '{q['respuesta']}'.")
                else:
                    st.error(f"Caso {i+1}: Incorrecto. El encuadre legal exacto es: '{q['respuesta']}'.")
            
            st.metric(label="Calificación", value=f"{aciertos} / 10")
            if aciertos >= 8:
                st.balloons()
            
            if st.button("Reiniciar Actividad"):
                st.session_state.eval_81 = False
                st.rerun()
