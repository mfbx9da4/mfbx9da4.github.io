---
layout: post
title:  "Proof of max integer encoded by two's complement"
date:   2015-05-17 15:30:27
categories: twos-complement binary-encoding integer-encoding geometric-series
permalink: /twos-complement
---

[Two's-complement](https://en.wikipedia.org/wiki/Two's_complement) is the most common binary way of encoding positive and negative integers in computers. In this post I will prove that the maximum integer encoded by $n$ bits using two's complement encoding is:

$$
MaxInt(n)=2^{n-1}−1 
$$

The two's complement encoding ($TC$), implements the [normal binary system](https://en.wikipedia.org/wiki/Binary_number#/media/File:Binary_counter.gif) except the most significant bit has a negative weight. Here are some examples with 4 bits:

$$
TC([{\color{#CC0000} {0001} }]) = −{\color{#CC0000} {0} } \cdot 2^3 + {\color{#CC0000} {0} } \cdot 2^2 + {\color{#CC0000} {0} } \cdot 2^1 + {\color{#CC0000} {1} } \cdot 2^0 = 0 + 0 + 0 + 1 = 1
$$
$$
TC([{\color{#CC0000} {0101} }]) = −{\color{#CC0000} {0} } \cdot 2^3 + {\color{#CC0000} {1} } \cdot 2^2 + {\color{#CC0000} {0} } \cdot 2^1 + {\color{#CC0000} {1} } \cdot 2^0 = 0 + 4 + 0 + 1 = 5
$$
$$
TC([{\color{#CC0000} {1011} }]) = −{\color{#CC0000} {1} } \cdot 2^3 + {\color{#CC0000} {0} } \cdot 2^2 + {\color{#CC0000} {1} } \cdot 2^1 + {\color{#CC0000} {1} } \cdot 2^0 = −8 + 0 + 2 + 1 = −5
$$
$$
TC([{\color{#CC0000} {1111} }]) = −{\color{#CC0000} {1} } \cdot 2^3 + {\color{#CC0000} {1} } \cdot 2^2 + {\color{#CC0000} {1} } \cdot 2^1 + {\color{#CC0000} {1} } \cdot 2^0 = −8 + 4 + 2 + 1 = −1
$$


Therefore the maximum integer encodable with 4 bits is 7:

![two's complement]({{ site.url }}/assets/img/twos-complement.png)

Therefore for $n$ bits, the largest number encodable $MaxInt(n)$ is the sum of the base 2 bits excluding the left most bit:

$$
MaxInt(n) = \sum_{i=0}^{n-2} 2^i = (2^0 + 2^1 + ... + 2^{n-3} + 2^{n-2} )
$$

For brevity, let us refer to the $MaxInt(n)$ sum as $S(n)$ for now: 

$$
S(n) = MaxInt(n)
$$

Applying the proof of the geometric series to this particular case, lets double the geometric series and add  up each term in the series for $2S(n)$:

$$
2S(n) = (2^0 + 2^0) + (2^1 + 2^1) ... + (2^{n-3} + 2^{n-3}) + (2^{n-2} + 2^{n-2})
$$

Simplifying:

$$
2S(n) = 2^1 + 2^2 ... + (2 \cdot 2^{n-3}) + (2 \cdot 2^{n-2})
$$

$$
= 2^1 + 2^2 ... + (2 \cdot \frac{2^{n}}{2^3}) + (2 \cdot \frac{2^{n}}{2^2})
$$

$$
 = 2^1 + 2^2 ... + \frac{2^{n}}{2^2} + \frac{2^{n}}{2^1}
$$

$$
 = 2^1 + 2^2 ... + \frac{2^{n}}{2^2} + \frac{2^{n}}{2^1}
$$

$$
 = {\color{#CC0000} {2^1 + 2^2 ... + 2^{n-2}} } + 2^{n-1}
$$

Notice what is in <span style="color: #CC0000">red</span> is actually $S(n)$ except it is missing the first term ($2^0$), lets call this part in <span style="color: #CC0000">red</span> $y$:

$$
2S(n) = {\color{#CC0000} {y} } + 2^{n-1}
$$

where 

$$
{\color{#CC0000} {y} } = S(n) - 2^0
$$

Substituting in:

$$
2S(n) = {\color{#CC0000} {S(n) -2^0} } + 2^{n-1}
$$

$$
S(n) = 2^{n-1} - 2^0
$$

$$
= 2^{n-1} - 1
$$

$$
\therefore MaxInt(n) = \sum_{i=0}^{n-2} 2^i = 2^{n-1} - 1
$$

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>
<script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>



