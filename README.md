# Clasificación de baraja de cartas inglesa

En este proyecto se propone desarrollar un sistema capaz de clasificar automáticamente una carta de una baraja inglesa a partir de una imagen de la misma. Es decir, dado un modelo de reconocimiento visual, el objetivo es identificar correctamente tanto el valor (As, 2, 3, ..., J, Q, K) como el palo (corazones, diamantes, tréboles o picas) de la carta mostrada en la fotografía. Este tipo de sistema puede resultar especialmente útil en entornos como competiciones de póker o casinos, donde es importante llevar un registro preciso y automatizado de las cartas que se juegan en cada partida.

En la siguiente tabla se resumen los enfoques y resultados reportados por algunos programadores que nos preceden, utilizando la métrica de accuracy, que es también la métrica principal considerada en un proyecto de clasificación de imagenes.

| Autor / Referencia | Modelo utilizado         | Estrategia                                | Accuracy reportada |
| ------------------ | ------------------------ | ----------------------------------------- | ------------------ |
| JAIGANESAN         | CNN entrenada desde cero | Entrenamiento completo (*from scratch*)   | 80 %               |
| JAIGANESAN         | ResNet152                | Modelo preentrenado (*transfer learning*) | > 95 %             |
| Efrain Perez       | CNN                      | Entrenamiento supervisado                 | 92.45 %            |
| Otros usuarios     | Modelos preentrenados    | Transfer learning  (EffecientNetB3)       | Hasta 98 %         |

Vamos a tratar de mejorar estas metricas tan altas usando tecnicas de machine learning modernas ya que la mayoria de estos resultados tienen ya un par de años.

# Nuestros modelos

En esta parte documentaremos las estadisticas de nuestros modelos.

| Autor / Referencia | Modelo utilizado    | Estrategia                                | Accuracy reportada | Loss train | Loss valid | Loss test |
| ------------------ | ------------------- | ----------------------------------------- | ------------------ | ---------- | ---------- | --------- |
| Nosotros           | Regresión logística | Obtener vector de características con HOG | 69.43 %            | 0.000952   | 1.5265     | 1.5265    |
| Nosotros           | CNN                 | Crear una CNN más simple posible          | 2.6 %              | 0.016      | 3.305      | 3.393     |


