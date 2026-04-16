import streamlit as st

# ==========================================
# BASE DE DATOS INTERNA: TRANSCRIPCIÓN EXACTA CFF
# ==========================================
infracciones_db = [
    {
        "articulo": "Art. 79, Fracción I",
        "tema": "Registro Federal de Contribuyentes (RFC)",
        "infraccion": "No solicitar la inscripción cuando se está obligado a ello o hacerlo extemporáneamente, salvo cuando la solicitud se presente de manera espontánea.",
        "multa_legal": "Art. 80, Fracción I: De $5,070.00 a $15,200.00.",
        "ejemplo": "Un estudiante organiza el grupo digital 'UDAL Emprendimiento' por WhatsApp para vender fundas y accesorios de telefonía móvil. Comienza a generar ingresos constantes mediante transferencias bancarias, pero nunca solicita su inscripción al SAT."
    },
    {
        "articulo": "Art. 79, Fracción III",
        "tema": "Registro Federal de Contribuyentes (RFC)",
        "infraccion": "No presentar los avisos al registro o hacerlo extemporáneamente, salvo cuando la presentación sea espontánea.",
        "multa_legal": "Art. 80, Fracción II: De $5,400.00 a $10,780.00.",
        "ejemplo": "Una productora independiente de cine de terror psicológico traslada su estudio de grabación de Cholula a Cuautlancingo, pero olvida presentar el aviso de cambio de domicilio fiscal ante la autoridad."
    },
    {
        "articulo": "Art. 79, Fracción IV",
        "tema": "Registro Federal de Contribuyentes (RFC)",
        "infraccion": "No citar la clave del registro o utilizar alguna no asignada por la autoridad fiscal, en las declaraciones, avisos, solicitudes, promociones y demás documentos que se presenten ante las autoridades fiscales y jurisdiccionales.",
        "multa_legal": "Art. 80, Fracción III: Multa entre el 2% de las contribuciones declaradas y $10,790.00 (mínimo $4,310.00).",
        "ejemplo": "Una clínica que ofrece servicios especializados para practicar inglés médico presenta sus solicitudes y promociones ante el SAT utilizando una homoclave genérica o inventada en lugar de la que le fue asignada oficialmente."
    },
    {
        "articulo": "Art. 81, Fracción I",
        "tema": "Declaraciones, Solicitudes y Avisos",
        "infraccion": "No presentar las declaraciones, las solicitudes, los avisos o las constancias que exijan las disposiciones fiscales, o no hacerlo a través de los medios electrónicos que señale la Secretaría de Hacienda y Crédito Público o presentarlos a requerimiento de las autoridades fiscales.",
        "multa_legal": "Art. 82, Fracción I, inciso a): De $2,050.00 a $25,360.00 por cada una de las obligaciones no declaradas.",
        "ejemplo": "Un abogado que litiga de forma independiente tiene una carga excesiva de trabajo en los tribunales y deja pasar el mes de abril sin presentar su declaración anual del Impuesto Sobre la Renta."
    },
    {
        "articulo": "Art. 81, Fracción IV",
        "tema": "Declaraciones, Solicitudes y Avisos",
        "infraccion": "No efectuar en los términos de las disposiciones fiscales los pagos provisionales de una contribución.",
        "multa_legal": "Art. 82, Fracción IV: De $12,240.00 a $24,480.00 (salvo contribuyentes obligados a pagos trimestrales/cuatrimestrales, que será de $1,220.00 a $7,340.00).",
        "ejemplo": "Un negocio local dedicado a la importación e instalación de dispositivos de domótica (enchufes inteligentes, controladores) calcula sus impuestos, pero omite realizar el pago provisional mensual en el portal bancario."
    },
    {
        "articulo": "Art. 83, Fracción I",
        "tema": "Contabilidad",
        "infraccion": "No llevar contabilidad.",
        "multa_legal": "Art. 84, Fracción I: De $2,220.00 a $22,110.00.",
        "ejemplo": "Un comerciante en un tianguis local que confecciona y vende sudaderas tipo 'oversize' con diseños de grafiti se niega a llevar los sistemas contables electrónicos obligatorios, anotando todo únicamente en una libreta."
    },
    {
        "articulo": "Art. 83, Fracción II",
        "tema": "Contabilidad",
        "infraccion": "No llevar algún libro o registro especial a que obliguen las leyes fiscales; no cumplir con las obligaciones sobre valuación de inventarios o no llevar el procedimiento de control de los mismos.",
        "multa_legal": "Art. 84, Fracción II: De $490.00 a $11,050.00.",
        "ejemplo": "Una empresa no lleva el registro de control de inventarios de su mercancía, imposibilitando a la autoridad verificar las entradas y salidas de sus productos de almacén."
    },
    {
        "articulo": "Art. 83, Fracción IV",
        "tema": "Contabilidad",
        "infraccion": "No hacer los asientos correspondientes a las operaciones efectuadas; hacerlos incompletos, inexactos, con identificación incorrecta de su objeto o fuera de los plazos respectivos, así como registrar gastos inexistentes.",
        "multa_legal": "Art. 84, Fracción III: De $290.00 a $5,330.00 (y de 55% a 75% del monto de cada registro de gasto inexistente).",
        "ejemplo": "El contador de una agencia de diseño registra las compras de equipo de cómputo tres meses después de la adquisición y con una clasificación inexacta en las pólizas contables."
    },
    {
        "articulo": "Art. 83, Fracción VII",
        "tema": "Contabilidad y Comprobantes",
        "infraccion": "No expedir, no entregar o no poner a disposición de los clientes los comprobantes fiscales digitales por Internet de sus actividades cuando las disposiciones fiscales lo establezcan, o expedirlos sin que cumplan los requisitos.",
        "multa_legal": "Art. 84, Fracción IV, inciso a): De $22,300.00 a $127,530.00. En caso de reincidencia, clausura preventiva de 3 a 15 días.",
        "ejemplo": "Un arrendador que renta departamentos a estudiantes universitarios se niega sistemáticamente a emitir los CFDI correspondientes al pago de las rentas mensuales, argumentando que 'no maneja facturas'."
    },
    {
        "articulo": "Art. 83, Fracción IX",
        "tema": "Contabilidad y Comprobantes",
        "infraccion": "Expedir comprobantes fiscales digitales por Internet asentando la clave del registro federal de contribuyentes de persona distinta a la que adquiere el bien o el servicio.",
        "multa_legal": "Art. 84, Fracción VI: De $21,420.00 a $122,440.00 por la primera infracción.",
        "ejemplo": "Una tienda de electrónica factura la venta de un smartphone de gama alta utilizando el RFC de un cliente diferente al que realizó la compra, negándose a cancelar y reexpedir el documento."
    }
]

