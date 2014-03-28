
## The good
- Most known language?

## The bad
- The console is not great, more like ipython and repl

### Sorting
    > a = [5,4,3,2,1]
    [ 5, 4, 3, 2, 1 ]
    > a.sort()
    [ 1, 2, 3, 4, 5 ]
    > a = [3,1,5,2,4]
    [ 3, 1, 5, 2, 4 ]
    > a.sort()
    [ 1, 2, 3, 4, 5 ]
    > a = [3,1,5,12,4]
    [ 3, 1, 5, 12, 4 ]
    > a.sort()
    [ 1, 12, 3, 4, 5 ]

### Parsing variables to functions
    > function shouldRaiseAnError () { return false;}
    > shouldRaiseAnError()
    > false
    > shouldRaiseAnError(3,2,5,2,4,5,2,1) 
    > false // at least tell me I'm sending you junk!

## At least throw an error 
    > ({row:1, col:2} == {row:1, col:2})
    > false