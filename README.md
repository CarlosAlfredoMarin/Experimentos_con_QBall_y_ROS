# Experimentos con QBall y ROS
Este repositorio contiene las carpetas, códigos y explicación de algunos experimentos básicos realizados con la librería Hector_Quadrotor, un modelo tridimensional del dron Quanser Qball2 y ROS.

![](https://github.com/CarlosAlfredoMarin/Experimentos_con_QBall_y_ROS/blob/main/Qball.png)


Para descargar los archivos de este repositorio y poder ejecutarlos en tu propio computador sigue las siguientes instrucciones.  
<br>

Se requieren instalar algunas dependencias de ROS. En una nueva terminal:
```
sudo apt-get install ros-noetic-ros-control ros-noetic-gazebo-ros-control ros-noetic-unique-identifier ros-noetic-tf2-geometry-msgs ros-noetic-laser-geometry ros-noetic-geographic-info ros-noetic-tf-conversions ros-noetic-joy
```

## Instalación Librería Hector

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
<br>


## Crear el Espacio de Trabajo
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

# ¿Cómo Lanzar los Experimentos?
Cada una de kas siguientes líneas de código se ejecutan en terminales separadas, por ejemplo, ```Lazo Abierto - Movimiento Circular``` tiene 2 líneas para ejecutarm usted debe abrir 2 terminales.

##Lazo Abierto - Movimiento Circular
```
roslaunch dron_cinematico lanzador_principal.launch
rosrun dron_cinematico movimiento_circular
```

##Lazo Cerrado - Trayectoria Lemniscata
```
roslaunch dron_cinematico lanzador_principal.launch
rosrun dron_cinematico lemniscata_helice
```

##Lazo Cerrado - Trayectoria Lemniscata y Gráfica
```
roslaunch dron_cinematico lanzador_principal.launch
rosrun dron_cinematico lemniscata_helice_grafica
roslaunch dron_cinematico visualizacion_graficas.launch
```

##Lazo Cerrado - Trayectoria, Líder-Seguidor
```
roslaunch dron_cinematico lanzador_2_quadrotores.launch
rosrun dron_cinematico lider_seguidor
```

##Lazo Cerrado - Trayectoria, Líder-Seguidor y Gráfica
```
roslaunch dron_cinematico lanzador_2_quadrotores.launch
```
```
rosrun dron_cinematico lider_seguidor_grafica
```
```
roslaunch dron_cinematico visualizacion_lider_seguidor_graficas.launch
```
