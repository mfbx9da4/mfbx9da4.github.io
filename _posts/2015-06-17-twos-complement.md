---
layout: post
title:  "Proof of max integer encoded by two's complement"
date:   2015-05-17 15:30:27
categories: twos-complement binary-encoding integer-encoding geometric-series
permalink: /twos-complement
---

[Two's-complement](https://en.wikipedia.org/wiki/Two's_complement) is the most common binary way of encoding positive and negative integers in computers. In this post I will prove that the maximum integer encoded by $n$ bits using two's complement encoding is:

$$
MaxInt(n)=2n−1 
$$

The two's complement encoding ($TC$), implements the normal binary system except the most significant bit has a negative weight. Here are some examples with 4 bits:

$$
TC([0001]) = −0 \cdot 2^3 + 0 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 = 0 + 0 + 0 + 1 = 1
$$
$$
TC([0101]) = −0 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 = 0 + 4 + 0 + 1 = 5
$$
$$
TC([1011]) = −1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0 = −8 + 0 + 2 + 1 = −5
$$
$$
TC([1111]) = −1 \cdot 2^3 + 1 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0 = −8 + 4 + 2 + 1 = −1
$$
Therefore the maximum integer encodable with 4 bits is 7:

![two's complement]({{ site.url }}/assets/img/twos-complement.png)

Therefore for $n$ bits:
$$
MaxInt(n) = \sum_{i=0}^{n-2} 2^i = (2^0 + 2^1 + ... + 2^{n-3} + 2^{n-2} )
$$

Applying the proof of the geometric series to this particular case:

$$
MaxInt(n) = S(n) = \sum_{i=0}^{n-2} 2^i = 2^0 + 2^1 ... + 2^{n-3} + 2^{n-2}
$$

Adding up each term in the series:

$$
2S(n) = (2^0 + 2^0) + (2^1 + 2^1) ... + (2^{n-3} + 2^{n-3}) + (2^{n-2} + 2^{n-2})
$$

Simplifying:

$$
2S(n) = 2^1 + 2^2 ... + (2 \cdot \frac{2^{n}}{2^3}) + (2 \cdot \frac{2^{n}}{2^2})
$$

$$
2S(n) = 2^1 + 2^2 ... + \frac{2^{n}}{2^2} + \frac{2^{n}}{2^1}
$$

$$
2S(n) = {\color{Blue} {2^1 + 2^2 ... + 2^{n-2}} } + 2^{n-1}
$$

Notice what is in blue is actually $S(n)$ except it is missing the first term, lets call this part in blue $y$:

$$
2S(n) = {\color{Blue} {y} } + 2^{n-1}
$$

$$
{\color{Blue} {y} } = S(n) - 2^0
$$

Substituting in:

$$
2S(n) = {\color{Blue} {S(n) -2^0} } + 2^{n-1}
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



