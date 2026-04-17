# ====================================================================
# ARCHIVO: datos_cff.py
# BASE DE DATOS MAESTRA: INFRACCIONES Y MULTAS DEL CFF
# ====================================================================

# --------------------------------------------------------------------
# BLOQUE 1: REGISTRO FEDERAL DE CONTRIBUYENTES (ART. 79 Y 80)
# Exhaustividad: 100% (Fracciones I a X)
# --------------------------------------------------------------------
infracciones_79_80 = [
    {
        "fraccion": "Fracción I",
        "infraccion": "No solicitar la inscripción cuando se está obligado a ello o hacerlo extemporáneamente, salvo cuando la solicitud se presente de manera espontánea. Se excluye de responsabilidad por la comisión de esta infracción a las personas cuya solicitud de inscripción debe ser legalmente efectuada por otra, inclusive cuando dichas personas quede subsidiariamente obligadas a solicitar su inscripción.",
        "multa": "Art. 80, Fracción I: De $5,070.00 a $15,200.00.",
        "ejemplo": "Una persona física inicia operaciones de comercio electrónico y recibe ingresos constantes, pero omite deliberadamente darse de alta en el SAT."
    },
    {
        "fraccion": "Fracción II",
        "infraccion": "No presentar solicitud de inscripción a nombre de un tercero cuando legalmente se esté obligado a ello o hacerlo extemporáneamente, salvo cuando la solicitud se presente espontáneamente.",
        "multa": "Art. 80, Fracción I: De $5,070.00 a $15,200.00.",
        "ejemplo": "El albacea de una sucesión o el tutor legal de un menor que adquiere bienes inmuebles omite inscribir a su representado en el RFC."
    },
    {
        "fraccion": "Fracción III",
        "infraccion": "No presentar los avisos al registro o hacerlo extemporáneamente, salvo cuando la presentación sea espontánea.",
        "multa": "Art. 80, Fracción II: De $5,400.00 a $10,780.00. (Tratándose de contribuyentes del Título IV, Cap. II, Sec. II LISR, la multa será de $1,800.00 a $3,600.00).",
        "ejemplo": "Una empresa traslada su almacén y oficinas administrativas a otro municipio, pero no presenta el aviso de cambio de domicilio fiscal."
    },
    {
        "fraccion": "Fracción IV",
        "infraccion": "No citar la clave del registro o utilizar alguna no asignada por la autoridad fiscal, en las declaraciones, avisos, solicitudes, promociones y demás documentos que se presenten ante las autoridades fiscales y jurisdiccionales, cuando se esté obligado conforme a la Ley.",
        "multa": "Art. 80, Fracción III: a) Tratándose de declaraciones: entre el 2% de las contribuciones declaradas y $10,790.00 (mínimo $4,310.00). b) En los demás documentos: De $1,310.00 a $3,010.00.",
        "ejemplo": "Al presentar un recurso de revocación ante la autoridad fiscal, el representante legal asienta una homoclave del RFC que no le corresponde a la empresa."
    },
    {
        "fraccion": "Fracción V",
        "infraccion": "Autorizar actas constitutivas, de fusión, escisión o liquidación de personas morales, sin cumplir lo dispuesto por el artículo 27 de este Código.",
        "multa": "Art. 80, Fracción IV: De $25,360.00 a $50,710.00.",
        "ejemplo": "Un Notario Público formaliza el acta constitutiva de una sociedad anónima sin asentar los RFC de los socios ni cumplir los requisitos del Art. 27 del CFF."
    },
    {
        "fraccion": "Fracción VI",
        "infraccion": "Señalar como domicilio fiscal para efectos del registro federal de contribuyentes, un lugar distinto del que corresponda conforme al Artículo 10.",
        "multa": "Art. 80, Fracción I: De $5,070.00 a $15,200.00.",
        "ejemplo": "Un contribuyente con su negocio operativo en la capital del estado señala como domicilio fiscal un terreno baldío en una zona rural para evadir notificaciones."
    },
    {
        "fraccion": "Fracción VII",
        "infraccion": "No asentar o asentar incorrectamente en las actas de asamblea o libros de socios o accionistas, la clave en el registro federal de contribuyentes de cada socio o accionista, a que se refiere el artículo 27, apartado B, fracción V de este Código.",
        "multa": "Art. 80, Fracción V: De $5,030.00 a $15,160.00.",
        "ejemplo": "El administrador de una empresa actualiza el libro corporativo de accionistas, pero registra solo los nombres y omite el RFC de los inversionistas."
    },
    {
        "fraccion": "Fracción VIII",
        "infraccion": "No asentar o asentar incorrectamente en las escrituras públicas en que hagan constar actas constitutivas y demás actas de asamblea de personas morales cuyos socios o accionistas deban solicitar su inscripción en el registro federal de contribuyentes, la clave correspondiente a cada socio o accionista... cuando los socios concurran.",
        "multa": "Art. 80, Fracción VI: De $21,560.00 a $43,140.00.",
        "ejemplo": "Durante una asamblea extraordinaria con todos los socios presentes, el Corredor Público no asienta el RFC de dos de ellos en la póliza respectiva."
    },
    {
        "fraccion": "Fracción IX",
        "infraccion": "No verificar que la clave del registro federal de contribuyentes aparezca en los documentos a que hace referencia la fracción anterior, cuando los socios o accionistas no concurran a la constitución de la sociedad o a la protocolización del acta respectiva.",
        "multa": "Art. 80, Fracción VI: De $21,560.00 a $43,140.00.",
        "ejemplo": "Un socio extranjero envía a su apoderado a la protocolización de un acta, y el fedatario no verifica que el RFC del socio ausente conste en los documentos presentados."
    },
    {
        "fraccion": "Fracción X",
        "infraccion": "No atender los requerimientos realizados por la autoridad fiscal, en el plazo concedido, respecto de corroborar la autenticidad, la validación o envío de instrumentos notariales para efectos de la inscripción o actualización en el registro federal de contribuyentes...",
        "multa": "Art. 80, Fracción VI: De $21,560.00 a $43,140.00.",
        "ejemplo": "El SAT requiere a un Notario para que valide la autenticidad de un acta constitutiva enviada por un contribuyente, y el Notario deja vencer el plazo sin responder."
    }
]

