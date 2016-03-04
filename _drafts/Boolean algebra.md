#Boolean algebra: mimic bitwise XOR in terms of AND and COMPLEMENT

Here is a question from one of the homeworks on Hardware Software Interface
course on coursera.


```C
    /*
     * bitXor - x^y using only ~ and &
     *   Example: bitXor(4, 5) = 1
     *   Legal ops: ~ &
     *   Max ops: 14
     *   Rating: 1
     */
    int bitXor(int x, int y) {
      return;
    }
```

One way to think about such a problem is convert the bit numbers into the sets
they represent, taking the example of 4 and 5:

    4 => 0100 => {2}
    5 => 0101 => {0,2}

Next lets do the XOR of these two numbers:

      0100
    ^ 0101
    ------
      0001

So our target output is 1, which translates as the subset `{0}`.

We can see that by performing `&` on the subsets `{2}` and `{0,2}` produces
`{2}` however it loses the important bit `{0}`.

  
