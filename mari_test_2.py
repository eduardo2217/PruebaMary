# coding=utf-8
import speech_recognition as sr
from gtts import gTTS
import os
import cv2
import time
import threading
from openai import OpenAI



client = OpenAI(api_key='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') #paid AudacIA account

#configure openai


assistante = 'Actua como Mary, la inteligencia artificial de AudacIA; '
corta_respuesta = 'responde en un parrafo de 30 palabras'
'''
messages_array = [
    {'role': 'system', 'content': assistante  + 'saluda a los invitados de esta manera: ¡Hola! Bienvenido a AudacIA, el centro de investigación, desarrollo tecnológico e innovación en inteligencia artificial y robótica. ¿En qué puedo ayudarte hoy?'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'IA obtenida a partir de datos simulados para atacar el virus SARS-CoV-2 (Covid 19) Demora en obtener resultados por la alta demanda de pruebas PCR en la ciudad de Barranquilla. Esta alta demanda promovía la obtención de resultados erróneos dando como negativos casos posiblemente positivos. Se generaron y probaron modelos de aprendizaje automático (ML)utilizando pequeñas cantidades de datos de cada clase. Se utilizó el mejor modelo para clasificar los big data obtenidos por el Laboratorio de Virología de la Universidad Simón Bolívar a partir de curvas de RT-PCR en tiempo real para el SARS-CoV-2, y el modelo fue reentrenado e implementado en un software que correlacionó los datos del paciente con la prueba y diagnósticos de IA. La IA se diseñó para facilitar la verificación mediante la detección de perfiles atípicos en las curvas de PCR causados por contaminación o artefactos. Se mejoró la atención de los laboratorios y la veracidad de los resultados de las muestras PCR en la ciudad de Barranquilla y Departamento del Atlántico El problema radica cuando son muchas muestras que hay que revisar por parte de los directores de laboratorios, cuando CAMILLE detecta una anomalía marca la intercepción del canal y el paciente específico, donde se debe revisar para tomar la decisión.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Aplicativo con IA para la alerta de irregularidades en la piel SkinnIA es una empresa con base tecnológica y en salud. Gracias al programa Versos, AudacIA apoyó esta iniciativa desarrollando un aplicativo móvil educativo para el cuidado de la piel con inteligencia artificial para la alerta de irregularidades que necesiten de la atención de un profesional de la salud. La aplicación trabaja por medio de fotos que la IA puede identificar si un melanoma es benigno o maligno. Además, cuenta con cursos donde los usuarios pueden aprender y evaluar sus conocimientos sobre la piel y sus cuidados. SkinnIA es una empresa de base tecnológica que busca incrementar la tasa de supervivencia de pacientes con cáncer y otras afectaciones de piel, poniendo a disposición del público una herramienta de impresión diagnostica temprana basada en tecnología de inteligencia artificial.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'VART es un dispositivo de telemedicina con IA que identifica enfermedades oculares en bebés prematuros al capturar imágenes de la retina con un campo visual de 160°, facilitando el diagnóstico de retinopatía del prematuro'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Patrii es una IA que detecta glaucoma en segundos al analizar campos visuales. Su software autónomo es un valioso recurso para oftalmólogos, identificando anomalías y glaucoma en 20 segundos, además de ser uno de los primero software patentados en Colombia'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Dispositivo que diagnostica daños en la retina Más de 2.000 millones de personas en el planeta sufren de alguna deficiencia visual o ceguera, los cuales generan un alto volumen de exámenes cuyo resultados demoran en la entrega a los pacientes Se desarrolló una plataforma basada en inteligencia artificial para la lectura de exámenes de retina, que ayuda oftalmólogos especialistas quienes necesitan realizar lectura de cada imagen por cada ojo de cada paciente, disminuyendo así, el tiempo empleado en la lectura de exámenes y agilizando la entrega de resultados. El equipo estaba formado por físicos, químicos, matemáticos e ingenieros de sistemas que mezclaron sus conocimientos con los especialistas de Cofca sumando un total de 12.000 horas de trabajo. Disminuir los tiempos de lectura, permitiendo mayor disponibilidad de tiempo para actividades de formación, y mejoraría la capacidad lectora de imágenes de los médicos, con inclusión de una nueva ventaja competitiva de ser personal médico con formación de expertos.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Bot que ayuda al entrenamiento de estudiantes de medicina en el uso de la semiología de las enfermedades El software con inteligencia artificial para fortalecer la precisión de dictámenes médicos por medio de la simulación de pacientes virtuales. Mario toma como base la simulación de pacientes virtuales que permita fortalecer conocimientos y habilidades de las personas del sector de la salud, siendo destinado principalmente a los estudiantes de dicho sector para complementar su proceso de aprendizaje. El adecuado reconocimientos de síntomas físicos es crucial en este campo profesional, por ejemplo, un pediatra se debe ser muy cuidadoso con respecto a lo que el niño trata de expresar las molestias que siente. Actualmente el uso e implementación de pacientes virtuales supone un gran avance tecnológico para la exploración de distintas ramas de la medicina. Esto impacta significativamente en las habilidades a desarrollar por el personal de la salud, como lo es la toma de diagnóstico médico, repercutiendo finalmente en la creación de la historia clínica del mismo. Los resultados obtenidos del uso del software evidencian el mejoramiento paulatino de los usuarios en el campo médico.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'IA para el análisis predictivo de fractura Schatzker Desarrollar un modelo de análisis predictivo con base en la información histórica asistencial de los pacientes como referente para tratamientos futuros. Se desarrolló una inteligencia artificial la cual a partir de datos suministrados en relación a la fractura y el tratamiento propuesto es capaz de predecir si el tratamiento será favorable o no, facilitando y ayudando al personal médico a la hora de decidir el mejor tratamiento frente a una fractura schatzker.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Detección de neumonía viral o bacteriana a través de imágenes de radiografía de tórax Neupeek es una app desarrollada para hacer una impresión diagnóstica por medio de una red neuronal convolucional entrenada con imágenes de radiografía de tórax de pacientes con neumonía Bacteriana y viral.​'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Inteligencia artificial capaz de alertar sobre trastornos psicológicos La ansiedad y la depresión están infradiagnosticadas y en aumento a nivel mundial. Con Mary queremos dar una herramienta útil a los médicos para que sea una orientación a un correcto diagnóstico y así tratarlo previamente Se creó un software entrenado con baterías de test de aspectos psicológicos le permite interactuar fluidamente con las personas y procesar la información para dar como resultado impresiones diagnósticas de forma masiva. Mary guarda las respuestas del paciente y con base a su diagnóstico, sugiere agendar cita con un profesional de la salud 37.000 personas del Departamento del Atlántico fueron monitoreadas y 180 personas fueron analizadas vía telefónica por difícil acceso al lugar'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Inteligencia artificial que evalúa a los estudiantes a través del sonido Vallenato Master es una plataforma e-learning para aprender a tocar instrumentos como el acordeón. Gracias al programa Versos, AudacIA apoyó esta iniciativa desarrollando una Inteligencia Artificial que automatize parte del proceso administrativo de Keiner, CEO de Vallenato Master, ayudándolo a evaluar a los estudiantes a través del sonido. Esta plataforma consiste en un listado de canciones previamente grabadas donde el estudiante escoge una la cual escucha, analiza y posterior a eso empieza a grabar. Una vez completado el ejercicio la IA da un porcentaje de similitud según la canción original. Con Vallenato Master cualquier persona puede aprender a tocar acordeón de forma didáctica y efectiva, con la que, gracias a nuestra metodología de enseñanza tipo blended learning probada con más de 9.500 estudiantes, y apoyados en nuestra plataforma tecnológica, podrás aprender a tocar acordeón un 30% más rápido y eficazmente que con los métodos convencionales como tutores, cursos presenciales y similares, todo por una fracción del costo de estos últimos.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Aplicación móvil para la reserva de experiencias turísticas ValleApp es un aplicativo móvil en donde se oferta experiencias turísticas. Gracias al programa Versos, AudacIA apoyó esta iniciativa desarrollando un aplicativo móvil donde se vende la experiencia turística a través de la tecnología. Por medio de un registro mira, reserva y paga desde la aplicación las diferentes experiencias en Valledupar. Además, recibirás notificaciones de los eventos gastronómicos locales. En ValleApp se reune lo más novedoso de la oferta turística Vallenata para que vivas una experiencia única. En colaboración con Turoperadores, sector hotelero, agentes de viajes, y empresarios de los 25 municipios, que pueden exhibir su oferta a propios y extranjeros de diferentes países con interés en conocer el potencial de esta maravillosa región.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Inteligencia artificial que evalúa las notas musicales para aprender instrumentos de viento. PIPEMASTER es tu profesor de música personal. La aplicación te escucha tocar y brinda devoluciones al instante sobre la precisión de tu ejercicio. El contenido está diseñado por el experto y maestro de Gaita Antonio Luis González para que todos los músicos. Es la herramienta usada en la tesis de maestría en objetos virtuales de aprendizaje de la universidad de Cartagena. Esta diseñado para músicos de nivel completamente principiantes como profesionales. PIPEMASTER se usa sólo con un instrumento de verdad, nada más. El micrófono de tu teléfono te escucha tocar y la aplicación te dice cómo lo hiciste, gracias a el algoritmo de reconocimiento entrenado de notas generadas por este instrumento. PIPEMASTER se creó junto con los métodos de enseñanza de los maestros expertos. Se adapta para que aprendas por tu cuenta o como complemento a las clases de un profesor. Con tutoriales paso a paso y devoluciones constantes.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'IA para la segmentación de turistas en el departamento de la Guajira Algoritmo que procesa la información de las bases de datos y segmenta a los usuarios según características en común. Este modelo de inteligencia artificial permite identificar y predecir gustos y preferencias para ofrecer servicios turísticos más a fínes a las características para asegurar una compra por parte del turista y una victoria temprana por parte de las entidades ofrecedoras del servicio. La IA clasifica a los usuarios gracias a los datos suministrados, cuando llega un nuevo usuario a la página y suministra los datos de entrada, la IA lo clasifica en uno de los segmentos ya creados, dirigiéndolo los paquetes turísticos que están relacionados a sus preferencias. La Universidad Simón Bolívar desde su centro de inteligencia artificial AudacIA, participó en la convocatoria de Minciencias, del programa COLinnova para financiar proyectos de innovación, donde se creó una alianza estratégica con entidades del Departamento de la Guajira, figurando SOLERA VIAJES Y TURISMO como entidad líder de la alianza y AudacIA – Unisimón como Aliado técnico del proyecto.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Simulador de acordeón que evalúa a los estudiantes según el número de aciertos Huellas del Maestro es una academia virtual de acordeón vallenato. Gracias al programa Versos, AudacIA apoyó esta iniciativa desarrollando una plataforma de simulador de acordeón. El simulador cuenta con un módulo con los diferentes controles para personalizar la práctica del acordeón acompañado de un listado de canciones de referencia. Mediante la comparación, el simulador da como resultado un porcentaje según el número de aciertos Es una plataforma digital experiencial de aprendizaje, para que cualquier persona pueda aprender a tocar acordeón de manera excepcional de la mano del ilustre Maestro Cocha Molina, gracias a una metodología diseñada a la medida por el maestro mismo y apoyado en la plataforma tecnológica que cuenta con un simulador de acordeón potenciado con inteligencia artificial.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Plataform E-learning para la enseñanza del baile Vallenclearato Bumva es una academia de baile para aprender a bailar vallenato. Gracias al programa Versos, AudacIA apoyó esta iniciativa desarrollando una plataforma e-learning que permita ofertar cursos con contenido multimedia y pago en línea Cuenta con una sección de blog donde se pueden ver noticias sobre la cultura vallenata y un foro donde los miembros pueden interactuar y compartir su proceso El Vallenato es un ritmo musical propio y autóctono que más se escuchaen Colombia y nos distinguen en el exterior, por eso con Bumva, colom- bianos y extrajeron podrán vivir bailando el vallenato 365 días al año 24/7desde cualquier lugar del mundo, a través un método deenseñanza único y personalizado de los cuatro ritmos vallenatos, desde una plata- forma tecnológica de forma fácil, eficaz y paso a paso, contribuyendo a la protección ydifusión de nuestro patrimonio cultural.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Software con inteligencia artificial y procesamiento de lenguaje natural Esta inteligencia artificial funciona como asistente virtual de entrenamiento para estudiantes de ingeniería de la Unisimón. Está entrenada para aprender cualquier tema y evaluar los conocimientos de los estudiantes Facilita en un 80% el aprendizaje de los temas de los estudiantes. Es un apoyo para los estudiantes en temas de inteligencia artifical y procesamiento del lenguage natural “Gracias a la necesidad y a la demanda que tienen las empresas de implementar Machine Learning en sus organizaciones, le pudimos dar vida a Mía, vimos una oportunidad muy grande para que los estudiantes conocieran y aprendieran sobre este tipo de tecnología, y para que así en el futuro puedan ser más competitivos en el mercado. Mía es producto 100% pensando para el crecimiento de nuestros estudiantes de la universidad”. – Reynaldo Villarreal'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Kit educativo para la enseñanza en ciencias de la computación y educación STEM Este kit consiste en el armado de las partes de un carrito junto con los elementos de robótica para su posterior programación a través de un software. CALVIN se creó con fines educativos y su diseño esta basado para la enseñanza en ciencias de la computación y educación STEM. Integra dos áreas básicas de la tecnología como son la robótica y la programación. Especial para niños ya que desarrolla conocimiento de una forma didáctica, divertida e intuitiva'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Sistema de inteligencia artificial para valoración de ecosistemas marinos Para la empresa SEPIAROV de San Andres, AudacIA de la Unisimón, desarrolló un sistema de inteligencia artificial para la valoración de ecosistemas mesofóticos; para agilizar el proceso de análisis de data colectada. Además, que se realice la identificación y estudio de especies de la reserva de Biosfera SEAFLOWER para la preservación de los ecosistemas marinos profundos. IMPACTOS +400 inmersiones 500 metros de profundidad 2 premios de la Real Academia de Ingeniería en Inglaterra La innovación e implementación tecnológica marina en San Andrés Islas se logró gracias al trabajo en equipo de la Universidad Simón Bolívar en compañía de la empresa SEPIA ROV.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Dispositivo para medir componentes del agua Victa es un innovador dispositivo diseñado para medir y analizar diversos componentes del agua. Esta avanzada boya flotante se caracteriza por su capacidad autónoma de carga, gracias a la incorporación de paneles solares que aprovechan la energía del sol para alimentar sus sistemas internos. Además, se destaca por su conveniente conectividad con dispositivos móviles, permitiendo un monitoreo y control fácil a través de una aplicación instalada en el celular. La funcionalidad de Victa abarca una amplia gama de aplicaciones relacionadas con el agua. Sus sensores especializados permiten medir parámetros cruciales como la temperatura, el pH, la conductividad eléctrica, oxígeno disuelto, brindando información precisa y actualizada sobre la calidad y las características del medio acuático en el que se encuentra desplegado.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Desarrollo de prototipo de un sistema que recolecta los datos de conductividad y ph en cultivos de Cannabis medicinal El presente proyecto se enfoca en el desarrollo de un prototipo de sistema para la recolección de datos de conductividad y pH en cultivos de cannabis medicinal. El objetivo principal es establecer una trazabilidad precisa de esta información, permitiendo un control más eficiente de las bombas de aire y agua utilizadas en el cultivo. El sistema propuesto tiene la capacidad de detectar cambios en el pH y llevar a cabo la dosificación del cultivo de forma automática, eliminando así la necesidad de intervención manual. Mediante la recopilación de datos de conductividad y pH en tiempo real, el sistema brinda a los cultivadores la posibilidad de monitorear y ajustar los niveles de nutrientes y condiciones del agua de riego de manera precisa y oportuna.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Desarrollo de un dispositivo innovador para la detección y diagnóstico oportuno del virus del Huanglongbing (HLB) en plantas de cítricos Este dispositivo estará diseñado para adaptarse a dispositivos móviles comunes, permitiendo a los agricultores y expertos en campo acceder a una herramienta de detección rápida y confiable. La tecnología se basará en una aplicación móvil y utilizará un sistema de filtros ópticos integrados en la cámara del celular. A través de esta aplicación, se podrá analizar una muestra de planta y determinar si está infectada con el virus HLB. La detección temprana de esta enfermedad es crucial, ya que permite tomar medidas preventivas y evitar la propagación del virus a otros cultivos cercanos.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Medidor de energía inteligente que permite gestionar y predecir el consumo de energía eléctrica Solenium SAS se encuentra actualmente en desarrollo de QUOIA, un medidor de energía inteligente que incorporará tecnología de inteligencia artificial. El objetivo es utilizar la inteligencia artificial para mejorar la detección y predicción de posibles fallas en el consumo eléctrico de las industrias. Este proyecto innovador está en la etapa de desarrollo y perfeccionamiento de la integración de la inteligencia artificial en QUOIA. Solenium SAS está trabajando arduamente para implementar esta tecnología de vanguardia y llevar los beneficios de la inteligencia artificial al monitoreo y gestión del consumo de energía eléctrica en las industrias.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Detección in situ de petróleo en suelos a través de espectroscopia láser de infrarrojo asistida por IA La inteligencia artificial permite analizar de manera rápida los datos recolectados por medio de un láser especial de cascada cuántica portátil, esto hace que pueda identificar con precisión la presencia / ausencia de trazas de petróleo en mezclas de suelo La Inteligencia artificial nos dice que suelo está contaminado y cual es el porcentaje de concentración de petróleo que contiene. Se desarrolló un método de análisis estadístico innovador, en términos técnicos, para calcular los límites de detección (LOD) y los límites de decisión (LD). Todo esto a partir de ajustes de probabilidad de detección. El desempeño superior de los modelos QCL / SVM mejoró estos valores a 0.04% y 0.003%, respectivamente, proporcionando una mejor probabilidad de identificación de suelos contaminados con petróleo.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Detección de inconsistencia en la toma de lecturas de consumo eléctrico IA capaz de pronosticar anomalías eléctricas según comportamiento del consumo. Este funciona por medio de una metodología Backpropagation algorithm optimizado con Adam, se realiza la clasificación de los usuarios con anomalías de lectura. En este se busca el valor mínimo de la función de error en el espacio de peso mediante una técnica llamada descenso de gradiente o regla delta. Las ponderaciones que minimizan la función de error se consideran una solución al problema de aprendizaje. Reducción de 70% al 20% de las rutas seleccionadas para visitas por anomalías Beneficios: – Reducción de costos operativos – Optimización de recursos – Detección de anomalías en centroides de energía'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'IA que detecta y cuantifica la contaminación de residuos de explosivos en suelos Inteligencia artificial que detecta y cuantifica, de manera ágil y rápida, la contaminación de residuos explosivos en diferentes suelos, basados en análisis multivariantes. Para el entrenamiento de la IA se realizaron estudios con tres diferentes tipos de suelos: – Bentonita – Suelo sintético – Suelo natural Para aumentar la selectividad, el modelo se entrenó y evaluó utilizando analitos adicionales como interferencias, incluidos otras sustancias y componentes explosivos y otros no explosivos.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Sistema de monitoreo inalámbrico que mide las variables de ph y conductividad en los cuerpos de agua Bucólicos es una empresa enfocada en la acuaponia e hidroponia la cual aporta a una mejor calidad de vida gracias a un proceso productivo cuya tecnología permite tener una producción limpia, libre de agroquímicos, versátil, adaptable, amigable con el medio ambiente y de tendencia km 0, esto garantiza poder ofrecer una variedad de productos agrícolas saludables, muy frescos, comercializados en una presentación 100% aprovechable y en un empaque que prolonga la conservación, facilita su uso, y ayuda a mantener la higiene. Gracias al programa Versos, AudacIA apoyó esta iniciativa desarrollando un sistema de monitoreo inalámbrico con autonomía en término de energía que se coloca en los cuerpos de agua para medir las variables de ph y conductividad. Estas se monitorean a través de una aplicación móvil llamado Hidrops Por medio de una app se reflejan los datos obtenidos de ph y conductividad, y reportes de datos históricos. Además, en la aplicación se pueden vincular diferentes dispositivos por medio de ID.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Desarrollando tecnologías en la industria de la moda Esta aplicación se diseñó con el fin de que los clientes puedan medirse prendas de vestir por medio de la realidad virtual. En el programa probeta en su versión 2020, se implementó este sistema para diseñar la tecnología para las tiendas RENZO como alternativa tecnológica para la reactivación economica de su sector.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Aplicativo móvil para la oferta de servicios de domicilio Motodomi una empresa que proporciona el servicio de logística de última milla y encomiendas directas. Gracias al programa Versos, AudacIA apoyó esta iniciativa desarrollando un aplicativo móvil que oferta servicios de domicilio y así mismo permite generar ingresos a terceros por medio del modo conductor. La aplicación ofrece el servicio de domicilios, recoger medicamentos y pagar facturas. Además, cuenta con rol cliente, rol conductor y rol administrativo, en donde cada uno podrá interactuar de manera personalizada en la app. Con un servicio digital de logística de última milla y encomiendas directas, que conecta a clientes y repartidores verificados de manera segura, tanto naturales como comerciales, para acortar los tiempos de envío a costos asequibles, desde la conveniencia de un aplicativo móvil.'},
    {'role': 'system', 'content': assistante + corta_respuesta + 'Aplicativo móvil para pruebas de sensores automotriz Adinel es un prototipo de un sistema para prueba de sensores automotriz, basado en tarjeta actual y número de entradas actuales. Gracias al programa Versos, AudacIA apoyó esta iniciativa desarrollando un aplicativo que recopila los datos obtenidos por el sensor.  Este se comunica de forma inalámbrica con una app para celular donde se visualizan los datos de las pruebas, reflejando así los resultados en tiempo real. En Adinel la confiabilidad y la información correcta del estado de un vehículo automotor es nuestra razón de ser, de allí que somos fabricantes de equipos de análisis tipo PALM ( portátil), el cual da un diagnóstico de los sensores del motor en tiempo real, de una manera ágil, sencilla, eficaz y económica, adicional fabricamos equipos de análisis de inyectores. Llevando a quienes usan los equipos un sello de transparencia en la revisión del vehículo y a los usuarios una confianza y credibilidad.'},

    {'role': 'system', 'content': 'Dispositivo que diagnostica daños en la retina Más de 2.000 millones de personas en el planeta sufren de alguna deficiencia visual o ceguera, los cuales generan un alto volumen de exámenes cuyo resultados demoran en la entrega a los pacientes Se desarrolló una plataforma basada en inteligencia artificial para la lectura de exámenes de retina, que ayuda oftalmólogos especialistas quienes necesitan realizar lectura de cada imagen por cada ojo de cada paciente, disminuyendo así, el tiempo empleado en la lectura de exámenes y agilizando la entrega de resultados. El equipo estaba formado por físicos, químicos, matemáticos e ingenieros de sistemas que mezclaron sus conocimientos con los especialistas de Cofca sumando un total de 12.000 horas de trabajo. Disminuir los tiempos de lectura, permitiendo mayor disponibilidad de tiempo para actividades de formación, y mejoraría la capacidad lectora de imágenes de los médicos, con inclusión de una nueva ventaja competitiva de ser personal médico con formación de expertos.'}
]
'''
messages_array = []

