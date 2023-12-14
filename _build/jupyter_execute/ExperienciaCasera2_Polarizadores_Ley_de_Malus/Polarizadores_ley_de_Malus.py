#!/usr/bin/env python
# coding: utf-8

# # EXPERIENCIA CASERA 2
# 
# # Polarizadores y Ley de Malus
# 
# Para realizar esta experiencia es necesario disponer de dos pequeñas láminas polarizadoras que se pueden comprar en muchos establecimientos. A modo de ejemplo el [siguiente enlace](https://www.amazon.es/s?k=l%C3%A1mina+polarizada&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2DMSIZKOSMDBS&sprefix=l%C3%A1mina+polarizada%2Caps%2C103&ref=nb_sb_noss_1) lleva a la tienda de Amazon donde aparecen diferentes propuestas de láminas polarizadoras. NOTA: Los autores no tienen ninguna relación con Amazon y únicamente se proporciona dicho enlace con el fin de facilitar la búsqueda de las láminas.
# 

# ## Introducción
# 
# Las ondas electromagnéticas planas son ondas vectoriales transversales: el campo eléctrico
# de la onda oscila contenido en un plano perpendicular a la dirección de propagación de la misma.
# Sin embargo, la dirección del campo en este plano puede mantenerse fija o cambiar. En general,
# las fuentes de luz producen luz despolarizada. Ello significa que la dirección del campo eléctrico  $\vec{E_0}$ cambia al azar de un instante a otro, tal como se indica en la figura 1\(a\), donde se han dibujado
# algunos vectores orientados al azar en diferentes instantes de tiempo. La luz proveniente del sol, o
# la que producen las bombillas de incandescencia o los fluorescentes, está despolarizada.
# 
# <img src=".Polarizadores_ley_de_Malus.ipynb.upload/paste-0.18964571241733863" style="max-width:100%" />
# 
# Se puede conseguir que el campo eléctrico de la onda mantenga una dirección fija en un plano.
# En este caso se dice que el haz de luz está linealmente polarizado. Existen diversas maneras de
# conseguir esto, y una de ellas consiste en hacer pasar un haz de luz despolarizado a través de un
# material especial que denominamos polarizador lineal. Este material transmite la componente del
# campo eléctrico de la onda que vibra paralelamente a una dirección privilegiada del material, que
# se denomina eje de transmisión del polarizador, y absorbe el campo que vibra en la dirección
# perpendicular a dicho eje. Por tanto a la **salida del polarizador** tendremos luz **linealmente**
# **polarizada en la dirección del eje de transmisión del polarizador**.
# En la figura 1\(b\) se muestra un ejemplo, supongamos que el campo eléctrico $\vec{E_0}$
# del haz incidente forma un ángulo $\theta$ con la vertical y que el material polarizador tiene su eje de transmisión en la
# dirección vertical. El material polarizador solo dejará pasar la proyección del campo incidente en
# la dirección del eje del polarizador, esto es, $E_0 \cos(\theta)$. Y por tanto la irradiancia a la salida del
# polarizador vendrá dada por:
# 
# $$I = I_0 \cos^2(\theta)$$
# 
# donde $I_0$ es la irradiancia del haz que incide sobre el material polarizador. Esta expresión es
# conocida como la **ley de Malus**, que proporciona el grado de atenuación del haz que emerge de un
# polarizador.
# 
# Si aplicamos esta idea al caso de un haz incidente despolarizado, el vector eléctrico $\vec{E_0}$
#  formará un ángulo $\theta(t)$ con el eje que irá cambiando al azar. Por lo tanto, en la irradiancia del haz transmitido
# tendremos que promediar todos los posibles valores que tomará el coseno al cuadrado del ángulo.
# Dicho promedio es 1/2, es decir, la irradiancia transmitida resulta ser $I = I_0 /2$.
# 
# Teniendo en cuenta lo anterior, podemos establecer un procedimiento para atenuar un haz de
# luz despolarizada empleando sucesivamente dos polarizadores: el primero de ellos permite atenuar
# la irradiancia en un factor 1/2 y si colocamos un segundo polarizador con su eje formando un cierto
# ángulo con el eje del primero, podemos variar a voluntad la irradiancia transmitida por el sistema
# formado por los dos polarizadores. Así obtenemos entonces un filtro de atenuación variable sin más
# que cambiar el ángulo relativo entre los ejes de transmisión de los dos polarizadores.
# 

# ## Análisis de polarizadores y Ley de Malus
# 
# El siguiente vídeo muestra el procedimiento para analizar el efecto de una lámina polarizadora en la luz así como el procedimiento para comprobar experimentalmente la ley de Malus anteriormente expuesta. Para ello, además de las dos pequeñas láminas polarizadores, será necesario disponer de:
# 
# - Un transportador de ángulos o similar. En el [siguiente documento](plantilla_angulos.pdf) se facilita una plantilla igual que la que se presenta en el vídeo para poder ser impresa y realizar la experiencia.
# - Una aplicación para el móvil que nos permita acceder a los valores que mide el sensor de luz. Hay muchas aplicaciones y cualquiera es válida. Para dispositivos Android, algunas de estas aplicaciones podrían ser [Phyphox](https://play.google.com/store/apps/details?id=de.rwth_aachen.phyphox) o [Light Meter Pro](https://play.google.com/store/apps/details?id=com.doggoapps.luxlight) \(Nota: Estos enlaces se proporcionan únicamente como ejemplos de aplicaciones para realizar la experiencia casera. Los autores de este documento no tienen ningún tipo de relación con los creadores de estas aplicaciones\).
# 
# 
# <video src="../_static/videos/ExperienciaCasera2_LeydeMalus_1.mp4" width=400px controls></video>
# 

# Una vez medidos los valores de la irradiancia en función del ángulo formado por los ejes de transmisión de los dos polarizadores, podemos realizar una ajuste lineal de los datos y así comprobar la ley de Malus. Para ello debemos representar las dos magnitudes que son proporcionales según la ley de Malus, es decir, la irradiancia y el coseno al cuadrado del ángulo. El ajuste lineal se puede realizar con cualquier programa de cálculo o usando la aplicación desarrollada para Android que se puede descargar del enlace  [https://play.google.com/store/apps/details?id=appinventor.ai\_oscar\_gomezcalderon.AjusteLineal\_ShaDB&hl=es&gl=US&pli=1](https://play.google.com/store/apps/details?id=appinventor.ai_oscar_gomezcalderon.AjusteLineal_ShaDB&hl=es&gl=US&pli=1)
# 
# 
