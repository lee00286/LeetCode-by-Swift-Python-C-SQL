# Swift Notes

## Table of Contents
- [Array](#array)
- [String](#string)

## Array

### Identify if the Given Element in the Sequence
Returns a Boolean value indicating whether the sequence contains the given element.
```
let cast = ["A", "B", "C", "D"]
print(cast.contains("A"))
// Prints "true"
print(cast.contains("E"))
// Prints "false"
```

## String

### Measure the Length of a String
```
var str = "String Length"
// Length of the characters in the string
var len = str.count

print( "Length of str is \(len)" )
>> Length of str is 13
```

### Filters a Collection of the Same Type Containing
Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.
```
let cast = ["ABCDEF", "UVWXYZ", "MNO", "K"]
let shortNames = cast.filter { $0.count < 5 }
print(shortNames)
>> ["Kim", "Karl"]
```
