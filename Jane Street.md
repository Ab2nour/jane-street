.# Problème original

## Énoncé

The 11-by-11 grid above has been divided into various regions. Shade some of the cells black, then place digits (0-9) into the remaining cells. Shading must be “sparse”: that is, no two shaded cells may share an edge.

Every cell within a region must contain the same digit, arthogonally adjacent cells in different regions must have different digits. (Note that shading cells may break up regions or change which pairs of regions are adjacent. See the example, below.)

Each row has been supplied with a clue. _Every_ number formed by concatenating consecutive groups of unshaded cells within a row must satisfy the clue given for the row. (As in the example.) Numbers must be at least **two digits long** and may not begin with a 0.

The answer to this month’s puzzle is the sum of all the numbers formed in the completed grid. (As in the example.)

## Grille + exemple

![[number-cross-4-updated.png]]

## Grille originale

![[Pasted image 20240714114204.png]]

# Grille annotée 

## Numéros lignes 

![[Pasted image 20240714120403.png]]

## Numéros lignes & colonnes 
![[Pasted image 20240714120821.png]]

# Carrés noirs

## Colonne 2 et 10

![[Pasted image 20240714114316.png]]

Impossible d'en mettre dans la zone rouge, car il faut des nombres d'au moins 2 chiffres.

## Ligne 1 (square)

### Case (1, 9)

![[Pasted image 20240715092850.png]]

Il faudrait un carré à 2 chiffres identiques.
Or les carrés à 2 chiffres sont 16, 25, 36, 49, 64, 81.

Donc cette case ne peut être noire.

![[Pasted image 20240715092948.png]]

### Case (1, 3)

Même raisonnement que (1, 9)

![[Pasted image 20240715093106.png]]

### Carrés de la forme abb

100, 400, 900, 144, 

### Carrés de la forme aab

225, 441, 

## Ligne 2 (1 more than a palindrome)

todo


## Ligne 4 (sum of digits is 7)

### Case (4, 9)

![[Pasted image 20240715092633.png]]

Il faudrait un nombre à 2 chiffres identiques dont la somme vaut 7.
Or $7 / 2 = 3.5$ donc ce n'est pas possible.

Donc cette case ne peut pas être noire.

![[Pasted image 20240715092746.png]]

## Ligne 7 (multiple 37)

### Case (7, 9)

![[Pasted image 20240715092432.png]]

Si cette case est noire, alors on devrait avoir un multiple de 37 de longueur 2 avec 2 fois le même chiffre, or les premiers multiples sont 37, 74, 111.

Donc cette case ne peut être noire.

![[Pasted image 20240715092547.png]]

## Ligne 8 (multiple de 23 palindrome)

Le plus petit palindrome multiple de 23 est 161, de longueur 3. Donc les nombres de la ligne 8 sont de longueur 3 minimum, donc les colonnes 3 et 9 de la ligne 8 sont blanches.

![[Pasted image 20240714180014.png]]
![[Pasted image 20240715092239.png]]

### Case (8, 4)

![[Pasted image 20240715100544.png]]

Ne respecterait pas la structure de palindrome pour le nombre à gauche

Ne peut pas être noire

### Todo 

Utiliser les zones de contact avec le même nombre

(8, 7)
![[Pasted image 20240715100648.png]]




## Ligne 10 (multiple de 88)

![[Pasted image 20240715092315.png]]

### Premiers multiples

88
176
264
352
440
528
616
704
792
880
968

### Case (10, 3)

Le plus petit multiple de 88 est 88, puis le deuxième est 176, de longueur 3.

Si on noircit cette case :
![[Pasted image 20240714180339.png]]

alors il reste 2 cases à gauche, donc il faudrait mettre un multiple de 88 de longueur 2 dedans. Le seul étant 88, et les zones étant connexes, on arrive à une impossibilité.

![[Pasted image 20240714180534.png]]

Cette case ne peut pas être noire.

### Case (10, 9)

Même raisonnement que la case (10, 3).

![[Pasted image 20240714180630.png]]

Cette case ne peut pas être noire.

### Case (10, 4)

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


### Case (10, 7)

Cette case est-elle noire ? 

![[Pasted image 20240714181848.png]]

S'il n'existe aucun multiple de 88 finissant par 3 fois le même nombre, de longueur 5 ou 6, alors cette case ne peut pas être noire.

## Ligne 11 (1 less than a palindrome)

à revoir en fait... je n'ai pas pris en compte si on noircissait (11, 1)
![[Pasted image 20240715094550.png]]

==> en fait si je pense que c'est bon

![[Pasted image 20240715100003.png]]

### Case (11, 3)

![[Pasted image 20240715093214.png]]

Il nous faudrait 1 de moins qu'un palindrome, de longueur 2, avec 2 chiffres égaux... On a une contradiction.

Cette case ne peut être noire.

![[Pasted image 20240715093309.png]]

### Case (11, 4)

![[Pasted image 20240715094206.png]]

Il nous faudrait 1 de moins qu'un palindrome, de longueur 3, avec 3 chiffres égaux, contradiction.

Cette case ne peut être noire.

![[Pasted image 20240715094229.png]]

### Case (11, 5)

Idem que (11, 4)

![[Pasted image 20240715094258.png]]

### Case (11, 6)

Idem que (11, 4)

### Case (11, 8)

![[Pasted image 20240715100225.png]]

Je pense qu'on arrive à une contradiction

Car le nombre à gauche serait de la forme
a aaa abb

Ce qui ne pourrait pas être un "palindrome - 1"

## Maximum de carrés noirs

On ne peut pas avoir plus de 4 carrés noirs dans une ligne, du fait qu'il doit y avoir au moins 2 chiffres d'affilée

 Donc, il y a 4 chiffres max à trouver par ligne

Exemple :
![[Pasted image 20240714115851.png]]

## Idées

- lister toutes les possibilités de motifs de carrés noirs

# Zones définitives

Zones qui auront le même nombre, quoi qu'il arrive (à cause de l'impossibilité de mettre des carrés noirs)

![[Pasted image 20240714115049.png]]

# Palindromes



# Random

vu qu'il y a 4 carrés noirs max il y a 4 chiffres max à trouver par ligne non ?

# Ligne par ligne

## 2 - 1 more than a palindrome

### Exemples

#### Longueur 2

12
23
34
45
56
67
78
89



## 9 - Product of digits ends with 1

Pas de
- 0 car le produit finit par 1
- 2 sinon ça finit par un nombre pair
- 4 (pareil que 2)
- 5 sinon ça finit par 0 ou 5
- 6 (pareil que 2)
- 8 (pareil que 2)

**Possibilités : 1, 3, 7, 9**

### Influence

Dans la zone violette => 1, 3, 7, 9
![[Pasted image 20240714125822.png]]
![[Pasted image 20240714183642.png]]

## 11 - 1 less than a palindrome

### Exemples

#### Longueur 2

10
21
32
43
54
65
76
87
98

#### Longueur 3

Palindromes 111, 121, ...
- 110
- 120
- 130
- ...
- 190

Palindromes 
0 4 5 6 7 10

donc
1 5 6 7 8 11

donc
2 3 4 9 10

# Cases forcément blanches

D'après le solver d'Antoine

![[Pasted image 20240714134406.png]]

possibilités noires ligne 8 : 0 4 7 10 => 1 5 8 11
donc cases blanches : 2 3 4 6 7 9 10

- soit ça : (cases noires : 1 / 5 / 11)
161 989
13731 37973
![[Pasted image 20240714135032.png]]



- soit la case 7:
autres possibilités (voir solver)