# Quiz exhaustivo Artículos 79 y 80
quiz_79_80 = [
    {
        "pregunta": "1. Un Notario autoriza la fusión de dos empresas sin cumplir lo dispuesto por el artículo 27 del CFF. ¿Cuál es la multa exacta aplicable según el Art. 80, Fracción IV?",
        "opciones": ["De $5,070.00 a $15,200.00", "De $25,360.00 a $50,710.00", "De $21,560.00 a $43,140.00", "De $5,400.00 a $10,780.00"],
        "respuesta": "De $25,360.00 a $50,710.00"
    },
    {
        "pregunta": "2. Una escuela señala como domicilio fiscal un apartado postal en lugar del inmueble donde realiza sus actividades (Art. 79, Fracc. VI). ¿A qué multa se hace acreedora (Art. 80, Fracc. I)?",
        "opciones": ["De $5,070.00 a $15,200.00", "De $5,400.00 a $10,780.00", "De $21,560.00 a $43,140.00", "De $1,310.00 a $3,010.00"],
        "respuesta": "De $5,070.00 a $15,200.00"
    },
    {
        "pregunta": "3. Se presenta una declaración fiscal pero se asienta un RFC no asignado por la autoridad. Según el Art. 80, Fracción III, inciso a), la multa NO será menor de:",
        "opciones": ["$1,310.00", "$4,310.00", "$5,070.00", "$10,790.00"],
        "respuesta": "$4,310.00"
    },
    {
        "pregunta": "4. Una empresa traslada sus oficinas y olvida presentar el aviso de cambio de domicilio. ¿Cuál es el parámetro de la multa general aplicable por la Fracción III del Art. 79?",
        "opciones": ["De $5,070.00 a $15,200.00", "De $5,400.00 a $10,780.00", "De $1,800.00 a $3,600.00", "De $21,560.00 a $43,140.00"],
        "respuesta": "De $5,400.00 a $10,780.00"
    },
    {
        "pregunta": "5. El administrador de una SA de CV no asienta el RFC de sus accionistas en el libro corporativo (Fracc. VII). ¿Cuál es la multa según el Art. 80, Fracción V?",
        "opciones": ["De $5,070.00 a $15,200.00", "De $25,360.00 a $50,710.00", "De $5,030.00 a $15,160.00", "De $21,560.00 a $43,140.00"],
        "respuesta": "De $5,030.00 a $15,160.00"
    },
    {
        "pregunta": "6. Un tutor que está legalmente obligado a solicitar la inscripción de un tercero (Fracc. II) omite hacerlo. ¿Qué multa corresponde (Art. 80, Fracc. I)?",
        "opciones": ["De $5,070.00 a $15,200.00", "De $5,400.00 a $10,780.00", "De $25,360.00 a $50,710.00", "De $1,310.00 a $3,010.00"],
        "respuesta": "De $5,070.00 a $15,200.00"
    },
    {
        "pregunta": "7. El SAT requiere a un Corredor Público corroborar un instrumento notarial para actualización del RFC y este no atiende el requerimiento en plazo (Fracc. X). ¿Cuál es la sanción económica?",
        "opciones": ["De $5,030.00 a $15,160.00", "De $21,560.00 a $43,140.00", "De $25,360.00 a $50,710.00", "De $5,400.00 a $10,780.00"],
        "respuesta": "De $21,560.00 a $43,140.00"
    },
    {
        "pregunta": "8. Se presenta un recurso de revocación (no es declaración) y se asienta un RFC inventado. Al tratarse de 'otros documentos' (Art. 80, Fracc. III, inciso b), la multa es de:",
        "opciones": ["De $4,310.00 a $10,790.00", "De $1,310.00 a $3,010.00", "De $5,070.00 a $15,200.00", "De $5,030.00 a $15,160.00"],
        "respuesta": "De $1,310.00 a $3,010.00"
    },
    {
        "pregunta": "9. En la protocolización de un acta donde los socios no concurren, el fedatario no verifica que el RFC aparezca en los documentos (Fracc. IX). ¿Qué multa se aplica?",
        "opciones": ["De $5,030.00 a $15,160.00", "De $21,560.00 a $43,140.00", "De $25,360.00 a $50,710.00", "De $5,070.00 a $15,200.00"],
        "respuesta": "De $21,560.00 a $43,140.00"
    },
    {
        "pregunta": "10. Una persona física recibe ingresos por arrendamiento pero no solicita su inscripción al RFC, violando la Fracción I del Artículo 79. Su multa será de:",
        "opciones": ["De $5,070.00 a $15,200.00", "De $5,400.00 a $10,780.00", "De $1,800.00 a $3,600.00", "De $1,310
# --------------------------------------------------------------------
# BLOQUE 2: DECLARACIONES, AVISOS Y REPORTES (ART. 81 Y 82)
# Exhaustividad: 100% (Fracciones I a XLVI, incluyendo derogadas)
# --------------------------------------------------------------------
infracciones_81_82 = [
    {
        "fraccion": "Fracción I",
        "infraccion": "No presentar las declaraciones, las solicitudes, los avisos o las constancias que exijan las disposiciones fiscales, no hacerlo a través de los medios electrónicos que señale la SHCP o presentarlos a requerimiento... No cumplir los requerimientos de las autoridades o no presentar reportes del art. 28, fracc. I, ap. B.",
        "multa": "Art. 82, Fracc. I:\na) $2,050 a $25,360 (declaraciones omitidas)\nb) $2,050 a $50,710 (fuera de plazo o incumplimiento)\nc) $19,460 a $38,890 (no presentar aviso art. 23)\nd) $20,790 a $41,590 (medios electrónicos)\ne) $18,360 a $36,740 (reportes art. 28)\nf) $2,080 a $6,660 (demás documentos)",
        "ejemplo": "Un contribuyente no presenta su declaración anual y omite enviar los reportes de controles volumétricos."
    },
    {
        "fraccion": "Fracción II",
        "infraccion": "Presentar las declaraciones, las solicitudes, los avisos, la información del art. 17-K... incompletos, con errores o en forma distinta a lo señalado por las disposiciones fiscales, o bien en medios electrónicos.",
        "multa": "Art. 82, Fracc. II:\na) $1,520 a $5,070 (nombre/domicilio equivocado)\nb) $30 a $140 (por dato de clientes/proveedores)\nc) $270 a $500 (por dato incorrecto en anexos)\nd) $1,020 a $2,520 (actividad preponderante)\ne) $6,230 a $20,790 (medios electrónicos incompletos/errores)\nf) $1,830 a $5,500 (sin firma)\ng) $920 a $2,500 (demás casos)",
        "ejemplo": "Se presenta la declaración informativa pero el contador asienta mal el RFC de 50 proveedores."
    },
    {
        "fraccion": "Fracción III",
        "infraccion": "No pagar las contribuciones dentro del plazo que establecen las disposiciones fiscales, cuando se trate de contribuciones que no sean determinables por los contribuyentes, salvo pago espontáneo.",
        "multa": "Art. 82, Fracc. III: De $2,050.00 a $50,710.00, por cada requerimiento.",
        "ejemplo": "No pagar un impuesto aduanero determinado previamente por la autoridad en el plazo legal."
    },
    {
        "fraccion": "Fracción IV",
        "infraccion": "No efectuar en los términos de las disposiciones fiscales los pagos provisionales de una contribución.",
        "multa": "Art. 82, Fracc. IV: De $25,360.00 a $50,710.00 (Salvo pagos trimestrales/cuatrimestrales: de $2,520.00 a $15,200.00).",
        "ejemplo": "Una empresa comercializadora omite efectuar su pago provisional mensual de ISR de agosto."
    },
    {
        "fraccion": "Fracción V",
        "infraccion": "No proporcionar la información de las personas a las que les hubiera entregado cantidades en efectivo por concepto de subsidio para el empleo... o presentarla fuera del plazo.",
        "multa": "Art. 82, Fracc. V: De $17,410.00 a $34,870.00.",
        "ejemplo": "Un patrón entrega subsidio al empleo en efectivo a sus operarios pero no envía la relación al SAT."
    },
    {
        "fraccion": "Fracción VI",
        "infraccion": "No presentar aviso de cambio de domicilio o presentarlo fuera de los plazos que señale el Reglamento de este Código, salvo presentación espontánea.",
        "multa": "Art. 82, Fracc. VI: De $5,070.00 a $15,200.00.",
        "ejemplo": "Una oficina de abogados se muda a otra colonia y no actualiza su domicilio fiscal."
    },
    {
        "fraccion": "Fracción VII",
        "infraccion": "No presentar la información manifestando las razones por las cuales no se determina impuesto a pagar o saldo a favor, por alguna de las obligaciones (art. 31, sexto párrafo).",
        "multa": "Art. 82, Fracc. VII: De $1,260.00 a $12,790.00.",
        "ejemplo": "Una empresa cierra en ceros el mes y no presenta la declaración estadística justificando la falta de impuesto a cargo."
    },
    {
        "fraccion": "Fracción VIII",
        "infraccion": "No presentar la información a que se refieren los artículos 17 de la Ley del Impuesto sobre Tenencia o Uso de Vehículos o 19, fracciones VIII, IX y XII, de la Ley del IEPS...",
        "multa": "Art. 82, Fracc. VIII: De $96,230.00 a $288,660.00.",
        "ejemplo": "Una ensambladora omite enviar los reportes del IEPS correspondientes a la producción de ciertos bienes."
    },
    {
        "fraccion": "Fracción IX",
        "infraccion": "No proporcionar la información a que se refiere el artículo 20, décimo primer párrafo de este Código, en los plazos que establecen las disposiciones fiscales.",
        "multa": "Art. 82, Fracc. IX: De $15,200.00 a $50,710.00.",
        "ejemplo": "Omisión de información relativa a índices y recargos específicos requeridos por la ley."
    },
    {
        "fraccion": "Fracción X",
        "infraccion": "No cumplir, en la forma y términos señalados, con lo establecido en la fracción IV del artículo 29 de este Código.",
        "multa": "Art. 82, Fracc. X: De $14,100.00 a $26,430.00.",
        "ejemplo": "Un proveedor de certificación de CFDI no envía al SAT las copias de los comprobantes que certificó."
    },
    {
        "fraccion": "Fracción XI",
        "infraccion": "No incluir a todas las sociedades integradas en la solicitud de autorización para determinar el resultado fiscal integrado... o no incorporar a todas en el régimen opcional para grupos de sociedades.",
        "multa": "Art. 82, Fracc. XI: De $165,010.00 a $220,020.00 por cada sociedad no incluida.",
        "ejemplo": "Un corporativo consolida sus resultados pero deja fuera a una de sus subsidiarias estratégicamente."
    },
    {
        "fraccion": "Fracción XII",
        "infraccion": "No presentar los avisos de incorporación o desincorporación al régimen opcional para grupos de sociedades... o presentarlos extemporáneamente.",
        "multa": "Art. 82, Fracc. XII: De $65,930.00 a $101,470.00 por cada aviso no presentado.",
        "ejemplo": "Un holding adquiere una nueva empresa y no avisa al SAT de su incorporación al grupo."
    },
    {
        "fraccion": "Fracción XIII",
        "infraccion": "(Se deroga).",
        "multa": "Art. 82, Fracc. XIII (Compilada): De $15,200.00 a $50,710.00.",
        "ejemplo": "Disposición derogada en el tipo de la conducta, pero la multa se mantiene tabulada en el Art. 82."
    },
    {
        "fraccion": "Fracción XIV",
        "infraccion": "No proporcionar la información de las operaciones efectuadas en el año de calendario anterior, a través de fideicomisos por los que se realicen actividades empresariales...",
        "multa": "Art. 82, Fracc. XIV: De $15,200.00 a $35,490.00.",
        "ejemplo": "Un banco fiduciario no entrega el reporte anual de los fideicomisos empresariales que administra."
    },
    {
        "fraccion": "Fracción XV",
        "infraccion": "(Se deroga).",
        "multa": "Art. 82, Fracc. XV (Compilada): De $126,820.00 a $253,640.00.",
        "ejemplo": "Disposición derogada."
    },
    {
        "fraccion": "Fracción XVI",
        "infraccion": "No proporcionar la información a que se refiere la fracción V del artículo 32 de la LIVA... o presentarla incompleta o con errores.",
        "multa": "Art. 82, Fracc. XVI: De $15,650.00 a $31,290.00. (Reincidencia aumenta al 100%).",
        "ejemplo": "Un contribuyente no presenta la DIOT (Declaración Informativa de Operaciones con Terceros)."
    },
    {
        "fraccion": "Fracción XVII",
        "infraccion": "No presentar la declaración informativa de las operaciones efectuadas con partes relacionadas... o presentarla incompleta o con errores.",
        "multa": "Art. 82, Fracc. XVII: De $112,750.00 a $225,500.00.",
        "ejemplo": "Una multinacional no reporta las transferencias hechas a su matriz en el extranjero."
    },
    {
        "fraccion": "Fracción XVIII",
        "infraccion": "No proporcionar la información a que se refiere el artículo 19, fracciones II, tercer párrafo, XIII y XV de la Ley del IEPS.",
        "multa": "Art. 82, Fracc. XVIII: De $14,380.00 a $23,940.00.",
        "ejemplo": "Un productor de bebidas alcohólicas no proporciona el reporte de lectura de sus medidores."
    },
    {
        "fraccion": "Fracción XIX",
        "infraccion": "No proporcionar la información a que se refiere el artículo 19, fracciones X y XVI de la Ley del IEPS.",
        "multa": "Art. 82, Fracc. XIX: De $23,940.00 a $47,930.00.",
        "ejemplo": "Omisión de presentar la información de marbetes y precintos destruidos."
    },
    {
        "fraccion": "Fracción XX",
        "infraccion": "No presentar el aviso a que se refiere el último párrafo del artículo 9o. de este Código.",
        "multa": "Art. 82, Fracc. XX: De $7,680.00 a $15,350.00.",
        "ejemplo": "No presentar el aviso de suspensión temporal o de reanudación de actividades cuando la ley lo exige."
    },
    {
        "fraccion": "Fracción XXI",
        "infraccion": "No registrarse de conformidad con lo dispuesto en el artículo 19, fracciones XI y XIV de la Ley del IEPS.",
        "multa": "Art. 82, Fracc. XXI: De $183,460.00 a $366,950.00.",
        "ejemplo": "Un importador de tabacos labrados no se inscribe en el padrón sectorial correspondiente."
    },
    {
        "fraccion": "Fracción XXII",
        "infraccion": "No proporcionar la información relativa del interés real pagado por el contribuyente... por créditos hipotecarios (fracc IV art 151 LISR).",
        "multa": "Art. 82, Fracc. XXII: De $7,680.00 a $15,350.00 por cada informe.",
        "ejemplo": "Una institución financiera no le entrega a su cliente la constancia de intereses reales de su hipoteca."
    },
    {
        "fraccion": "Fracción XXIII",
        "infraccion": "No proporcionar la información a que se refiere el penúltimo párrafo de la fracción VIII del artículo 29 de la LIVA o presentarla incompleta o con errores.",
        "multa": "Art. 82, Fracc. XXIII: De $22,010.00 a $40,360.00.",
        "ejemplo": "Omisión en reportes específicos de la Ley del IVA por parte de residentes en el extranjero."
    },
    {
        "fraccion": "Fracción XXIV",
        "infraccion": "No proporcionar la constancia a que se refiere la fracción II del artículo 55 de la LISR.",
        "multa": "Art. 82, Fracc. XXIV: De $7,680.00 a $15,350.00 por cada constancia.",
        "ejemplo": "Un banco no proporciona la constancia de retenciones de ISR por el pago de rendimientos o dividendos."
    },
    {
        "fraccion": "Fracción XXV",
        "infraccion": "No dar cumplimiento a lo dispuesto en el art 28, fracc I (Controles volumétricos). (Incisos a al i).",
        "multa": "Art. 82, Fracc. XXV:\na) $39,360 a $69,160.\nb) $1,124,500 a $1,686,750 (sin dictamen).\nc) $2,249,000 a $3,373,500 + clausura (registro distinto).\nd) $3,373,500 a $5,622,500 + clausura (sin equipos).\ne, f, g, h) $39,360 a $69,160 por reporte omitido/erróneo.\ni) Doble clausura por destrucción de sellos.",
        "ejemplo": "Una gasolinera altera los programas informáticos de controles volumétricos para registrar menos combustible vendido (Inciso d)."
    },
    {
        "fraccion": "Fracción XXVI",
        "infraccion": "No proporcionar la información de la fracción VIII del art 32 de la LIVA (Plataformas digitales).",
        "multa": "Art. 82, Fracc. XXVI: De $14,880.00 a $29,750.00 (100% de aumento en reincidencia).",
        "ejemplo": "Una plataforma de transporte (apps de viaje) no entrega la información de las operaciones de sus conductores."
    },
    {
        "fraccion": "Fracción XXVII",
        "infraccion": "No proporcionar la información a que se refiere el artículo 32-G de este Código (órganos de gobierno).",
        "multa": "Art. 82, Fracc. XXVII: De $17,410.00 a $34,870.00.",
        "ejemplo": "Un municipio no entrega el reporte de retenciones realizadas a sus trabajadores y proveedores."
    },
    {
        "fraccion": "Fracción XXVIII",
        "infraccion": "No cumplir con la obligación a que se refiere la fracción IV del artículo 98 de la LISR.",
        "multa": "Art. 82, Fracc. XXVIII: De $1,050.00 a $1,580.00.",
        "ejemplo": "Un trabajador no le comunica a su patrón que él mismo presentará su declaración anual."
    },
    {
        "fraccion": "Fracción XXIX",
        "infraccion": "No proporcionar la información señalada en el artículo 30-A de este Código o presentarla incompleta o con errores.",
        "multa": "Art. 82, Fracc. XXIX: De $70,600.00 a $353,010.00. (Reincidencia: $141,180 a $706,020).",
        "ejemplo": "Omisión de información respecto al uso de monederos electrónicos y vales de despensa autorizados."
    },
    {
        "fraccion": "Fracción XXX",
        "infraccion": "No proporcionar documentación comprobatoria que ampare que acciones objeto de autorización no han salido del grupo de sociedades.",
        "multa": "Art. 82, Fracc. XXX: De $231,010.00 a $328,900.00.",
        "ejemplo": "Un corporativo reestructura acciones y no comprueba que el control sigue en la misma entidad holding."
    },
    {
        "fraccion": "Fracción XXXI",
        "infraccion": "No proporcionar información de los arts 76, 82, 110, 118 y 128 LISR, o en forma extemporánea.",
        "multa": "Art. 82, Fracc. XXXI: De $231,010.00 a $328,900.00.",
        "ejemplo": "Fideicomisos inmobiliarios (FIBRAS) que no reportan los rendimientos distribuidos."
    },
    {
        "fraccion": "Fracciones XXXII, XXXIII y XXXV",
        "infraccion": "(Se derogan).",
        "multa": "N/A",
        "ejemplo": "Disposiciones derogadas."
    },
    {
        "fraccion": "Fracción XXXIV",
        "infraccion": "No proporcionar datos, informes o documentos solicitados por autoridades conforme al art 42-A.",
        "multa": "Art. 82, Fracc. XXXIV: De $29,930.00 a $49,870.00 por cada solicitud no atendida.",
        "ejemplo": "Instituciones de crédito que no informan estados de cuenta requeridos sin ejercer facultades de comprobación."
    },
    {
        "fraccion": "Fracciones XXXVI, XXXVII, XXXVIII, XLII y XLIV",
        "infraccion": "No cumplir obligaciones del art 82 LISR (donatarias: estructura, gobierno corporativo, restricciones).",
        "multa": "Art. 82, Fracc. XXXVI: De $114,770.00 a $143,450.00, y cancelación de autorización para recibir donativos.",
        "ejemplo": "Una donataria interviene en campañas políticas (infracción al art 82 LISR)."
    },
    {
        "fraccion": "Fracción XXXIX",
        "infraccion": "No destinar la totalidad del patrimonio o donativos en los términos del art 82, fracc V LISR.",
        "multa": "Art. 82, Fracc. XXXIX: De $201,610.00 a $287,040.00.",
        "ejemplo": "Al liquidarse una asociación civil donataria, los socios se reparten el patrimonio en lugar de pasarlo a otra donataria."
    },
    {
        "fraccion": "Fracción XL",
        "infraccion": "No proporcionar información de los arts 31-A CFF y 76-A LISR (Operaciones relevantes / BEPS).",
        "multa": "Art. 82, Fracc. XXXVII: De $226,000.00 a $321,770.00.",
        "ejemplo": "Una transnacional omite entregar el Reporte Maestro (Master File) o País por País (CbC)."
    },
    {
        "fraccion": "Fracción XLI",
        "infraccion": "No ingresar la información contable a través de la página del SAT estando obligado (Contabilidad Electrónica).",
        "multa": "Art. 82, Fracc. XXXVIII: De $8,050.00 a $24,130.00.",
        "ejemplo": "Una empresa no sube la balanza de comprobación y catálogo de cuentas mensual en formato XML."
    },
    {
        "fraccion": "Fracción XLIII",
        "infraccion": "(Se deroga).",
        "multa": "N/A",
        "ejemplo": "Disposición derogada DOF 12-11-2021."
    },
    {
        "fraccion": "Fracción XLV",
        "infraccion": "Cuando el contratista no cumpla con la obligación de entregar información y documentación (Subcontratación especializada / REPSE).",
        "multa": "Art. 82, Fracc. XLI: De $196,540.00 a $393,090.00 por cada obligación no cumplida.",
        "ejemplo": "Una empresa de limpieza subcontratada no le entrega a su cliente copia de los pagos de IMSS y nómina de los trabajadores."
    },
    {
        "fraccion": "Fracción XLVI",
        "infraccion": "No cancelar los CFDI de ingresos cuando se hayan emitido por error o sin causa, o cancelarlos fuera de plazo.",
        "multa": "Art. 82, Fracc. XLII: Del 5% a un 10% del monto de cada comprobante fiscal.",
        "ejemplo": "Emitir una factura por 1 millón de pesos por error a un cliente y nunca realizar el proceso de cancelación en el SAT."
    }
]

# Quiz exhaustivo Artículos 81 y 82
quiz_81_82 = [
    {
        "pregunta": "1. Una donataria autorizada destina parte de su patrimonio a fines personales de los socios, violando la Fracción XXXIX del Art. 81. ¿Cuál es su multa según el Art. 82?",
        "opciones": ["De $201,610.00 a $287,040.00", "De $114,770.00 a $143,450.00", "De $226,000.00 a $321,770.00", "Cancelación automática de la autorización solamente"],
        "respuesta": "De $201,610.00 a $287,040.00"
    },
    {
        "pregunta": "2. Una plataforma de entrega de comida a domicilio (plataforma digital) no proporciona la información de la fracción VIII del Art. 32 LIVA (Fracc. XXVI). ¿Qué multa se aplica?",
        "opciones": ["De $14,880.00 a $29,750.00", "De $15,650.00 a $31,290.00", "De $7,680.00 a $15,350.00", "De $1,050.00 a $1,580.00"],
        "respuesta": "De $14,880.00 a $29,750.00"
    },
    {
        "pregunta": "3. Se presenta una declaración informativa en medios electrónicos pero el archivo XML contiene 10 errores de estructura y captura. ¿Qué multa corresponde (Art. 82, Fracc. II, inciso e)?",
        "opciones": ["De $6,230.00 a $20,790.00", "De $30.00 a $140.00 por cada error", "De $270.00 a $500.00 por cada error", "De $1,520.00 a $5,070.00"],
        "respuesta": "De $6,230.00 a $20,790.00"
    },
    {
        "pregunta": "4. Una gasolinera altera los programas de controles volumétricos (Art. 81, Fracc. XXV, inciso d). ¿Cuál es la severa sanción económica prevista por el Art. 82, Fracc. XXV?",
        "opciones": ["De $3,373,500.00 a $5,622,500.00 y clausura", "De $1,124,500.00 a $1,686,750.00", "De $39,360.00 a $69,160.00", "Doble de la clausura impuesta previamente"],
        "respuesta": "De $3,373,500.00 a $5,622,500.00 y clausura"
    },
    {
        "pregunta": "5. El cliente detecta una factura millonaria emitida por error hacia él, pero el emisor se niega a cancelarla fuera de plazo (Fracc. XLVI). ¿Cómo se tasa la multa del infractor?",
        "opciones": ["Del 5% a un 10% del monto del comprobante", "De $196,540.00 a $393,090.00", "De $2,050.00 a $25,360.00", "De $8,050.00 a $24,130.00"],
        "respuesta": "Del 5% a un 10% del monto del comprobante"
    },
    {
        "pregunta": "6. Una empresa de servicios de subcontratación especializada (REPSE) no le entrega los recibos de nómina a su contratante (Fracc. XLV). ¿Cuál es el parámetro de la multa?",
        "opciones": ["De $196,540.00 a $393,090.00", "De $226,000.00 a $321,770.00", "De $29,930.00 a $49,870.00", "De $114,770.00 a $143,450.00"],
        "respuesta": "De $196,540.00 a $393,090.00"
    },
    {
        "pregunta": "7. Un banco no le expide a su cliente la constancia anual de intereses reales hipotecarios para que deduzca en su declaración (Fracc. XXII). ¿A cuánto asciende la sanción por cada constancia no entregada?",
        "opciones": ["De $7,680.00 a $15,350.00", "De $22,010.00 a $40,360.00", "De $1,050.00 a $1,580.00", "De $14,880.00 a $29,750.00"],
        "respuesta": "De $7,680.00 a $15,350.00"
    },
    {
        "pregunta": "8. Una persona moral presenta su declaración pero el representante legal olvida firmarla electrónicamente. ¿Cuál es el monto de la multa (Art. 82, Fracc. II, inciso f)?",
        "opciones": ["De $1,830.00 a $5,500.00", "De $920.00 a $2,500.00", "De $1,020.00 a $2,520.00", "De $270.00 a $500.00"],
        "respuesta": "De $1,830.00 a $5,500.00"
    },
    {
        "pregunta": "9. Una empresa no sube su contabilidad electrónica (balanzas de comprobación) al portal del SAT (Fracc. XLI). Según la Fracción XXXVIII del Art. 82, la multa es de:",
        "opciones": ["De $8,050.00 a $24,130.00", "De $17,410.00 a $34,870.00", "De $5,070.00 a $15,200.00", "De $2,050.00 a $50,710.00"],
        "respuesta": "De $8,050.00 a $24,130.00"
    },
    {
        "pregunta": "10. Se presenta un aviso fuera del plazo requerido (ej. cambio de domicilio), actualizando la Fracción VI del Art. 81. La multa aplicable es de:",
        "opciones": ["De $5,070.00 a $15,200.00", "De $1,260.00 a $12,790.00", "De $17,410.00 a $34,870.00", "De $25,360.00 a $50,710.00"],
        "respuesta": "De $5,070.00 a $15,200.00"
    }
]