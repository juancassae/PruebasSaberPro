import streamlit as st
import pandas as pd
import sklearn 
import pickle

def transform_data(data):
    categorical_columns = data.select_dtypes(include=['object', 'category']).columns.tolist()
    ordinal_columns = ['ESTU_VALORMATRICULAUNIVERSIDAD', 'ESTU_HORASSEMANATRABAJA','FAMI_EDUCACIONPADRE','FAMI_ESTRATOVIVIENDA','FAMI_EDUCACIONMADRE']
    nominal_columns = [col for col in categorical_columns if col not in ordinal_columns]

    ordinal_categories = {
        'ESTU_VALORMATRICULAUNIVERSIDAD': ['No pagó matrícula','Menos de 500 mil', 'Entre 500 mil y menos de 1 millón', 'Entre 1 millón y menos de 2.5 millones','Entre 2.5 millones y menos de 4 millones','Entre 4 millones y menos de 5.5 millones','Entre 5.5 millones y menos de 7 millones','Más de 7 millones'], 
        'ESTU_HORASSEMANATRABAJA': ['0','Menos de 10 horas', 'Entre 11 y 20 horas', 'Entre 21 y 30 horas','Más de 30 horas'],
        'FAMI_EDUCACIONPADRE': ['No Aplica','No sabe','Ninguno','Primaria incompleta','Primaria completa','Secundaria (Bachillerato) incompleta',
    'Secundaria (Bachillerato) completa','Técnica o tecnológica incompleta','Técnica o tecnológica completa','Educación profesional incompleta','Educación profesional completa','Postgrado'],
        'FAMI_ESTRATOVIVIENDA': ['Sin Estrato', 'Estrato 1','Estrato 2', 'Estrato 3', 'Estrato 4', 'Estrato 5', 'Estrato 6'],
        'FAMI_EDUCACIONMADRE': ['No Aplica','No sabe','Ninguno','Primaria incompleta','Primaria completa','Secundaria (Bachillerato) incompleta',
    'Secundaria (Bachillerato) completa','Técnica o tecnológica incompleta','Técnica o tecnológica completa','Educación profesional incompleta','Educación profesional completa','Postgrado']
    }


    data_encoded = pd.get_dummies(data, columns=nominal_columns, drop_first=True)


    ordinal_encoder = sklearn.preprocessing.OrdinalEncoder(categories=[ordinal_categories[ord_var] for ord_var in ordinal_columns])
    data_encoded[ordinal_columns] = ordinal_encoder.fit_transform(data[ordinal_columns])
    col_names = ['ESTU_VALORMATRICULAUNIVERSIDAD', 'ESTU_HORASSEMANATRABAJA', 'FAMI_EDUCACIONPADRE', 'FAMI_ESTRATOVIVIENDA', 'FAMI_EDUCACIONMADRE', 'ESTU_DEPTO_PRESENTACION_ANTIOQUIA', 'ESTU_DEPTO_PRESENTACION_ARAUCA', 'ESTU_DEPTO_PRESENTACION_ATLANTICO', 'ESTU_DEPTO_PRESENTACION_BOGOTÁ', 'ESTU_DEPTO_PRESENTACION_BOLIVAR', 'ESTU_DEPTO_PRESENTACION_BOYACA', 'ESTU_DEPTO_PRESENTACION_CALDAS', 'ESTU_DEPTO_PRESENTACION_CAQUETA', 'ESTU_DEPTO_PRESENTACION_CASANARE', 'ESTU_DEPTO_PRESENTACION_CAUCA', 'ESTU_DEPTO_PRESENTACION_CESAR', 'ESTU_DEPTO_PRESENTACION_CHOCO', 'ESTU_DEPTO_PRESENTACION_CORDOBA', 'ESTU_DEPTO_PRESENTACION_CUNDINAMARCA', 'ESTU_DEPTO_PRESENTACION_GUAINIA', 'ESTU_DEPTO_PRESENTACION_GUAVIARE', 'ESTU_DEPTO_PRESENTACION_HUILA', 'ESTU_DEPTO_PRESENTACION_LA GUAJIRA', 'ESTU_DEPTO_PRESENTACION_MAGDALENA', 'ESTU_DEPTO_PRESENTACION_META', 'ESTU_DEPTO_PRESENTACION_NARIÑO', 'ESTU_DEPTO_PRESENTACION_NORTE SANTANDER', 'ESTU_DEPTO_PRESENTACION_PUTUMAYO', 'ESTU_DEPTO_PRESENTACION_QUINDIO', 'ESTU_DEPTO_PRESENTACION_RISARALDA', 'ESTU_DEPTO_PRESENTACION_SAN ANDRES', 'ESTU_DEPTO_PRESENTACION_SANTANDER', 'ESTU_DEPTO_PRESENTACION_SUCRE', 'ESTU_DEPTO_PRESENTACION_TOLIMA', 'ESTU_DEPTO_PRESENTACION_VALLE', 'ESTU_DEPTO_PRESENTACION_VAUPES', 'ESTU_DEPTO_PRESENTACION_VICHADA', 'ESTU_MCPIO_PRESENTACION_ANDES', 'ESTU_MCPIO_PRESENTACION_APARTADÓ', 'ESTU_MCPIO_PRESENTACION_ARAUCA', 'ESTU_MCPIO_PRESENTACION_ARMENIA', 'ESTU_MCPIO_PRESENTACION_BARANOA', 'ESTU_MCPIO_PRESENTACION_BARBOSA', 'ESTU_MCPIO_PRESENTACION_BARRANCABERMEJA', 'ESTU_MCPIO_PRESENTACION_BARRANQUILLA', 'ESTU_MCPIO_PRESENTACION_BELLO', 'ESTU_MCPIO_PRESENTACION_BOGOTÁ D.C.', 'ESTU_MCPIO_PRESENTACION_BUCARAMANGA', 'ESTU_MCPIO_PRESENTACION_BUENAVENTURA', 'ESTU_MCPIO_PRESENTACION_CALARCÁ', 'ESTU_MCPIO_PRESENTACION_CALDAS', 'ESTU_MCPIO_PRESENTACION_CALI', 'ESTU_MCPIO_PRESENTACION_CARTAGENA DE INDIAS', 'ESTU_MCPIO_PRESENTACION_CARTAGO', 'ESTU_MCPIO_PRESENTACION_CAUCASIA', 'ESTU_MCPIO_PRESENTACION_CHIQUINQUIRÁ', 'ESTU_MCPIO_PRESENTACION_CHÍA', 'ESTU_MCPIO_PRESENTACION_COROZAL', 'ESTU_MCPIO_PRESENTACION_CÚCUTA', 'ESTU_MCPIO_PRESENTACION_DUITAMA', 'ESTU_MCPIO_PRESENTACION_EL BANCO', 'ESTU_MCPIO_PRESENTACION_EL CARMEN DE VIBORAL', 'ESTU_MCPIO_PRESENTACION_ENVIGADO', 'ESTU_MCPIO_PRESENTACION_ESPINAL', 'ESTU_MCPIO_PRESENTACION_FACATATIVÁ', 'ESTU_MCPIO_PRESENTACION_FLORENCIA', 'ESTU_MCPIO_PRESENTACION_FUNZA', 'ESTU_MCPIO_PRESENTACION_FUSAGASUGÁ', 'ESTU_MCPIO_PRESENTACION_GACHETÁ', 'ESTU_MCPIO_PRESENTACION_GARZÓN', 'ESTU_MCPIO_PRESENTACION_GIRARDOT', 'ESTU_MCPIO_PRESENTACION_GIRÓN', 'ESTU_MCPIO_PRESENTACION_GUADALAJARA DE BUGA', 'ESTU_MCPIO_PRESENTACION_GUAPÍ', 'ESTU_MCPIO_PRESENTACION_GÜICÁN DE LA SIERRA', 'ESTU_MCPIO_PRESENTACION_IBAGUÉ', 'ESTU_MCPIO_PRESENTACION_ICONONZO', 'ESTU_MCPIO_PRESENTACION_INÍRIDA', 'ESTU_MCPIO_PRESENTACION_IPIALES', 'ESTU_MCPIO_PRESENTACION_ISTMINA', 'ESTU_MCPIO_PRESENTACION_ITAGÜÍ', 'ESTU_MCPIO_PRESENTACION_JAMUNDÍ', 'ESTU_MCPIO_PRESENTACION_LA DORADA', 'ESTU_MCPIO_PRESENTACION_LA VEGA', 'ESTU_MCPIO_PRESENTACION_LETICIA', 'ESTU_MCPIO_PRESENTACION_MADRID', 'ESTU_MCPIO_PRESENTACION_MAGANGUÉ', 'ESTU_MCPIO_PRESENTACION_MANIZALES', 'ESTU_MCPIO_PRESENTACION_MARQUETALIA', 'ESTU_MCPIO_PRESENTACION_MEDELLÍN', 'ESTU_MCPIO_PRESENTACION_MELGAR', 'ESTU_MCPIO_PRESENTACION_MITÚ', 'ESTU_MCPIO_PRESENTACION_MOCOA', 'ESTU_MCPIO_PRESENTACION_MOMPÓS', 'ESTU_MCPIO_PRESENTACION_MONIQUIRÁ', 'ESTU_MCPIO_PRESENTACION_MONTELÍBANO', 'ESTU_MCPIO_PRESENTACION_MONTERREY', 'ESTU_MCPIO_PRESENTACION_MONTERÍA', 'ESTU_MCPIO_PRESENTACION_MOSQUERA', 'ESTU_MCPIO_PRESENTACION_MÁLAGA', 'ESTU_MCPIO_PRESENTACION_NEIVA', 'ESTU_MCPIO_PRESENTACION_NILO', 'ESTU_MCPIO_PRESENTACION_NOCAIMA', 'ESTU_MCPIO_PRESENTACION_OCAÑA', 'ESTU_MCPIO_PRESENTACION_ORITO', 'ESTU_MCPIO_PRESENTACION_PALMIRA', 'ESTU_MCPIO_PRESENTACION_PAMPLONA', 'ESTU_MCPIO_PRESENTACION_PASTO', 'ESTU_MCPIO_PRESENTACION_PENSILVANIA', 'ESTU_MCPIO_PRESENTACION_PEREIRA', 'ESTU_MCPIO_PRESENTACION_PIEDECUESTA', 'ESTU_MCPIO_PRESENTACION_PIENDAMÓ - TUNÍA', 'ESTU_MCPIO_PRESENTACION_PITALITO', 'ESTU_MCPIO_PRESENTACION_POPAYÁN', 'ESTU_MCPIO_PRESENTACION_PUERTO ASÍS', 'ESTU_MCPIO_PRESENTACION_PUERTO BERRÍO', 'ESTU_MCPIO_PRESENTACION_PUERTO CARREÑO', 'ESTU_MCPIO_PRESENTACION_PÁCORA', 'ESTU_MCPIO_PRESENTACION_QUIBDÓ', 'ESTU_MCPIO_PRESENTACION_RIOHACHA', 'ESTU_MCPIO_PRESENTACION_RIONEGRO', 'ESTU_MCPIO_PRESENTACION_RIOSUCIO', 'ESTU_MCPIO_PRESENTACION_ROLDANILLO', 'ESTU_MCPIO_PRESENTACION_SABANETA', 'ESTU_MCPIO_PRESENTACION_SAHAGÚN', 'ESTU_MCPIO_PRESENTACION_SAN ANDRÉS', 'ESTU_MCPIO_PRESENTACION_SAN ANDRÉS DE TUMACO', 'ESTU_MCPIO_PRESENTACION_SAN GIL', 'ESTU_MCPIO_PRESENTACION_SAN JOSÉ DEL GUAVIARE', 'ESTU_MCPIO_PRESENTACION_SAN JUAN NEPOMUCENO', 'ESTU_MCPIO_PRESENTACION_SANTA FÉ DE ANTIOQUIA', 'ESTU_MCPIO_PRESENTACION_SANTA MARTA', 'ESTU_MCPIO_PRESENTACION_SANTA ROSA DE OSOS', 'ESTU_MCPIO_PRESENTACION_SANTANDER DE QUILICHAO', 'ESTU_MCPIO_PRESENTACION_SIBUNDOY', 'ESTU_MCPIO_PRESENTACION_SINCELEJO', 'ESTU_MCPIO_PRESENTACION_SOACHA', 'ESTU_MCPIO_PRESENTACION_SOATÁ', 'ESTU_MCPIO_PRESENTACION_SOCORRO', 'ESTU_MCPIO_PRESENTACION_SOGAMOSO', 'ESTU_MCPIO_PRESENTACION_SOLEDAD', 'ESTU_MCPIO_PRESENTACION_SONSÓN', 'ESTU_MCPIO_PRESENTACION_SOPETRÁN', 'ESTU_MCPIO_PRESENTACION_TADÓ', 'ESTU_MCPIO_PRESENTACION_TULUÁ', 'ESTU_MCPIO_PRESENTACION_TUNJA', 'ESTU_MCPIO_PRESENTACION_TURBO', 'ESTU_MCPIO_PRESENTACION_URRAO', 'ESTU_MCPIO_PRESENTACION_VALLEDUPAR', 'ESTU_MCPIO_PRESENTACION_VILLA DEL ROSARIO', 'ESTU_MCPIO_PRESENTACION_VILLAVICENCIO', 'ESTU_MCPIO_PRESENTACION_VÉLEZ', 'ESTU_MCPIO_PRESENTACION_YARUMAL', 'ESTU_MCPIO_PRESENTACION_YOLOMBÓ', 'ESTU_MCPIO_PRESENTACION_YOPAL', 'ESTU_MCPIO_PRESENTACION_ZARZAL', 'ESTU_MCPIO_PRESENTACION_ZIPAQUIRÁ', 'ESTU_PAGOMATRICULABECA_Si', 'ESTU_PAGOMATRICULACREDITO_Si', 'ESTU_PRIVADO_LIBERTAD_S', 'ESTU_GENERO_M', 'ESTU_PAGOMATRICULAPADRES_Si', 'ESTU_PAGOMATRICULAPROPIO_Si', 'FAMI_TIENEAUTOMOVIL_Si', 'FAMI_TIENELAVADORA_Si', 'FAMI_TIENECOMPUTADOR_Si', 'FAMI_TIENEINTERNET_Si', 'INST_ORIGEN_NO OFICIAL - FUNDACIÓN', 'INST_ORIGEN_OFICIAL DEPARTAMENTAL', 'INST_ORIGEN_OFICIAL MUNICIPAL', 'INST_ORIGEN_OFICIAL NACIONAL', 'INST_ORIGEN_REGIMEN ESPECIAL']
    for column in col_names:
        if column not in data_encoded.columns:
            data_encoded[column] = False

    data_encoded = data_encoded[col_names]

    return data_encoded

