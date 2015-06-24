---
layout: post
title:  "Combinations and permuations"
date:   2015-04-13 19:30:27
categories: permutations combinations maths
permalink: /combinations-and-permuations
---


This post explains the distinction between combinations and permuations and how to calculate them.

- If order **doesn't** matter it is a **combination** e.g. fruit salad of melon, strawberry and bannanas.
- If order **does** matter it is a **permuation** e.g. bike lock code.


### Permuatations

#### Permutations with repition:

- e.g. range of numbers a byte can encode, combination lock possibilities
- `n` things to choose from, `n` choices each time
- `r` number of choices

```
n^r
```

#### Permutations without repition:

- e.g. What order could 16 pool balls be in?
- `n` things to choose from `n` choices the first time and then one less each time
- If we choose `n` times then the number of permutations is

```
!n
```

- e.g. If we only chose `r` pool balls, we must remove some permutations

```
!n / (n - r)!
```

### Combinations

#### Combinations without repition:

- e.g. lotteries
- Calculated by calculating the permuations and reducing it by how many ways the objects could be in order:

```
(!n / (n - r)!) * (1 /r!)
```

#### Combinations with repition:

- e.g. Choose 3 scopes of 5 flavours of ice cream (`n = 5`, `r = 3`)
- Can be abstracted to the permuations probem where
there are `r + (n - 1)` positions and we choose `r` of them to be 1 and the other positions to be 0.

```
(n + r - 1)! / (r!(n - 1)!)
```