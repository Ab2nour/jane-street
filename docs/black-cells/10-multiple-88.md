# Ligne 10 (multiple de 88)

![[Pasted image 20240715092315.png]]

## Premiers multiples

### Longueur 2

- 88

### Longueur 3

- 176
- 264
- 352
- 440
- 528
- 616
- 704
- 792
- 880
- 968

## Case (10, 3)

![img_2.png](../img/cells/black-cells/line-10/3/1.png)
![img_3.png](../img/cells/black-cells/line-10/3/2.png)

Le plus petit multiple de 88 est 88, puis le deuxième est 176, de longueur 3.

Si on noircit cette case :
![[Pasted image 20240714180339.png]]

alors il reste 2 cases à gauche, donc il faudrait mettre un multiple de 88 de longueur 2 dedans. Le seul étant 88, et les zones étant connexes, on arrive à une impossibilité.

![[Pasted image 20240714180534.png]]

Cette case ne peut pas être noire.

## Case (10, 7)

![img.png](../img/cells/black-cells/line-10/7/img.png)

![img_1.png](../img/cells/black-cells/line-10/7/img_1.png)

![img_2.png](../img/cells/black-cells/line-10/7/img_2.png)

Aucun multiple de 88 n'est de la forme aaab avec a = 1 ou a = 9

donc (10, 7 est blanche)

## Case (10, 8)

Supposons la case noire

![img.png](../img/cells/black-cells/line-10/8/img.png)

![img_1.png](../img/cells/black-cells/line-10/8/img_1.png)

![img_2.png](../img/cells/black-cells/line-10/8/img_2.png)

aucun multiple de 88 de longueur 3 ne commence par "11" ou "99"

donc (10, 8) est blanche

## Case (10, 9)

![img.png](../img/cells/black-cells/line-10/9/1.png)
![img_1.png](../img/cells/black-cells/line-10/9/2.png)

Même raisonnement que la case (10, 3).

![[Pasted image 20240714180630.png]]

Cette case ne peut pas être noire.

## Case (10, 11)

Supposons (10, 11) noire

![img.png](../img/cells/black-cells/line-10/11/img.png)

Utilisons les cases (8, 9) à (8, 11)

Il ne peut y avoir que 161 et 989 (forme aba et 1 3 7 9 de la ligne 9)

![img_1.png](../img/cells/black-cells/line-10/11/img_1.png)

![img_2.png](../img/cells/black-cells/line-10/11/img_2.png)

on aurait alors un multiple de 88 qui finit par 1 ou 9

sachant que 88 = 44 x 2, on aurait un multiple de 2 qui finit par 1 ou 9 => contradiction

Donc (10, 11) est blanche

## Case (10, 4)

Cette case est-elle noire ? 

![[Pasted image 20240714182148.png]]

1) Il existe un multiple de 88 de longueur 3, finissant par 2 fois le même nombre
2) Il n'y en a pas
    a) Soit 88 dans les cases vertes et la première case est noire
    b) Soit (10, 4) n'est pas noire

Le 1) est faux (cf les premiers multiples ci-dessus).

DONC 
- soit (10, 4) est blanche
- soit (10, 4) et (10, 1) sont noires, et les cases vertes contiennent 88
![[Pasted image 20240714182556.png]]


## Case (10, 7)

Cette case est-elle noire ? 

![[Pasted image 20240714181848.png]]

S'il n'existe aucun multiple de 88 finissant par 3 fois le même nombre, de longueur 5 ou 6, alors cette case ne peut pas être noire.
