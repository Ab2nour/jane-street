# Ligne 8 (multiple de 23 palindrome)

Le plus petit palindrome multiple de 23 est 161, de longueur 3. Donc les nombres de la ligne 8 sont de longueur 3 minimum, donc les colonnes 3 et 9 de la ligne 8 sont blanches.

- Longueur 3 minimum
- 

![[Pasted image 20240714180014.png]]
![[Pasted image 20240715092239.png]]


## Couleurs 

### Cases blanches

- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 9
- 10
- 11

### Cases noires

- 8

## Premiers

- 161
- 414
- 575
- 828
- 989
- 1771
- 4554
- 7337

longueur 7 avec la forme attendue :

- 3375733
- 7714177
- 7796977
- 9970799

## Case (8, 1)

la résolution ici dépend de toutes les autres cases de la ligne 8

![img.png](../img/cells/black-cells/line-8/1/img.png)

supposons (8, 1) noire

![img_1.png](../img/cells/black-cells/line-8/1/img_1.png)

![img_2.png](../img/cells/black-cells/line-8/1/img_2.png)

(8, 1) ne peut être noire sinon la structure de palindrome est invalide

donc (8, 1) est blanche


## Case (8, 3)

![](../img/cells/black-cells/line-8/3/1.png)
![](../img/cells/black-cells/line-8/3/2.png)

- ne respecte pas longueur 3 minimum
- ne peut pas être noire

## Case (8, 4)

![](../img/cells/black-cells/line-8/4/1.png)
![](../img/cells/black-cells/line-8/4/2.png)

- ne respecterait pas la structure de palindrome pour le nombre à gauche
- ne peut pas être noire

## Case (8, 5)

![img_8.png](../img/cells/black-cells/line-8/8/img_8.png)

(8, 8) est noire, et le plus petit nombre compatible est de taille 3



## Case (8, 6)

![img.png](../img/cells/black-cells/line-8/6/1.png)

2 cas :

(8, 1) noir

![img_1.png](../img/cells/black-cells/line-8/6/2.png)

![img_2.png](../img/cells/black-cells/line-8/6/3.png)

les seules possibilités sont :

- 1771
- 4554
- 7337

Aucune ne correspond au motif.

Examinons le cas où (8, 1) est blanc

![img_3.png](../img/cells/black-cells/line-8/6/4.png)

![img_4.png](../img/cells/black-cells/line-8/6/5.png)

de la forme aa b c d, ne peut pas être un palindrome

Donc (8, 6) est blanche.

## Case (8, 7)

![img.png](../img/cells/black-cells/line-8/7/1.png)

Soit (8, 11) est noire

![img_1.png](../img/cells/black-cells/line-8/7/2.png)

![img_2.png](../img/cells/black-cells/line-8/7/3.png)

de la forme aa b, ne peut pas être un palindrome

Soit (8, 11) est blanche

![img_4.png](../img/cells/black-cells/line-8/7/4.png)

![img_3.png](../img/cells/black-cells/line-8/7/5.png)

de la forme aa b c, ne peut pas être un palindrome

donc (8, 7) est blanche

## Case (8, 8)

Dépendance aux colonnes :

- 2
- 3
- 4
- 6
- 7
- 9
- 10

Supposons que (8, 8) est blanche (déjà essayé de supposer qu'elle était noire, pas de contradiction)

![img.png](../img/cells/black-cells/line-8/8/img.png)

soit (8, 5) est noire

![img_1.png](../img/cells/black-cells/line-8/8/img_1.png)

![img_2.png](../img/cells/black-cells/line-8/8/img_2.png)

de la forme aa bb c, ou aa bb c d en fonction de la couleur de (8, 11)

Dans les deux cas, aa bb c et aa bb c d ne sont pas des formes de palindromes valides

donc (8 ,8) blanche => (8, 5) blanche

![img_3.png](../img/cells/black-cells/line-8/8/img_3.png)

soit (8, 1) blanche

![img_4.png](../img/cells/black-cells/line-8/8/img_4.png)

prenons cette portion

![img_5.png](../img/cells/black-cells/line-8/8/img_5.png)

de la forme aa b c

si (8, 11) est blanche

![img_6.png](../img/cells/black-cells/line-8/8/img_6.png)

de la forme cc b a, donc pas compatible avec aa b c => pas possible de faire un palindrome

donc (8, 11) ne peut pas être blanche

essayons avec (8, 11) noire

![img_7.png](../img/cells/black-cells/line-8/8/img_7.png)

la ligne finit par un motif avec deux chiffres différents, donc incompatible avec le début de la ligne qui commence par 2 chiffres identiques, pour avoir un palindrome

donc (8, 8) est noire

## Case (8, 9)

![](../img/cells/black-cells/line-8/9/1.png)
![](../img/cells/black-cells/line-8/9/2.png)

- ne respecte pas longueur 3 minimum
- ne peut pas être noire

## Case (8, 11)

![img_8.png](../img/cells/black-cells/line-8/8/img_8.png)

(8, 8) est noire, et le plus petit nombre compatible est de taille 3


## Todo 

Utiliser les zones de contact avec le même nombre

(8, 7)
![[Pasted image 20240715100648.png]]