base_dir = os.path.dirname(__file__)
default_voice = os.path.join(base_dir,'mensaje_error.mp3')
idle_video = os.path.join(base_dir, "GAIA A1.mp4")
think_video = os.path.join(base_dir, "GAIA A2.mp4")
speak_video = os.path.join(base_dir, "GAIA A3.mp4")



# Define the video paths
video_paths = {
    "LISTENING": idle_video,
    "PROCESSING": think_video,
    "RESPONDING": speak_video
}

# Initialize the video player
video_player = None
global evento 
evento="LISTENING"

# Define the event callback function
def event_callback():
    global video_player, evento

    # Stop the current video
    if video_player is not None:
        video_player.release()
        video_player = None

    # Play the video for the current event
    if evento == "LISTENING":
        video_player = cv2.VideoCapture(video_paths["LISTENING"])
        print("LISTENING")
    elif evento == "PROCESSING":
        video_player = cv2.VideoCapture(video_paths["PROCESSING"])
        print("PROCESSING")
    elif evento == "RESPONDING":
        video_player = cv2.VideoCapture(video_paths["RESPONDING"])
        print("RESPONDING")
    
    # Loop through the video frames
    while True:
        ret, frame = video_player.read()
        if not ret:
            break

        # Show the frame
        cv2.imshow("Video", frame)

        # Exit the loop if the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the video player
    video_player.release()
    video_player = None

    # listen()
