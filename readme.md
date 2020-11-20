
<h2 align="center">Python Kivy - kivy &nbsp;:heart:&nbsp;</h2>

<p align="center">
  
  <a href="https://github.com/BrianMarquez3/Python-Kivy/tags">
    <img src="https://img.shields.io/github/tag/BrianMarquez3/Python-Kivy.svg?label=version&style=flat" alt="Version">
  </a>
  <a href="https://github.com/BrianMarquez3/Python-Kivy/stargazers">
    <img src="https://img.shields.io/github/stars/BrianMarquez3/Python-Kivy.svg?style=flat" alt="Stars">
  </a>
  <a href="https://github.com/BrianMarquez3/Python-Kivy/network">
    <img src="https://img.shields.io/github/forks/BrianMarquez3/Python-Kivy.svg?style=flat" alt="Forks">
  </a>
</p>
  
![kivy](./images/Kivy.png)

## ¿Que es Kiby? 💻

Kivy es una biblioteca de código abierto de Python para el rápido desarrollo de interfaces de usuario multiplataforma. Las aplicaciones Kivy se pueden desarrollar para Linux, Windows, OS X, Android e iOS usando el mismo código base.

Los gráficos se procesan a través de OpenGL ES 2 en lugar de a través de widgets nativos, lo que lleva a una apariencia bastante uniforme en todos los sistemas operativos.

Desarrollar interfaces en Kivy opcionalmente implica el uso de kvlang, un pequeño lenguaje que admite expresiones similares a python e interoperabilidad de python. El uso de kvlang puede simplificar drásticamente el desarrollo de la interfaz de usuario en comparación con el uso exclusivo de Python. [RIPTUTORIAL](https://riptutorial.com/es/kivy).<br>

## Installing the kivy stable release

[Installation on Windows](https://kivy.org/doc/stable/installation/installation-windows.htmly).<br>
_bash_

```
pthon -m venv virt
```

```
sourse virt/Scripts/activate
```

<hr />

_Documentacion_

1. Ensure you have the latest pip, wheel, and virtualenv:

- First create the environment named kivy_venv in your current directory:

```
python -m virtualenv kivy_venv
```
-  Activate the virtual environment. You’ll have to do this step from the current directory every time you start a new terminal. On windows CMD do:

```
kivy_venv\Scripts\activate
```

-  If you’re in a bash terminal, instead do:

```
source kivy_venv/Scripts/activate
```

2. Install the dependencies (skip gstreamer (~120MB) if not needed, see Kivy’s dependencies). If you are upgrading Kivy, see Updating Kivy from a previous release

```
python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
python -m pip install kivy_deps.gstreamer==0.1.*
```

3. Install kivy:

```
python -m pip install kivy==1.11.1
```


<p style="color:#FF0000";>Red paragraph text</p>