def load_model(file_path):
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model

def user_input_features():
    valor_matric = st.sidebar.selectbox('Valor de la Matrícula', ('Entre 2.5 millones y menos de 4 millones', 
                                                                  'Menos de 500 mil',
                                                                  'Entre 1 millón y menos de 2.5 millones',
                                                                  'Entre 500 mil y menos de 1 millón',
                                                                  'Más de 7 millones',                   
                                                                  'Entre 4 millones y menos de 5.5 millones',
                                                                   'Entre 5.5 millones y menos de 7 millones', 
                                                                   'No pagó matrícula'))
    dep_pres = st.sidebar.selectbox('Departamento de Presentación', ('BOGOTÁ', 'VALLE', 'TOLIMA', 'SANTANDER', 'SUCRE', 'ANTIOQUIA', 'BOYACA', 'CAUCA', 'HUILA', 'CUNDINAMARCA', 'CORDOBA', 'ATLANTICO', 'BOLIVAR', 'CALDAS', 'NORTE SANTANDER', 'CESAR', 'RISARALDA', 'QUINDIO', 'MAGDALENA', 'ARAUCA', 'META', 'CAQUETA', 'NARIÑO', 'LA GUAJIRA', 'PUTUMAYO', 'AMAZONAS', 'CHOCO', 'CASANARE', 'GUAVIARE', 'SAN ANDRES', 'GUAINIA', 'VAUPES', 'VICHADA'))
    muncp_pres = st.sidebar.selectbox('Municipio de Presentación', ('BOGOTÁ D.C.', 'TULUÁ', 'IBAGUÉ', 'BARRANCABERMEJA', 'SINCELEJO', 'PALMIRA', 'CALI', 'ITAGÜÍ', 'DUITAMA', 'POPAYÁN', 'NEIVA', 'RIONEGRO', 'BELLO', 'CHÍA', 'MONTERÍA', 'BARRANQUILLA', 'MONTELÍBANO', 'CARTAGENA DE INDIAS', 'SOACHA', 'TURBO', 'MÁLAGA', 'SABANETA', 'RIOSUCIO', 'BUENAVENTURA', 'CÚCUTA', 'TUNJA', 'MEDELLÍN', 'PITALITO', 'VALLEDUPAR', 'PEREIRA', 'YOLOMBÓ', 'BUCARAMANGA', 'ARMENIA', 'SANTA MARTA', 'ARAUCA', 'BARANOA', 'SOLEDAD', 'MANIZALES', 'VILLA DEL ROSARIO', 'VILLAVICENCIO', 'SOGAMOSO', 'VÉLEZ', 'FUSAGASUGÁ', 'FLORENCIA', 'GIRARDOT', 'PASTO', 'FUNZA', 'ZIPAQUIRÁ', 'FACATATIVÁ', 'OCAÑA', 'SAHAGÚN', 'RIOHACHA', 'IPIALES', 'GIRÓN', 'MOCOA', 'ROLDANILLO', 'SOCORRO', 'CHIQUINQUIRÁ', 'GUADALAJARA DE BUGA', 'COROZAL', 'LETICIA', 'APARTADÓ', 'EL BANCO', 'JAMUNDÍ', 'SANTANDER DE QUILICHAO', 'QUIBDÓ', 'YOPAL', 'SANTA ROSA DE OSOS', 'CAUCASIA', 'PAMPLONA', 'GUAPÍ', 'CALDAS', 'SAN JOSÉ DEL GUAVIARE', 'PENSILVANIA', 'MADRID', 'MOSQUERA', 'CALARCÁ', 'SAN ANDRÉS', 'PUERTO ASÍS', 'SAN ANDRÉS DE TUMACO', 'ESPINAL', 'MAGANGUÉ', 'MONIQUIRÁ', 'SAN GIL', 'SANTA FÉ DE ANTIOQUIA', 'LA DORADA', 'ANDES', 'CARTAGO', 'ORITO', 'PIEDECUESTA', 'MELGAR', 'AGUACHICA', 'PIENDAMÓ - TUNÍA', 'GARZÓN', 'SIBUNDOY', 'ISTMINA', 'INÍRIDA', 'MOMPÓS', 'ZARZAL', 'NOCAIMA', 'EL CARMEN DE VIBORAL', 'SOATÁ', 'URRAO', 'MARQUETALIA', 'MITÚ', 'PÁCORA', 'PUERTO BERRÍO', 'PUERTO CARREÑO', 'TADÓ', 'GACHETÁ', 'MONTERREY', 'SAN JUAN NEPOMUCENO', 'YARUMAL', 'SONSÓN', 'BARBOSA', 'ICONONZO', 'GÜICÁN DE LA SIERRA', 'LA VEGA', 'SOPETRÁN', 'ENVIGADO', 'NILO'))
    beca = st.sidebar.radio('Tiene Beca?', ('Si', 'No'))
    credito = st.sidebar.radio('Tiene Credito?', ('Si', 'No'))
    h_trabajo = st.sidebar.selectbox('Horas de Trabajo a la Semana?', ('0','Entre 11 y 20 horas', 'Entre 21 y 30 horas', 'Más de 30 horas',  'Menos de 10 horas'))
    libertad = st.sidebar.radio('Ha estado Privado de Libertad?', ("S", "N"))
    genero = st.sidebar.radio('Sexo', ('M', 'F'))
    pago_padres = st.sidebar.radio('Los Padres Pagaron la Matricula?', ("Si", "No"))
    pago_propio = st.sidebar.radio('Pago la Matricula por Medios Propios?', ("Si", "No"))
    automovil = st.sidebar.radio('Tiene Automovil?', ("Si", "No"))
    lavadora = st.sidebar.radio('Tiene Lavadora?', ("Si", "No"))
    estrato_vivienda = st.sidebar.selectbox('Estrato de Vivienda', ('Estrato 2', 'Estrato 3', 'Estrato 1', 'Estrato 4', 'Estrato 5', 'Estrato 6', 'Sin Estrato'))
    computador = st.sidebar.radio('Tiene Computador?', ("Si", "No"))    
    internet = st.sidebar.radio('Tiene Internet?', ("Si", "No"))
    educacion_padre = st.sidebar.selectbox('Nivel de Educación del Padre', ('Secundaria (Bachillerato) incompleta', 'No sabe', 'Técnica o tecnológica completa', 'Educación profesional completa', 'Ninguno', 'Técnica o tecnológica incompleta', 'Primaria completa', 'Primaria incompleta', 'Educación profesional incompleta', 'Secundaria (Bachillerato) completa', 'Postgrado', 'No Aplica'))
    educacion_madre = st.sidebar.selectbox('Nivel de Educación de la Madre', ('Secundaria (Bachillerato) incompleta', 'No sabe', 'Técnica o tecnológica completa', 'Educación profesional completa', 'Ninguno', 'Técnica o tecnológica incompleta', 'Primaria completa', 'Primaria incompleta', 'Educación profesional incompleta', 'Secundaria (Bachillerato) completa', 'Postgrado', 'No Aplica'))
    tipo_de_institucion = st.sidebar.selectbox('Tipo de Institución', ('NO OFICIAL - CORPORACIÓN', 'OFICIAL DEPARTAMENTAL', 'NO OFICIAL - FUNDACIÓN', 'OFICIAL NACIONAL', 'OFICIAL MUNICIPAL', 'REGIMEN ESPECIAL'))
    
    features = {'ESTU_VALORMATRICULAUNIVERSIDAD': valor_matric,
                'ESTU_DEPTO_PRESENTACION': dep_pres,
                'ESTU_MCPIO_PRESENTACION': muncp_pres,
                'ESTU_PAGOMATRICULABECA': beca,
                'ESTU_PAGOMATRICULACREDITO': credito,
                'ESTU_HORASSEMANATRABAJA': h_trabajo,
                'ESTU_PRIVADO_LIBERTAD': libertad,
                'ESTU_GENERO': genero,
                'ESTU_PAGOMATRICULAPADRES': pago_padres,
                'ESTU_PAGOMATRICULAPROPIO': pago_propio,
                'FAMI_EDUCACIONPADRE': educacion_padre,
                'FAMI_TIENEAUTOMOVIL': automovil,
                'FAMI_TIENELAVADORA': lavadora,
                'FAMI_ESTRATOVIVIENDA': estrato_vivienda,
                'FAMI_TIENECOMPUTADOR': computador,
                'FAMI_TIENEINTERNET': internet,
                'FAMI_EDUCACIONMADRE': educacion_madre,
                'INST_ORIGEN': tipo_de_institucion
            }
    
    return pd.DataFrame(features, index=["Predicción"])