# ==========================================
# BASE DE DATOS INTERNA: QUIZ EVALUATIVO
# ==========================================
quiz_db = [
    {
        "pregunta": "1. Un despacho de arquitectos se muda del centro de la ciudad a una plaza comercial, pero no actualiza su información ante el SAT. ¿Cuáles son los parámetros exactos de la multa que le corresponde por esta omisión (Art. 80, Fracc. II)?",
        "opciones": ["De $5,070.00 a $15,200.00", "De $5,400.00 a $10,780.00", "De $2,050.00 a $25,360.00", "De $22,300.00 a $127,530.00"],
        "respuesta_correcta": "De $5,400.00 a $10,780.00",
        "retroalimentacion": "Correcto. El no presentar avisos al registro (como el de cambio de domicilio) se fundamenta en el Art. 79 Fracc. III y se sanciona con los parámetros del Art. 80 Fracc. II."
    },
    {
        "pregunta": "2. Una empresa comercializadora se niega a emitir el CFDI a un cliente corporativo que acaba de realizar una compra de equipo. ¿Qué artículo y fracción del CFF está violando de manera directa?",
        "opciones": ["Art. 81, Fracción I", "Art. 83, Fracción VII", "Art. 79, Fracción I", "Art. 83, Fracción IV"],
        "respuesta_correcta": "Art. 83, Fracción VII",
        "retroalimentacion": "Correcto. La negativa a expedir, entregar o poner a disposición los CFDI se tipifica textualmente en el Art. 83, Fracción VII."
    },
    {
        "pregunta": "3. Un emprendedor de ventas por internet lleva 2 años operando y recibiendo ingresos sin solicitar su inscripción al RFC. Con base en el Art. 80, Fracción I, ¿cuál es la multa aplicable?",
        "opciones": ["De $22,300.00 a $127,530.00", "De $490.00 a $11,050.00", "De $5,070.00 a $15,200.00", "De $12,240.00 a $24,480.00"],
        "respuesta_correcta": "De $5,070.00 a $15,200.00",
        "retroalimentacion": "Correcto. Infringir el Art. 79 Fracc. I (No solicitar la inscripción) genera una multa de entre $5,070.00 a $15,200.00."
    },
    {
        "pregunta": "4. El contador de una refaccionaria registra los ingresos mensuales 60 días fuera del plazo legal respectivo en las pólizas de ingresos. ¿Qué artículo y fracción está violando respecto a la contabilidad?",
        "opciones": ["Art. 83, Fracción IV", "Art. 81, Fracción I", "Art. 83, Fracción I", "Art. 79, Fracción IV"],
        "respuesta_correcta": "Art. 83, Fracción IV",
        "retroalimentacion": "Correcto. Hacer los asientos contables incompletos, inexactos o fuera de los plazos respectivos es infracción del Art. 83, Fracción IV."
    },
    {
        "pregunta": "5. ¿Cuál es el parámetro de multa aplicable a una persona moral que presenta su declaración anual a requerimiento de la autoridad (fuera de plazo), según el Art. 82, Fracción I, inciso a)?",
        "opciones": ["De $290.00 a $5,330.00", "De $2,050.00 a $25,360.00", "De $21,420.00 a $122,440.00", "De $5,400.00 a $10,780.00"],
        "respuesta_correcta": "De $2,050.00 a $25,360.00",
        "retroalimentacion": "Correcto. La falta de presentación de declaraciones (Art. 81 Fracc. I) conlleva la multa estipulada en el Art. 82 Fracc. I, inciso a)."
    },
    {
        "pregunta": "6. Una persona física con actividad empresarial simplemente decide 'no llevar contabilidad' de ningún tipo. Al ser detectado en facultades de comprobación, ¿qué multa se le impone (Art. 84, Fracción I)?",
        "opciones": ["De $22,300.00 a $127,530.00", "De $5,070.00 a $15,200.00", "De $2,220.00 a $22,110.00", "De $490.00 a $11,050.00"],
        "respuesta_correcta": "De $2,220.00 a $22,110.00",
        "retroalimentacion": "Correcto. La infracción por no llevar contabilidad (Art. 83 Fracc. I) se sanciona según los parámetros del Art. 84 Fracc. I."
    },
    {
        "pregunta": "7. Un proveedor expide la factura de una maquinaria, pero asienta deliberadamente la clave del RFC de una empresa 'fantasma' en lugar de la del comprador real. ¿A qué sanción económica se enfrenta (Art. 84, Fracción VI)?",
        "opciones": ["De $21,420.00 a $122,440.00", "De $12,240.00 a $24,480.00", "De $2,050.00 a $25,360.00", "De $290.00 a $5,330.00"],
        "respuesta_correcta": "De $21,420.00 a $122,440.00",
        "retroalimentacion": "Correcto. Expedir un CFDI asentando la clave del RFC de persona distinta (Art. 83 Fracc. IX) genera una de las multas más altas del CFF."
    },
    {
        "pregunta": "8. Una constructora presenta ante el SAT un documento donde omite citar su clave del RFC, o utiliza una clave inventada. Según el Art. 80, Fracción III, la multa mínima fijada por el código es de:",
        "opciones": ["$2,050.00", "$4,310.00", "$5,070.00", "$22,300.00"],
        "respuesta_correcta": "$4,310.00",
        "retroalimentacion": "Correcto. El CFF estipula que la multa no será menor a $4,310.00 ni mayor a $10,790.00 (o 2% de las contribuciones)."
    },
    {
        "pregunta": "9. Si un establecimiento comercial es reincidente en la falta de expedición de Comprobantes Fiscales Digitales por Internet (CFDI), además de la sanción económica, ¿qué medida adicional procede según el CFF?",
        "opciones": ["Prisión de 3 a 5 años.", "Clausura preventiva de 3 a 15 días.", "Embargo precautorio inmediato de las cuentas bancarias.", "Suspensión definitiva del Registro Federal de Contribuyentes."],
        "respuesta_correcta": "Clausura preventiva de 3 a 15 días.",
        "retroalimentacion": "Correcto. El Art. 84, Fracción IV, inciso a) estipula claramente la clausura preventiva por reincidencia en la no emisión de comprobantes."
    },
    {
        "pregunta": "10. Una empresa maquiladora no efectúa el pago provisional del ISR del mes de mayo. Suponiendo que no está en régimen trimestral/cuatrimestral, ¿cuál es el parámetro de multa que le corresponde?",
        "opciones": ["De $12,240.00 a $24,480.00", "De $2,050.00 a $25,360.00", "De $2,220.00 a $22,110.00", "De $5,400.00 a $10,780.00"],
        "respuesta_correcta": "De $12,240.00 a $24,480.00",
        "retroalimentacion": "Correcto. No efectuar pagos provisionales en los términos de las disposiciones fiscales (Art. 81 Fracc. IV) se sanciona con base en el Art. 82 Fracc. IV."
    }
]

