- [number-cross-4-updated.PNG (1782×2024) (janestreet.com)]([https://www.janestreet.com/puzzles/number-cross-4-updated.PNG](https://www.janestreet.com/puzzles/number-cross-4-updated.PNG))

- [Number Cross 4 :: Jane Street]([https://www.janestreet.com/puzzles/number-cross-4-index/](https://www.janestreet.com/puzzles/number-cross-4-index/))

  

# Reasoning

  

Grid size is $11 \times 11 = 121$ 

Without taking the rules into account, each cell can be either in $[[0, 9]]$ or shaded, so $11$ possibilities per cell

Number of possibilities: $11^{121}$ => impossible to try exhaustively

  

# Train of thought

  

1) Can it be solved without an algorithm?

2) Looks like we need an algorithm, maybe some graph traversal

3) Graph because there are adjacent zones, we do not have to test so many possibilities, only testing for areas

4) The shaded cells are so difficult: we do not know their number and their position AND they can even create new regions...

6) Starting mathematically to see if we can see obvious things

7) I made a list with all rows, all columns, to try to deduce things, eliminate number possibilities

# Elimination

  

# Rows

## 1 square

  

## 2 one more than  a palindrome

  

- 1st number is some $n$ and last number is some $n+1$

- so 1st number is at most 8 and last number is at least 2

- 

  

## 3

  

## 4 sum of digits is seven

  

- there should be 0 in this row

  

## 5

  

## 6

  

## 7

  

## 8

  

## 9

  

cannot have

- 0 because product ends in 1

- 2 because it would end with an even number (0, 2, 4, 6, 8)

- 4 for the same reason than 2

- 5 because it would end with either 0 or 5

- 6 for the same reason than 2

- 8 for the same reason than 2

- possibilities: 1, 3, 7, 9

  

## 10

  

$88 = 2^3 \times 11$

## 11

  

  

# Columns

  

  

## 1

  

- cannot have leading 0 (according to rules)

- 

  

## 2

  

## 3

  

## 4

  

## 5

  

## 6

  

## 7

  

## 8

  

## 9

  

## 10

  

## 11

  

  

  

  

  

# Black boxes

## 1 square

  

## 2 one more than  a palindrome

  

## 3

  

## 4

  

## 5

  

## 6

  

## 7

  

## 8

  

## 9

  

black boxes could have an influence only on those 2 cases (because it would create another zones => there would be more number in the product)

  

![[Pasted image 20240523151833.png]]

  

4 cases

- $J \times K \times L \times E$ ends with 1 or,

- $J \times K_1 \times K_2 \times L \times E$ ends with 1 or,

- $J \times K \times L \times E_1 \times E_2$ ends with 1 or,

- $J \times K_1 \times K_2 \times L \times E_1 \times E_2$ ends with 1.

  

Reminder: possibilities are 1, 3, 7, 9

## 10

  

## 11

  

  

# Graph

  

- E must be separated in sub-nodes because it has 11 neighbors, and you can have at most 9 neighbors

  

# Solution

  

- ancien problème résolu avec le solver Z3 [Jane-Street-Solutions/2016_07_NumberCross3.ipynb at master · gowen100/Jane-Street-Solutions · GitHub]([https://github.com/gowen100/Jane-Street-Solutions/blob/master/2016_07_NumberCross3.ipynb](https://github.com/gowen100/Jane-Street-Solutions/blob/master/2016_07_NumberCross3.ipynb)