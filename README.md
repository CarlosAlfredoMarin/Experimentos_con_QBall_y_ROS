# Experimentos con QBall y ROS
Este repositorio contiene las carpetas, códigos y explicación de algunos experimentos básicos realizados con la librería Hector_Quadrotor, un modelo tridimensional del dron Quanser Qball2 y ROS.

![](https://github.com/CarlosAlfredoMarin/Experimentos_con_QBall_y_ROS/blob/main/Qball.png)

# Índice
0. [Instalación ROS Noetic en Ubuntu 20.04 LTS](#id0)
1. [Instalación Librería Hector](#id1)
2. [Crear el Espacio de Trabajo](#id2)
3. [¿Cómo Lanzar los Experimentos?](#id3)
      - [Lazo Abierto - Movimiento Circular](#id4)
      - [Lazo Cerrado - Trayectoria Lemniscata](#id5)
      - [Lazo Cerrado - Trayectoria Lemniscata y Gráfica](#id6)
      - [Lazo Cerrado - Trayectoria, Líder-Seguidor](#id7)
      - [Lazo Cerrado - Trayectoria, Líder-Seguidor y Gráfica](#id8)  
<br><br>


<div id='id0' />

# Instalación ROS Noetic en Ubuntu 20.04

Antes de instalar ROS Noetic, se debe tener Ubuntu 20.04 instalado en su máquina, tener acceso de root para poder utilizar el superusuario a la hora de las instalaciones y además tener una buena conexión a internet.

## Configuración del archivo *sources.list*
Para instalar Noetic en Ubuntu 20.04, primero se necesita agregar el repositorio oficial de ROS Noetic a *sources.list*, esto permite a la configuración de la computadora aceptar software de *packages.ros.org*.


~~~
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
~~~

Posteriormente, digite su contraseña de usuario.

## Agregar llave oficial ROS
Se necesita agregar la llave ROS Noetic para obtener paquetes ROS autenticados.

~~~
sudo apt install curl -y
~~~

~~~
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
~~~

Debería aparecer en pantalla la palabra *OK*.

## Actualizar el índice del paquete ROS
A continuación, se necesita obtener la información del paquete ROS Noetic del repositorio que se acaba de agregar usando:

~~~
sudo apt update
~~~

~~~
sudo apt upgrade -y
~~~

Instalar herramientas de red:
~~~
sudo apt-get install net-tools
~~~

## Instalar Paquete Ros Noetic
Se instala el paquete mas completo, este es el mas recomendado ya que cuenta con
todo en el escritorio, más simuladores 2D/3D y paquetes de percepción 2D/3D.

~~~
sudo apt install ros-noetic-desktop-full
~~~

Cuando el sistema le pida confirmación, debe presionar '*Y*' seguidamente la tecla '*ENTER*' para continuar con la instalación. Este proceso toma alrededor de 10 a 20 minutos.


## Configuración del entorno
Se utiliza la siguiente línea de código, con el fin de poder usar los comandos de la terminal ROS, utilizar el creador de paquetes catkin y a su vez encontrar los archivos de su programa ROS, como los archivos de encabezado en su directorio:

~~~
source /opt/ros/noetic/setup.bash
~~~

**Recomendación:** Para evitar ejecutar el comando setup.bash de manera manual
cada vez que se abre una terminal, lo cual es necesario para desarrollar con ROS, se recomienda colocarlo en el .bashrc, archivo ubicado en el directorio raiz (∼). Para hacerlo, ejecutar lo siguiente:

~~~
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
~~~

~~~
source ~/.bashrc
~~~

## Dependencias para la construcción de paquetes
Para crear y administrar sus propios espacios de trabajo ROS, existen varias herramientas y requisitos que se distribuyen por separado. Por ejemplo, rosinstall es una herramienta de línea de comandos de uso frecuente, que le permite descargar fácilmente muchos árboles de origen para paquetes ROS con un solo comando. Para instalar esta herramienta y otras dependencias cuya función es construir paquetes ROS, es necesario ejecutar:

~~~
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential python3-rostopic
~~~

## Inicializacion de Rosdep
Antes de utilizar muchas herramientas ROS, deberá inicializar rosdep, esto le permite instalar fácilmente las dependencias del sistema para la fuente que desea compilar y su vez, es necesario para ejecutar algunos componentes centrales en ROS:

~~~
sudo apt install python3-rosdep
~~~

~~~
sudo apt install python3-rostopic
~~~

Para inicializar rosdep:
~~~
sudo rosdep init
~~~
~~~
rosdep update
~~~

## Verificación de Instalación
Para verificar el correcto funcionamiento de ROS se ejecutará una estructura en la cual se ejecuta el master, posteriormente, se utilizará un nodo de suscripción (para visualizar una tortuga), luego un nodo que publica información de posición y seguidamente se utiliza un nodo para mover la tortuga.

Verificamos que se tenga instalado ROS, al ejecutar el comando siguiente:

~~~
roscd
~~~

se debe obtener una línea como esta
~~~
/opt/ros/noetic
~~~
Para regresar al directorio raíz ingrese 
~~~
cd
~~~

Seguidamente se instala el paquete turtlesim, normalmente la instalación de ROS viene con este paquete por defecto, en caso contrario, ejecutar el siguiente comando:

~~~
sudo apt install ros-noetic-turtlesim
~~~

Se inicializa el roscore, con esto se ejecuta el master

~~~
roscore
~~~

Posteriormente, se abre otra terminal y se listan los canales de comunicación (topic)

~~~
rostopic list
~~~

Al correr el master, por defecto, como resultado se deben mostrar los siguientes canales

~~~
/rosout
/rosout_agg
~~~

Se ejecuta el nodo turtlesim

~~~
rosrun turtlesim turtlesim_node
~~~

Se abre otra terminal, para volver a listar los canales de comunicación
~~~
rostopic list
~~~

ahora se debe tener como resultado los siguientes:

~~~
/rosout
/rosout_agg
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose
~~~


Ahora, se procede a suscribirse al topíco /turtle1/cmd_vel para visualizar la posición lineal y angular


~~~
rostopic echo /turtle1/cmd_vel
~~~

Se abre otra terminal y se ejecuta el nodo turtle_teleop_key con las flechas se manipula la tortuga

~~~
rosrun turtlesim turtle_teleop_key
~~~

Nota: para finalizar los procesos en las terminales se utiliza Ctrl + C.

Recomendaciones: instalar el software T erminator para un facil manejo de las terminales

~~~

sudo apt-get install terminator
~~~
<br><br>





<div id='id1' />

# Instalación Librería Hector

Para descargar los archivos de este repositorio y poder ejecutarlos en tu propio computador sigue las siguientes instrucciones.  
<br>

Se requieren instalar algunas dependencias de ROS. En una nueva terminal:
```
sudo apt-get install ros-noetic-ros-control ros-noetic-gazebo-ros-control ros-noetic-unique-identifier ros-noetic-tf2-geometry-msgs ros-noetic-laser-geometry ros-noetic-geographic-info ros-noetic-tf-conversions ros-noetic-joy
```

Crear una carpeta en el usuario raíz
```
mkdir -p ~/hector_ws/src
cd hector_ws/src
```

Ahora, procedemos a descargar la librería, dentro de la carpeta ```src```:
```
git clone  https://github.com/tu-darmstadt-ros-pkg/hector_quadrotor
git clone  https://github.com/tu-darmstadt-ros-pkg/hector_localization
git clone  https://github.com/tu-darmstadt-ros-pkg/hector_gazebo
git clone  https://github.com/tu-darmstadt-ros-pkg/hector_models
```

Compilamos, el espacio de trabajo
```
cd ..
catkin_make
echo "source ~/hector_ws/devel/setup.bash" >> ~/.bashrc 
source ~/.bashrc
```  
<br><br>



<div id='id2' />

# Crear el Espacio de Trabajo
En una nueva terminal:  

Crear una carpeta en el usuario raíz
<pre><code>mkdir -p ~/my_ws/src </code></pre>

Entramos a la carpeta
<pre><code>cd ~/my_ws/src </code></pre>

Inicializamos el espacio de trabajo
<pre><code>catkin_init_workspace </code></pre>

Salimos de la carpeta src
<pre><code>cd .. </code></pre>

Compilamos el espacio de trabajo
<pre><code>catkin_make </code></pre>

Observamos el listado de carpetas que se han creado
<pre><code>ls </code></pre>

Siempre que abramos un terminal nuevo debemos ejecutar un fichero de inicialización
<pre><code>source ~/my_ws/devel/setup.bash </code></pre>

Otra opción, es crear un fichero de inicialización que ejecute ese comando automáticamente,
```
echo "source ~/my_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

Ahora, procedemos a clonar este repositorio, dentro de la carpeta ```src```:
```
cd ~/my_ws/src </code></pre> 
git clone https://github.com/CarlosAlfredoMarin/Experimentos_con_Libreria_Hector
```

Compilamos, nuevamente, el espacio de trabajo
```
cd ~/my_ws
catkin_make
```   
<br><br>








<div id='id3' />

# ¿Cómo Lanzar los Experimentos?
Cada una de kas siguientes líneas de código se ejecutan en terminales separadas, por ejemplo, ```Lazo Abierto - Movimiento Circular``` tiene 2 líneas, usted debe abrir 2 terminales, una para cada línea de código.

<div id='id4' />

## Lazo Abierto - Movimiento Circular

[Movimiento Circular]

[Movimiento Circular]: https://github.com/CarlosAlfredoMarin/Experimentos_con_QBall_y_ROS/tree/main/dron_cinematico/src/movimiento_circular

```
roslaunch dron_cinematico lanzador_principal.launch
```
```
rosrun dron_cinematico movimiento_circular
```



<div id='id5' />

## Lazo Cerrado - Trayectoria Lemniscata

[Trayectoria Lemniscata]

[Trayectoria Lemniscata]: https://github.com/CarlosAlfredoMarin/Experimentos_con_QBall_y_ROS/tree/main/dron_cinematico/src/lemniscata_helice

```
roslaunch dron_cinematico lanzador_principal.launch
```
```
rosrun dron_cinematico lemniscata_helice
```



<div id='id6' />

## Lazo Cerrado - Trayectoria Lemniscata y Gráfica

[Trayectoria Lemniscata y Gráfica]

[Trayectoria Lemniscata y Gráfica]: https://github.com/CarlosAlfredoMarin/Experimentos_con_QBall_y_ROS/tree/main/dron_cinematico/src/lemniscata_helice_grafica

```
roslaunch dron_cinematico lanzador_principal.launch
```
```
rosrun dron_cinematico lemniscata_helice_grafica
```
```
roslaunch dron_cinematico visualizacion_graficas.launch
```




<div id='id7' />

## Lazo Cerrado - Trayectoria, Líder-Seguidor

[Trayectoria, Líder-Seguidor]

[Trayectoria, Líder-Seguidor]: https://github.com/CarlosAlfredoMarin/Experimentos_con_QBall_y_ROS/tree/main/dron_cinematico/src/lider_seguidor

```
roslaunch dron_cinematico lanzador_2_quadrotores.launch
```
```
rosrun dron_cinematico lider_seguidor
```



<div id='id8' />

## Lazo Cerrado - Trayectoria, Líder-Seguidor y Gráfica

[Trayectoria, Líder-Seguidor y Gráfica]

[Trayectoria, Líder-Seguidor y Gráfica]: https://github.com/CarlosAlfredoMarin/Experimentos_con_QBall_y_ROS/tree/main/dron_cinematico/src/lider_seguidor_grafica

```
roslaunch dron_cinematico lanzador_2_quadrotores.launch
```
```
rosrun dron_cinematico lider_seguidor_grafica
```
```
roslaunch dron_cinematico visualizacion_lider_seguidor_graficas.launch
```
