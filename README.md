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
 

Con esos valores, la fila correspondiente queda completa. Te dejo **la tabla actualizada** manteniendo el mismo formato:
| Autor / Referencia | Modelo utilizado                                                                                    | Estrategia                                                                                                                                                      |        Nº parámetros | Accuracy reportada | Loss train | Loss valid | Loss test |
| ------------------ | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------: | -----------------: | ---------: | ---------: | --------: |
| Nosotros           | Regresión logística                                                                                 | Obtener vector de características con HOG                                                                                                                       |            ~ (d × c) |            69.43 % |   0.000952 |     1.5265 |    1.5265 |
| Nosotros           | CNN simple (va bastante mal, deberíamos revisar los datos que le llegan al modelo, no aprende nada) | Crear una CNN más simple posible                                                                                                                                |           26,926,645 |              2.6 % |      0.016 |      3.305 |     3.393 |
| Nosotros           | RandomForestClassifier                                                                              | Modelo simple de machine learning                                                                                                                               | Total leaves: 368901 |            58.11 % |     1.1745 |     2.5337 |    2.5451 |
| Nosotros           | Modelo basado solo en Cov                                                                           | Usar matriz de covarianza como única representación global                                                                                                      |                1,484 |              4.2 % |      3.884 |      3.915 |     3.946 |
| Nosotros           | Modelo Complejo                                                                                     | Modelo de red neuronal convolucional (CNN) con una arquitectura inusual que combina elementos de codificación-decodificación y capas densas para clasificación. |            2,839,573 |             48.7 % |       0.53 |      1.638 |     1.775 |
| Nosotros           | CNN                                                                                                 | CNN con una capa *Dense* al final                                                                                                                               |           26,926,645 |              2.6 % |      3.884 |      3.915 |     3.946 |
| Nosotros           | **CNNComplejo_BEST**                                                                                | **Combinación de maxpooling y upsampling con hiperparámetros encontrados por finetuning repetido**                                                              |          **395,765** |         **91.7 %** |  **0.028** |  **0.271** | **0.327** |