def decision(query):
    query.lower()
    if 'var' or 'bart'in query:
        print('hola')
    elif 'mari' in query:
        print('hols')


def listen():
    global evento
    
    evento = "LISTENING"
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print('Reconociendo...')
        query = r.recognize_google(audio, language='es-ES')
        print( query)
        messages_array.append({'role': 'user', 'content': query})
        evento = "PROCESSING"
        #respond(audio) if audio else respond(default_voice)
        decision(query)
               
    except Exception as e:
        # print('No te entiendo, repite, por favor', e)
        evento = "PROCESSING"
        speak("No te entiendo, repite, por favor")
    
   

#step 2 - respond to the new conversation item
def respond(audio): 
    global evento
    evento = "PROCESSING" 
    
    print('Respondiendo...')

    res = client.chat.completions.create(model='gpt-3.5-turbo-16k',
    messages=messages_array,
    temperature=0.65,
    n=1,
    max_tokens=800,
    stop=['.'])

    res_message = res.choices[0].message
    messages_array.append(res_message)
    print(res_message.content)
    speak(res_message.content)  
    evento = "PROCESSING" 
   


def speak(text):
    global evento

    evento = "RESPONDING"
    
    # event_callback()
    try:
        speech = gTTS(text=text, lang='es', slow=False)
        response_file = os.path.join(base_dir,'captured_voice.mp3')
        
        speech.save(response_file)
        os.system('afplay /Users/mari/Documents/py2/captured_voice.mp3 -r 1.2')# MacOS player
        os.remove(response_file)
        evento = "LISTENING"
    except:
        print("Speech not recognised")
        
    # listen()

# video_thread = threading.Thread(target=event_callback)
# video_thread.start()

audio_thread = threading.Thread(target=listen)
audio_thread.start()

# # event_callback()

# video_thread.join()
# audio_thread.join()


# if __name__ == '__main__':
    # llamar a la función freeze_support() antes de crear el proceso de animación
    # multiprocessing.freeze_support()

    # # create a process to display the animation
    # animation_process = multiprocessing.Process(target=event_callback)
    # animation_process.start()
    # while True:
    #     # listen for user input
    #     listen()

    #     # wait for the animation process to finish
    #     animation_process.join()


while True:
    # listen()
    #video_thread.join()
    # event_callback()
 
    audio_thread.join()
    time.sleep(1)