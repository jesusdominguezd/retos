# ¿Qué es un IOC y los TTPs de un adversario? 
Primero comenzamos definiendo un IOC, que no es más que una descripción de un incidente de ciberseguridad, actividad y artefacto malicioso mediante patrones para ser identificado en una red o endpoint pudiendo mejorar asi las capacidades antes la gestión de incidentes

Segundo definimos los TTPs como tácticas, técnicas y procedimientos, en un sentido más practico las tácticas describen en rasgos generales el comportamiento, las técnicas nos dan una descripción más detallada del comportamiento de las tácticas y el procedimiento nos dé una descripción muy detallada acerca del comportamiento de la técnica

Sentado lo anterior tenemos que los IOCs de un adversario son los rastros de su actividad y los TTPs es la manera en cómo comprometen un activo.

Un uso de los IOC es cuando a partir de estos se crean planes y estrategias ante un riesgo latente de ciber ataque, asi mismo se pueden integrar en aplicativos como:
* IDS
* IPS
* Firewalls
Esto con el objetivo de una temprana detección.

Y los TTPs ayudan a correlacionar un ataque con el atacante o grupo de amenazas conocido y con esto entender mejor el contexto del ataque, de igual manera nos ayudan a guiarnos en la ruta de la investigación de la amenaza asi como identificar los vectores de ataque, definir la gravedad de la amenaza y responder correctamente a un incidente y aplicar una correcta mitigación.

# ¿Qué es un SIEM y como podría aprovecharlo una organización?
Un Security Information and Event Management (SIEM) es software que tiene la tarea de monitorear activamente la red y los dispositivos conectados a esta, al mismo tiempo que tiene la capacidad de detectar, responder y neutralizar ciberamenzas.

Una organización puede aprovechar esta tecnología en su seguridad perimetral, previniendo de esta manera ataques externos, pero tambien controlando amenazas internas, generalmente el SIEM es gestionado por el SOC.

# ¿Qué es Cyber Threat Intelligence y como puede ser utilizado en las organizaciones?
Es una disciplina que tiene como objetivo principal recopilar datos de todas las fuentes disponibles, tanto públicas como privadas y con esto tomar decisiones adecuadas con base en estos datos, esto se puede utilizar para perfilar a un adversario y tomar las medidas preventivas para evitar un incidente de seguridad o en un caso extremo, responder a uno.

# ¿Qué es el cyber kill chain? Describe un ejemplo de las fases en un ataque
Es un modelo que divide un ciber ataque en 7 pasos bien identificados y diferenciados.
## Reconocimiento
Se recolecta información acerca del objetivo, se suele usar OSINT, algunos scanners para detectar vulnerabilidades y puertos de acceso, se recopila información acerca de sus sistemas de seguridad existentes
## Preparación
En esta etapa se perfilan los vectores de ataque que se pueden usar contra el objetivo, generalmente se usa la ruta de menor resistencia, algunos ejemplos de vectores de ataque son:
* Credenciales poco seguras o robadas
* Insiders
* Errores en la configuracion de sus sitemas
* Ingenieria social
* Errores humanos
## Entrega
Una vez dentro podemos plantar cualquier artefacto malicioso para continuar el ataque, algunos ejemplos son:
* Downloaders
* Info stealer
## Explotación
Consiste en la activación del artefacto malicioso, estos se pueden detonar mediante acciones específicas o directamente en los sistemas, estos artefactos ya se encuentras ofuscados o contienen técnicas para evitar la detección
## Instalación
Es en esta etapa donde se pueden instalar puertas traseras para acceder al objetivo más adelante con el fin de tener un libre acceso al objetivo comprometido
## Comando y control
Una vez que tenemos el terreno preparado se toma el control para continuar con el ataque, mantener el control del objetivo y/o exfiltrar datos
## Acciones sobre el objetivo
Esta es una fase de ejecución continua del ataque, donde podemos tomar diferentes acciones sobre el objetivo, se puede cifrar información para pedir un rescate, exfiltrar datos, vigilar el comportamiento del sistema, ataques de denegación de servicio por mencionar algunos ejemplos

# ¿Para qué sirven los comandos awk, grep, sed, cut, |, find, ps y como pueden ser aprovechados por los usuarios? Describe un ejemplo de su uso

## awk
Es un lenguaje de scripting y es muy útil cuando se trabajan textos largos en la terminal ya que nos permite procesar todo el texto.
### Uso
Se puede usar para buscar una palabra dentro de un texto
```bash
$ awk '{action}' your_file_name.txt
```
Se puede usar regex para buscar un patron en un texto
```bash
$ awk '/regex pattern/{action}' your_file_name.txt
```
## grep
Este comando se usa para buscar patrones de caracteres dentro de un archivo, el comando nos mostrara todas las líneas donde nuestro patrón de búsqueda aparezca
### Uso
La opcion -i habilita el case insensitive
```bash
$ grep -i "UNix" your_file_name.txt
```
La opcion -w busca la palabra completa en un archivo
```bash
$ grep -w "unix" your_file_name.txt
```
## sed
Es un comando que nos sirve para varias funciones como buscar, buscar y reemplazar, insertar y borrar.
### Uso
Reemplazar un string
```bash
$ sed 's/unix/linux/' your_file_name.txt
```
Reemplazar todas las ocurrencias del patrón en una línea
```bash
$ sed 's/unix/linux/g' your_file_name.txt
```
## cut
Este comando nos sirve para "recortar" secciones de archivos o líneas, nos da el resultado en standard output
### Uso
La opción -b extrae los bytes especificados
```bash
$ cut -b 1,2,3 your_file_name.txt
```
La opción -f nos permite traer un campo seleccionado y con el flag -d podemos poner un delimitador, esto es útil para archivos separados por comas, espacios, guiones, etc.
```bash
$ cut -d "delimiter" -f (field number) your_file_name.txt
```
## pipe (|)
Nos sirve para encadenar comandos, pasa el standard output de un comando al standard input de otro comando.
### Uso
Se encadenan 3 comandos para obtener un campo de las primeras líneas de un archivo
```bash
$ cat your_file_name.txt | head -n 3 | cut -d ' ' -f 1 > list.txt
```
## find
Es un comando que nos permite navegar en los directorios en linux, se puede usar para encontrar archivos y directorios
### Uso
Buscar por nombre
```bash
$ find ./my_dir -name your_file_name.txt
```
Buscar por permisos del archivo
```bash
$ find ./my_dir -perm 664
```
## ps
Con este comando podemos ver información acerca de los procesos que corren en un sistema Linux
### Uso
Ver todos los procesos
```bash
$ ps -a
```
Ver todos los procesos corriendo
```bash
$ ps -r
```