# ==========================================
# INTERFAZ DE STREAMLIT
# ==========================================
st.set_page_config(page_title="Simulador Exacto: Infracciones CFF", page_icon="📖", layout="wide")

st.title("📖 Simulador Exacto: Parámetros e Infracciones (CFF Vigente)")
st.markdown("""
Esta herramienta contiene la **transcripción íntegra y exacta** de las obligaciones fiscales fundamentales del CFF. 
Revisa los parámetros precisos de multas en el **Catálogo** y resuelve la **Actividad Final** para comprobar tu retención legal.
""")

tab1, tab2 = st.tabs(["📚 Catálogo de Infracciones Exactas", "📝 Actividad Final (Calificada)"])

# --- PESTAÑA 1: CATÁLOGO ---
with tab1:
    st.header("Catálogo de Estudio (Artículos 79 al 84 del CFF)")
    st.markdown("Revisa el texto legal, los montos vigentes y el ejemplo situacional.")
    
    for i, item in enumerate(infracciones_db):
        with st.expander(f"⚖️ {item['articulo']} - {item['tema']}"):
            st.markdown(f"**Texto de la Infracción:** {item['infraccion']}")
            st.error(f"**Parámetro de Multa:** {item['multa_legal']}")
            st.info(f"**Caso Práctico:** {item['ejemplo']}")

