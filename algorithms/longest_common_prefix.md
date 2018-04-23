I became curious to understand the internals of how string comparison works in python when I was solving the following example algorithm problem:

> Given two strings, return the length of the longest common prefix

## Solution 1: charByChar

My intuition told me that the optimal solution would be to start with one cursor at the beginning of both words and iterate forward until the prefixes no longer match. Something like

<!-- language: lang-python -->

    def charByChar(smaller, bigger):
      assert len(smaller) <= len(bigger)
      for p in range(len(smaller)):
        if smaller[p] != bigger[p]:
          return p
      return len(smaller)

To simplify the code, the function assumes that the length of the first string, `smaller`, is always smaller than or equal to the length of the second string, `bigger`. 

## Solution 2: binarySearch

Another method is to bisect the two strings to create two prefix substrings. If the prefixes are equal, we know that the common prefix point is at least as long as the midpoint. Otherwise the common prefix point is at least no bigger than the midpoint. We can then recurse to find the prefix length. 

Aka binary search.

<!-- language: lang-python -->

    def binarySearch(smaller, bigger):
      assert len(smaller) <= len(bigger)
      lo = 0
      hi = len(smaller)

      # binary search for prefix
      while lo < hi:
        # +1 for even lengths
        mid = ((hi - lo + 1) // 2) + lo

        if smaller[:mid] == bigger[:mid]:
          # prefixes equal
          lo = mid
        else:
          # prefixes not equal
          hi = mid - 1

      return lo


At first I assumed that that `binarySearch` would be slower because string comparison would compare all characters several times rather than just the prefix characters as in `charByChar`.

Surpisingly, the `binarySearch` turned out to be much faster after some preliminary benchmarking. 

**Figure A**

[![lcp_fixed_suffix][1]][1]




Above shows how performance is affected as prefix length is increased. Suffix length remains constant at 50 characters. 

This graph shows to things:

1. As expected, both algorithms perform linearly worse as prefix length increases. 
2. Performance of `charByChar` degrades at a much faster rate.

Why is `binarySearch` so much better? I think it is because

> 
1. The string comparison in `binarySearch` is presumably optimized by the interpreter / CPU behind the scenes. 
2. `charByChar` actually creates new strings for each character accessed and this produces significant overhead. 

To validate this I benchmarked the performance of comparing and slicing a string, labelled `cmp` and `slice` respectively below.

**Figure B**

[![cmp][2]][2]

This graph show two important things:

1. As expected, comparing and slicing increase linearly with length. 
2. The cost of comparing and slicing increase very slowly with length relative to algorithm performance, Figure A. Note both figures go up to strings of length 1 Billion characters. Therefore, the cost of comparing 1 character 1 Billion times is much much greater than comparing 1 Billion characters once. But this still doesn't answer why ...


## Cpython

In an effort to find out how the cpython interpreter optimizes string comparison I generated the byte code for the following function.

<!-- language: lang-python -->

    In [9]: def slice_cmp(a, b): return a[0] == b[0]

    In [10]: dis.dis(slice_cmp)
                0 LOAD_FAST                0 (a)
                2 LOAD_CONST               1 (0)
                4 BINARY_SUBSCR
                6 LOAD_FAST                1 (b)
                8 LOAD_CONST               1 (0)
               10 BINARY_SUBSCR
               12 COMPARE_OP               2 (==)
               14 RETURN_VALUE

I poked around the cpython code and found the following [two](https://github.com/python/cpython/blob/master/Python/pystrcmp.c#L13) [pieces](https://github.com/python/cpython/blob/master/Python/ceval.c#L4686) of code but I'm not sure this is where string comparison occurs.

## The question

> 
  - Where in the cpython does string comparison occur?
  - Is there a CPU optimization? Is there a special a special x86 instruction?
  - Why is comparing a long string so much faster than comparing each of it's characters?

----

## Bonus question: When is charByChar more performant?

If the prefix is sufficiently small in comparison to the length rest of the string, at some point the cost of creating substrings in `charByChar` becomes less than the cost of comparing the substrings in `binarySearch`.

To describe this relationship I delved into runtime analysis.

## Runtime analysis

To simplify the below equations, let's assume that `smaller` and `bigger` are the same size and I will refer to them as `s1` and `s2`.

### charByChar 

    charByChar(s1, s2) = costOfOneChar * prefixLen

Where the 

    costOfOneChar = cmp(1) + slice(s1Len, 1) + slice(s2Len, 1)

Where `cmp(1)` is the cost of comparing two strings of length 1 char.

`slice` is the cost of accessing a char, the equivalent of `charAt(i)`. Python has immutable strings and accessing a char actually creates a new string of length 1. `slice(string_len, slice_len)` is the cost of slicing a string of length `string_len` to a slice of size `slice_len`. 

So

>     
    charByChar(s1, s2) = O((cmp(1) + slice(s1Len, 1)) * prefixLen)

### binarySearch


    binarySearch(s1, s2) = costOfHalfOfEachString * log_2(s1Len)
    
`log_2` is the number of times to divide the strings in half until reaching a string of length 1. Where 

    costOfHalfOfEachString = slice(s1Len, s1Len / 2) + slice(s2Len, s1Len / 2) + cmp(s1Len / 2)

So the big-O of `binarySearch` will grow according to

> 
    binarySearch(s1, s2) = O((slice(s2Len, s1Len) + cmp(s1Len)) * log_2(s1Len))

Based on our previous analysis of the cost of 

If we assume that `costOfHalfOfEachString` is approximately the `costOfComparingOneChar` then we can refer to them both as `x`.

    charByChar(s1, s2) = O(x * prefixLen)
    binarySearch(s1, s2) = O(x * log_2(s1Len))

If we equate them 

    O(charByChar(s1, s2)) = O(binarySearch(s1, s2))
    x * prefixLen = x * log_2(s1Len)
    prefixLen = log_2(s1Len)
    2 ** prefixLen = s1Len

So `O(charByChar(s1, s2)) > O(binarySearch(s1, s2)` when 

> 
    2 ** prefixLen = s1Len

So plugging in the above formula I regenerated tests for Figure A but with strings of total length `2 ** prefixLen` expecting the performance of the two algorithms to be roughly equal.

[![img][3]][3]

However, clearly `charByChar` performs much better. With a bit of trial and error, the performance of the two algorithms are roughly equal when `s1Len = 200 * prefixLen`

[![img][4]][4]

Why is the relationship 200x?


  [1]: https://i.stack.imgur.com/DFBAT.png
  [2]: https://i.stack.imgur.com/lfZ5n.png
  [3]: https://i.stack.imgur.com/4lObA.png
  [4]: https://i.stack.imgur.com/WdxJn.png