st.markdown("""
<style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
    .info-text {
        font-size:16px;
    }
    h1 {
        color: #4A90E2;
    }
    .streamlit-expanderHeader {
        font-size: 18px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)



logo_path = 'LogoSabana.png'

col1, col2 = st.columns([1, 3])
with col1:
    st.write(' ')
    st.write(' ')
    st.image(logo_path, use_column_width=True
                    )  # Adjust width as needed
with col2:
    st.title('Estudio de Resultados de las Pruebas Saber-Pro Colombia')
st.markdown(''' 
    ## Una Mirada al Futuro de la Educación en Colombia
            
    ###### Autores:
    - Juan Manuel Castillo
    - Jose Miguel Tejedor
    - Mariana Tovar Vega
    - Shadia Haddad
 ''')

st.markdown("""
        <style>
        .justify-text {
            text-align: justify;
            text-justify: inter-word;
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        </style>
        <div class="justify-text">
            <h2>Introducción al Análisis de las Pruebas Saber Pro</h2>
            <p>Bienvenidos al dashboard interactivo para el análisis de los resultados de las Pruebas Saber Pro en Colombia. Este proyecto tiene como objetivo principal proporcionar una herramienta analítica que permita visualizar y explorar los datos relacionados con el desempeño académico de los estudiantes universitarios a lo largo de varios años.</p>
            <p>Las Pruebas Saber Pro son evaluaciones realizadas a nivel nacional que buscan medir la calidad de la educación superior en Colombia. Los resultados de estas pruebas son fundamentales para entender no solo el nivel académico de los estudiantes, sino también para identificar disparidades y oportunidades de mejora en el sistema educativo.</p>
            <p>Mediante este dashboard, los usuarios podrán interactuar con los datos y obtener insights personalizados sobre los factores que influyen en los resultados de las pruebas, como el contexto socioeconómico y geográfico de los estudiantes, así como características específicas de las instituciones educativas.</p>
            <p>Este análisis no solo es relevante para los estudiantes y educadores, sino también para los formuladores de políticas y las autoridades educativas que buscan desarrollar estrategias para mejorar la calidad y equidad de la educación superior en Colombia.</p>
            <p>A continuación, exploraremos en detalle los objetivos específicos de este proyecto.</p>
        </div>
        """, unsafe_allow_html=True)

col3, col4 = st.columns([3, 2])
saber_path = 'SaberPro.png'
with col4:
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.image(saber_path, use_column_width=True
              )  
with col3:
    st.markdown("""
            <style>
            .justify-text {
                text-align: justify;
                text-justify: inter-word;
            }
            </style>
            <div class="justify-text">
                <h2>Objetivo del Proyecto</h2>
                <p>Realizar un análisis profundo sobre los resultados de las pruebas Saber Pro de los años 2018 a 2022, para encontrar y estudiar las disparidades en los resultados educativos basándose en características socioeconómicas y demográficas de los estudiantes.</p>
            </div>
            """, unsafe_allow_html=True)

st.markdown("""
        <style>
        .justify-text {
            text-align: justify;
            text-justify: inter-word;
        }
        </style>
        <div class="justify-text">
            <h2>Objetivo de Desarrollo Sostenible</h2>
            <p>El nivel académico de los estudiantes universitarios es crucial para cumplir con el cuarto Objetivo de Desarrollo Sostenible de la ONU. Esto garantiza una educación de calidad para todos, reduce las disparidades educativas y prepara a los individuos para acceder a oportunidades, impulsando el desarrollo socioeconómico global.</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
            <style>
            .justify-text {
                text-align: justify;
                text-justify: inter-word;
            }
            .justify-list {
                text-align: justify;
                text-justify: inter-word;
                margin-left: 20px; /* Align list inside the div */
            }
            </style>
            <div class="justify-text">
                <h2>Objetivo del Negocio</h2>
                <ul class="justify-list">
                    <li>La meta principal es proporcionar a las instituciones educativas y al gobierno una herramienta confiable que les permita tomar decisiones informadas sobre cómo optimizar el proceso de mejorar la calidad de la educación.</li>
                    <li>Como modelo de negocio, buscamos desarrollar un aplicativo basado en la base de datos de exámenes pasados, con el fin de predecir el puntaje de un futuro estudiante dando su contexto socioeconómico.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

st.markdown("""
            <style>
                .justify-text {
                    text-align: justify;
                    text-justify: inter-word;
                    font-family: Arial, sans-serif;
                }
                .justify-list {
                    text-align: justify;
                    text-justify: inter-word;
                    margin-left: 40px;  /* Adjusted for better alignment */
                    font-family: Arial, sans-serif;
                    line-height: 1.6;  /* Improves readability */
                }
                h2 {
                    color: #4A90E2;  /* A blue that is easier on the eyes */
                }
            </style>

            <div class="justify-text">
                <h2>Descripción de los Datos</h2>
                <ul class="justify-list">
                    <li>Los datos provienen de <a href='https://www.datos.gov.co/' target='_blank'>datos.gov.co</a>, el portal de Datos Abiertos del Gobierno Colombiano. El conjunto de datos inicial consistía en 1,217,482 registros y 57 columnas, incluyendo información socioeconómica de los estudiantes, así como datos geográficos y detalles sobre las instituciones educativas donde se presentaron las pruebas.</li>
                    <li>Se llevó a cabo un Análisis Exploratorio de Datos (EDA) para identificar atributos clave y profundizar en el entendimiento de los patrones y comportamientos inherentes al conjunto de datos.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

st.markdown("""
            <style>
                .justify-text {
                    text-align: justify;
                    text-justify: inter-word;
                    font-family: Arial, sans-serif;
                }
                .justify-list {
                    text-align: justify;
                    text-justify: inter-word;
                    margin-left: 40px;  /* Adjusted for better alignment */
                    font-family: Arial, sans-serif;
                    line-height: 1.6;  /* Improves readability */
                }
                h2 {
                    color: #4A90E2;  /* A blue that is easier on the eyes */
                }
            </style>

            <div class="justify-text">
                <h3>Aquí mostramos el comportamiento de nuestro objetivo que es el puntaje total de la prueba de todos los datos observados</h3>
            </div>

            """, unsafe_allow_html=True)
st.image('EDA_PuntajeTotal.png',use_column_width=True)


st.markdown("""
                <style>
                    .justify-text {
                        text-align: justify;
                        text-justify: inter-word;
                        font-family: Arial, sans-serif;
                    }
                    .justify-list {
                        text-align: justify;
                        text-justify: inter-word;
                        margin-left: 40px;  /* Adjusted for better alignment */
                        font-family: Arial, sans-serif;
                        line-height: 1.6;  /* Improves readability */
                    }
                    h2, h3 {
                        color: #4A90E2;  /* A blue that is easier on the eyes */
                    }
                </style>

                <div class="justify-text">
                    <h3>Algunas gráficas interesantes...</h3>
                </div>
                """, unsafe_allow_html=True)


with st.expander("Ver Gráficas"):
    col5, col6 = st.columns([1, 1])
    with col5:
        st.image('EDA_1.png',use_column_width=True)  
    with col6:
        st.image('EDA_2.png', use_column_width=True) 

    col5, col6 = st.columns([1, 1])
    with col5:
        st.image('EDA_4.png',use_column_width=True)  
    with col6:
        st.image('EDA_5.png', use_column_width=True) 

    col5, col6 = st.columns([1, 1])
    with col5:
        st.image('EDA_7.png',use_column_width=True)  
    with col6:
        st.image('EDA_8.png', use_column_width=True)  
    st.image('EDA_9.png', use_column_width=True)
    st.image('EDA_10.png', use_column_width=True)
    st.image('EDA_11.png', use_column_width=True)

st.markdown("""
            <style>
            .justify-text {
                text-align: justify;
                text-justify: inter-word;
                font-family: Arial, sans-serif;
                line-height: 1.6;
            }
            </style>
            <div class="justify-text">
                <h1>Proceso de Aprendizaje Automático</h1>
                <p>En la fase de preparación de los datos, se realizó un procesamiento exhaustivo que incluyó técnicas como <em>one-hot encoding</em> y <em>ordinal encoding</em>. Además, se llevaron a cabo la eliminación y transformación de diversos atributos para optimizar la calidad de los datos de entrada.</p>
                <p>Durante el desarrollo del modelo, se evaluaron diversos algoritmos de Machine Learning para determinar cuál ofrecía el mejor rendimiento en términos de precisión y eficiencia. Después de probar opciones como Support Vector Machines, Random Forest y otros métodos de ensamble, se seleccionó el algoritmo de <strong>Gradient Boosting Regressor</strong> por su superior capacidad predictiva y manejo eficiente de las interacciones complejas entre atributos.</p>
                <p>El Gradient Boosting Regressor, parte de la familia de métodos de ensamble, combina múltiples árboles de decisión de manera secuencial. Cada árbol nuevo intenta corregir los errores del árbol anterior, resultando en una mejora incremental y significativa de la precisión en las predicciones. Este enfoque fue elegido por su eficacia probada en tareas similares de regresión y su habilidad para manejar características no lineales, lo que es crucial para la precisión de nuestras predicciones en el contexto educativo de las pruebas Saber Pro.</p>
                <p>A continuación, se presentan algunas visualizaciones que muestran el proceso de entrenamiento y validación del modelo, mediante las compraciones de los resultados de los algoritmos evaluados.</p>
            </div>
            """, unsafe_allow_html=True)

col8, col9 = st.columns([1, 1])
with col8:
    st.image('ML_1.png',use_column_width=True)  
with col9:
    st.image('ML_2.png', use_column_width=True) 

st.image('ML_3.png', use_column_width=True)

st.write("""
# Predicción de Resultados de la Prueba Saber-Pro
En la tabla a continuación, se muestran los atributos ingresados para predecir el resultado de la prueba Saber Pro. Como se menciono anteriormente se utilzara un modelo de Machine Learning para predecir el resultado de la prueba Saber Pro, especificamente Gradient Boosting Regressor el cual ya fue entrenado con la base de datos de los años 2018 a 2022.
""")



def load_model(file_path):
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model

if 'predictions' not in st.session_state:
    st.session_state.predictions = []

st.sidebar.header('Ingrese los Datos del Estudiante para la Predicción')
df = user_input_features()
st.write(df)

model = load_model('model_trained.pkl')

if st.button('Predecir Puntaje'):
    data = transform_data(df)
    prediction = model.predict(data)
    resultado = int(prediction[0].round(0))

    if len(st.session_state.predictions) >= 5:
        st.session_state.predictions.pop(0)
    st.session_state.predictions.append((df, resultado))

    st.write(f'## Predicción del Puntaje: {resultado}')
    st.write("Se realizo la predicción del puntaje del estudiante exitosamente!")
else:
    st.write('###### Si desea generar una predicción con los datos presentes, presione el botón, o si desea cambiar alguno de los valores presentados en la tabla anterior, puede hacerlo en la barra lateral.')

with st.expander("Ver Historial de Predicciones"):
    for data, score in st.session_state.predictions[::-1]:
        st.write(f"Puntaje Predicho: {score}")
        st.write(pd.DataFrame(data))