# --- PESTAÑA 2: ACTIVIDAD EVALUATIVA ---
with tab2:
    st.header("Actividad Final: Análisis de Casos y Parámetros")
    st.markdown("Selecciona la respuesta legalmente correcta con base en el catálogo de estudio.")
    
    if 'score_exacto' not in st.session_state:
        st.session_state.score_exacto = False

    respuestas_usuario = {}
    
    with st.form("quiz_exacto"):
        for i, q in enumerate(quiz_db):
            st.markdown(f"**{q['pregunta']}**")
            respuestas_usuario[i] = st.radio("Selecciona la opción correcta:", q['opciones'], key=f"q_{i}", index=None)
            st.markdown("---")
            
        submit_button = st.form_submit_button("✅ Enviar Respuestas y Obtener Calificación")
        
        if submit_button:
            st.session_state.score_exacto = True

    if st.session_state.score_exacto:
        st.subheader("Resultados y Retroalimentación Legal")
        score = 0
        
        for i, q in enumerate(quiz_db):
            resp_usuario = respuestas_usuario[i]
            if resp_usuario == q['respuesta_correcta']:
                score += 1
                st.success(f"**Pregunta {i+1}: Correcto.** {q['retroalimentacion']}")
            elif resp_usuario is None:
                st.warning(f"**Pregunta {i+1}: Sin responder.** La respuesta legal era: '{q['respuesta_correcta']}'. {q['retroalimentacion']}")
            else:
                st.error(f"**Pregunta {i+1}: Incorrecto.** Elegiste '{resp_usuario}'. La respuesta legal era: '{q['respuesta_correcta']}'. {q['retroalimentacion']}")
                
        st.metric(label="Calificación de la Actividad", value=f"{score} / {len(quiz_db)}")
        
        if score >= 8:
            st.balloons()
            st.success("¡Sobresaliente! Tienes un excelente manejo de las disposiciones textuales y parámetros del CFF.")
        elif score >= 6:
            st.warning("Aprobado. Se sugiere repasar los mínimos y máximos de las multas de los artículos 80, 82 y 84.")
        else:
            st.error("Es necesario regresar a la pestaña del Catálogo para estudiar la literalidad de la norma.")
        
        if st.button("Reiniciar Actividad"):
            st.session_state.score_exacto = False
            st.rerun()