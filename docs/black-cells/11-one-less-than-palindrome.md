# Ligne 11 (1 less than a palindrome)

à revoir en fait... je n'ai pas pris en compte si on noircissait (11, 1)
![[Pasted image 20240715094550.png]]

==> en fait si je pense que c'est bon

![[Pasted image 20240715100003.png]]

## Case (11, 3)

Supposons la case noire

![img_3.png](../img/cells/black-cells/line-11/3/img_3.png)

Il nous faudrait 1 de moins qu'un palindrome, de longueur 2, avec 2 chiffres égaux... On a une contradiction.

(11, 3) est blanche

## Case (11, 4)

![img.png](../img/cells/black-cells/line-11/4/img.png)

Il nous faudrait 1 de moins qu'un palindrome, de longueur 3, avec 3 chiffres égaux, contradiction.

Ou alors de longueur 2 si on suppose (11, 1) noire. Cela revient au même, impossible

(11, 4) est blanche

## Case (11, 5)

![img.png](../img/cells/black-cells/line-11/5/img.png)

palindrome - 1 de longueur 3 ou 4, avec tous les chiffres identiques

impossible

(11, 5) est blanche


## Case (11, 6)

Supposons (11, 6) noire

![img.png](../img/cells/black-cells/line-11/6/img.png)

Soit (11, 1) est noire, soit (11, 3) est noire (ou exclusif)

(11, 3) noire

![img_1.png](../img/cells/black-cells/line-11/6/img_1.png)

palindrome - 1 de longueur 2 de la forme aa, impossible

(11, 1) noire

![img_2.png](../img/cells/black-cells/line-11/6/img_2.png)

palindrome - 1 de la forme aaaa, impossible

(11, 6) est blanche



## Case (11, 8)

Dépendances
- de (11, 3) à (11, 5) blanches

Supposons (11, 8) noire

![img.png](../img/cells/black-cells/line-11/8/img.png)

![img_1.png](../img/cells/black-cells/line-11/8/img_1.png)

de 1 à 7

ou de 2 à 7

on aurait une structure

aaaa bb ou aaaaa bb, les palindromes sous-jacents seraient aaaa ba ou aaaaa ba

dans les deux cas, ce n'est pas une forme de palindrome valide

donc (11, 8) est blanche

## Case (11, 7)

dépendances :
- (11, 2) à (11, 10) sauf (11, 7)

Elle pourrait être noire (les deux côtés en résultant donnent des positions valides)

Supposons (11, 7) blanche

![img.png](../img/cells/black-cells/line-11/7/img.png)

4 cas :

1) (11, 1) blanche et (11, 11) blanche
2) (11, 1) blanche et (11, 11) noire
3) (11, 1) noire et (11, 11) blanche
4) (11, 1) noire et (11, 11) noire

### cas 1, (11, 1) blanche et (11, 11) blanche

![img_1.png](../img/cells/black-cells/line-11/7/img_1.png)

![img_2.png](../img/cells/black-cells/line-11/7/img_2.png)

structure de palindrome impossible

### cas 2, (11, 1) blanche et (11, 11) noire

![img_3.png](../img/cells/black-cells/line-11/7/img_3.png)

![img_4.png](../img/cells/black-cells/line-11/7/img_4.png)

structure de palindrome impossible

### cas 3, (11, 1) noire et (11, 11) blanche

![img_5.png](../img/cells/black-cells/line-11/7/img_5.png)

![img_6.png](../img/cells/black-cells/line-11/7/img_6.png)

structure de palindrome impossible

### cas 4, (11, 1) noire et (11, 11) noire

![img_7.png](../img/cells/black-cells/line-11/7/img_7.png)

![img_8.png](../img/cells/black-cells/line-11/7/img_8.png)

structure de palindrome impossible

Aucun cas ne marche, donc (11, 7) est noire

## Case (11, 9)

dépendances :
- (11, 3) à (11, 6), et (11, 8)

Supposons (11, 9) noire

![img.png](../img/cells/black-cells/line-11/9/img.png)

de 1 à 8 ou de 2 à 8 on a 5a 3b ou 4a 3b

palindromes sous-jacents 5a 2b a ou 4a 2b a

pas une forme de palindrome valide

donc (11, 9) est blanche

## Case (11, 11)

en fait si c'était 1 en 11,9 et 11,10, on ne pourrait pas décider de si la case (11, 11) est noire ou blanche
or, on nous promet une solution unique, donc on est contraint de choisir 9 en case (11, 9) et (11, 10), pour ne pas aboutir à une impasse 

random : ~~par exemple si c'était 1, on aurait le choix entre 3-1-1-noir et 3-1-1-2
ou 411n et 4113 etc etc
et c'est indécidable, ça contredirait le fait qu'il y ait une solution unique~~

en fonction du contenu de (10, 11), par exemple si c'était 2, on aurait le choix entre 3-1-1-2 et 2-1-1-n
mais du coup le contenu de (10, 11) ne suffit pas à trancher, alors que si on avait 99 on ne pourrait pas noircir (11,11) et ça règlerait

TODO à rédiger proprement :)

conclusion (11, 11) est blanche et c'est 99
