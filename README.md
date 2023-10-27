

# 463 project 1: a look into the joining of 2 algorithm
For My project I chose to use a hybrid sort the combined the speeds of merge and quick sort. My goal was to make a sort that on average was faster then the sorts by themselves. My goal was to make a sort algorithm that was able to cover the weakness of its two parts and would try to keep a comparable or faster speed then its two parts.

The big 0 of N for the sorts are as follows
Merge sort 0(n logn)
Quicksort 0(n^2)
Hybrid sort 0(n logn)

The way my sort improves its to base parts is by allowing for it to handle certain conditions better then the sum of its parts.

- For inputting data sizes Quicksort is usually faster then merge for the small end medium sized arrays. This is because quicksort has a smaller constant factor and cache performance. In the hybrid sort when the input data is bellow 10 elements quicksort is used if greater than merge is given priority.

- For stability Merge sort is better off, meaning it keeps the relative order of equal elements. Quicksort is not so stable. In cases where stability is more important merge sort will be chosen to keep order.

- for Adaptability Quick sort is reliant on the choice of its pivot element. In the hybrid sort the algorithm can be designed to choose a pivot off given inputs.  

- for predictability merge sort is a consistent 0(n log n) and wont change, while quick sort can degrade to 0(n^2) in worst case. The hybrid sort will use quicksort in most cases but will switch to merge if given input data is very unbalanced or has a lot of duplicate elements. This keeps performance constant.

- for Data Distribution merge sort is very efficient when dealing with data that is pretty much all ready sorted as it dose not require as much comparisons. The hybrid sort can detect such patters and use merge sort to improve efficiency as necessary.

- for hardware and memory constraints merge sort is more useful for external sorting with data that does not fit in the memory. allowing the hybrid sort can use merge sort for big datasets that exceed the memory available and that allows for the sort to use external storage capabilities.
  
My hybrid sort take strengths of its sister sorts to keep the code running at a constant and sometime faster speed if the right criteria are met.

## Tests and bench marking each test will run 10 times

### Test 1.1 output array has random numbers from 1 to 100000 with 1000 number total
Hybrid Sort - Time: 0.001993 seconds, Memory: 8056 bytes Fastest
Merge Sort - Time: 0.001998 seconds, Memory: 8056 bytes  
Quick Sort - Time: 0.002984 seconds, Memory: 8056 bytes

### test 1.2 output array has random numbers from 1 to 100000 with 1000 number total
Hybrid Sort - Time: 0.001056 seconds, Memory: 8056 bytes fastest
Merge Sort - Time: 0.002012 seconds, Memory: 8056 bytes
Quick Sort - Time: 0.001993 seconds, Memory: 8056 bytes

### test 1.3 output array has random numbers from 1 to 100000 with 1000 number total
Hybrid Sort - Time: 0.000995 seconds, Memory: 8056 bytes fastest
Merge Sort - Time: 0.001098 seconds, Memory: 8056 bytes
Quick Sort - Time: 0.002006 seconds, Memory: 8056 bytes

### test 1.4 output array has random numbers from 1 to 100000 with 1000 number total
Hybrid Sort - Time: 0.001121 seconds, Memory: 8056 bytes fastest
Merge Sort - Time: 0.001991 seconds, Memory: 8056 bytes
Quick Sort - Time: 0.001994 seconds, Memory: 8056 bytes

### test 1.5 output array has random numbers from 1 to 100000 with 1000 number total
Hybrid Sort - Time: 0.002064 seconds, Memory: 8056 bytes  
Merge Sort - Time: 0.002007 seconds, Memory: 8056 bytes
Quick Sort - Time: 0.001991 seconds, Memory: 8056 bytes fastest

### test 1.6 output array has random numbers from 1 to 100000 with 1000 number total
Hybrid Sort - Time: 0.001993 seconds, Memory: 8056 bytes
Merge Sort - Time: 0.000996 seconds, Memory: 8056 bytes fastest  
Quick Sort - Time: 0.002990 seconds, Memory: 8056 bytes

### test 1.7 output array has random numbers from 1 to 100000 with 1000 number total
Hybrid Sort - Time: 0.001016 seconds, Memory: 8056 bytes fastest
Merge Sort - Time: 0.002028 seconds, Memory: 8056 bytes
Quick Sort - Time: 0.002100 seconds, Memory: 8056 bytes

### test 1.8 output array has random numbers from 1 to 100000 with 1000 number total
Hybrid Sort - Time: 0.002058 seconds, Memory: 8056 bytes  
Merge Sort - Time: 0.000998 seconds, Memory: 8056 bytes fastest
Quick Sort - Time: 0.002002 seconds, Memory: 8056 bytes

### test 1.9 output array has random numbers from 1 to 100000 with 1000 number total
Hybrid Sort - Time: 0.002007 seconds, Memory: 8056 bytes  
Merge Sort - Time: 0.000983 seconds, Memory: 8056 bytes fastest 
Quick Sort - Time: 0.000999 seconds, Memory: 8056 bytes

### test 1.10 output array has random numbers from 1 to 100000 with 1000 number total  
Hybrid Sort - Time: 0.001145 seconds, Memory: 8056 bytes fastest
Merge Sort - Time: 0.002062 seconds, Memory: 8056 bytes
Quick Sort - Time: 0.002050 seconds, Memory: 8056 bytes

First 10 test with output array has random numbers from 1 to 100000 with 1000 number total
Hybrid Sort – Won 6 times  
Merge Sort – won 3 times
Quick Sort – won 1 times

### Test 2.1 output array has random numbers from 1 to 10000000 with 10000 number total
Hybrid Sort - Time: 0.020547 seconds, Memory: 80056 bytes
Merge Sort - Time: 0.018920 seconds, Memory: 80056 bytes fastest
Quick Sort - Time: 0.023782 seconds, Memory: 80056 bytes

### Test 2.2 output array has random numbers from 1 to 10000000 with 10000 number total 
Hybrid Sort - Time: 0.017427 seconds, Memory: 80056 bytes fastest
Merge Sort - Time: 0.021480 seconds, Memory: 80056 bytes  
Quick Sort - Time: 0.024606 seconds, Memory: 80056 bytes

### Test 2.3 output array has random numbers from 1 to 10000000 with 10000 number total
Hybrid Sort - Time: 0.019516 seconds, Memory: 80056 bytes fastest
Merge Sort - Time: 0.019835 seconds, Memory: 80056 bytes
Quick Sort - Time: 0.022940 seconds, Memory: 80056 bytes

### Test 2.4 output array has random numbers from 1 to 10000000 with 10000 number total
Hybrid Sort - Time: 0.019481 seconds, Memory: 80056 bytes  
Merge Sort - Time: 0.018942 seconds, Memory: 80056 bytes fastest
Quick Sort - Time: 0.022888 seconds, Memory: 80056 bytes

### Test 2.5 output array has random numbers from 1 to 10000000 with 10000 number total
Hybrid Sort - Time: 0.020244 seconds, Memory: 80056 bytes fastest  
Merge Sort - Time: 0.022854 seconds, Memory: 80056 bytes
Quick Sort - Time: 0.023859 seconds, Memory: 80056 bytes

### Test 2.6 output array has random numbers from 1 to 10000000 with 10000 number total
Hybrid Sort - Time: 0.020406 seconds, Memory: 80056 bytes  
Merge Sort - Time: 0.019901 seconds, Memory: 80056 bytes fastest
Quick Sort - Time: 0.021135 seconds, Memory: 80056 bytes

### Test 2.7 output array has random numbers from 1 to 10000000 with 10000 number total
Hybrid Sort - Time: 0.020024 seconds, Memory: 80056 bytes  
Merge Sort - Time: 0.018093 seconds, Memory: 80056 bytes fastest
Quick Sort - Time: 0.028450 seconds, Memory: 80056 bytes

### Test 2.8 output array has random numbers from 1 to 10000000 with 10000 number total
Hybrid Sort - Time: 0.019843 seconds, Memory: 80056 bytes fastest  
Merge Sort - Time: 0.020165 seconds, Memory: 80056 bytes
Quick Sort - Time: 0.022496 seconds, Memory: 80056 bytes

### Test 2.9 output array has random numbers from 1 to 10000000 with 10000 number total  
Hybrid Sort - Time: 0.020035 seconds, Memory: 80056 bytes  
Merge Sort - Time: 0.020028 seconds, Memory: 80056 bytes fastest
Quick Sort - Time: 0.029084 seconds, Memory: 80056 bytes

### Test 2.10 output array has random numbers from 1 to 10000000 with 10000 number total
Hybrid Sort - Time: 0.026314 seconds, Memory: 80056 bytes  
Merge Sort - Time: 0.024145 seconds, Memory: 80056 bytes fastest
Quick Sort - Time: 0.033018 seconds, Memory: 80056 bytes

second 10 output array has random numbers from 1 to 10000000 with 10000 number total
Hybrid Sort – Won 4  
Merge Sort – Won 6
Quick Sort – Won 0

### Test 3.1 output array has random numbers from 1 to 100 with 1000 number total 
Hybrid Sort - Time: 0.001072 seconds, Memory: 8056 bytes  
Merge Sort - Time: 0.001583 seconds, Memory: 8056 bytes  
Quick Sort - Time: 0.001019 seconds, Memory: 8056 bytes fastest

### Test 3.2 output array has random numbers from 1 to 100 with 1000 number total
Hybrid Sort - Time: 0.001131 seconds, Memory: 8056 bytes  
Merge Sort - Time: 0.001947 seconds, Memory: 8056 bytes
Quick Sort - Time: 0.000000 seconds, Memory: 8056 bytes fastest

### Test 3.3 output array has random numbers from 1 to 100 with 1000 number total  
Hybrid Sort - Time: 0.001007 seconds, Memory: 8056 bytes fastest  
Merge Sort - Time: 0.001581 seconds, Memory: 8056 bytes
Quick Sort - Time: 0.001021 seconds, Memory: 8056 bytes

### Test 3.4 output array has random numbers from 1 to 100 with 1000 number total  
Hybrid Sort - Time: 0.002482 seconds, Memory: 8056 bytes  
Merge Sort - Time: 0.001268 seconds, Memory: 8056 bytes fastest
Quick Sort - Time: 0.002170 seconds, Memory: 8056 bytes

### Test 3.5 output array has random numbers from 1 to 100 with 1000 number total
Hybrid Sort - Time: 0.002104 seconds, Memory: 8056 bytes  
Merge Sort - Time: 0.001001 seconds, Memory: 8056 bytes fastest  
Quick Sort - Time: 0.001032 seconds, Memory: 8056 bytes

### Test 3.6 output array has random numbers from 1 to 100 with 1000 number total
Hybrid Sort - Time: 0.000996 seconds, Memory: 8056 bytes fastest
Merge Sort - Time: 0.001501 seconds, Memory: 8056 bytes  
Quick Sort - Time: 0.001027 seconds, Memory: 8056 bytes

### Test 3.7 output array has random numbers from 1 to 100 with 1000 number total
Hybrid Sort - Time: 0.001000 seconds, Memory: 8056 bytes fastest  
Merge Sort - Time: 0.002064 seconds, Memory: 8056 bytes
Quick Sort - Time: 0.001105 seconds, Memory: 8056 bytes

### Test 3.8 output array has random numbers from 1 to 100 with 1000 number total
Hybrid Sort - Time: 0.000995 seconds, Memory: 8056 bytes  
Merge Sort - Time: 0.001993 seconds, Memory: 8056 bytes
Quick Sort - Time: 0.000000 seconds, Memory: 8056 bytes fastest

### Test 3.9 output array has random numbers from 1 to 100 with 1000 number total
Hybrid Sort - Time: 0.002171 seconds, Memory: 8056 bytes  
Merge Sort - Time: 0.001077 seconds, Memory: 8056 bytes fastest
Quick Sort - Time: 0.001082 seconds, Memory: 8056 bytes

### Test 3.10 output array has random numbers from 1 to 100 with 1000 number total
Hybrid Sort - Time: 0.000996 seconds, Memory: 8056 bytes tie  
Merge Sort - Time: 0.001996 seconds, Memory: 8056 bytes
Quick Sort - Time: 0.000996 seconds, Memory: 8056 bytes tie

Third test output array has random numbers from 1 to 100 with 1000 number total

Hybrid Sort – 1 tie, won 3  
Merge Sort - won 3  
Quick Sort – 1 tie won 3

Total of all test added up  
Hybrid Sort – 1 tie, won 13  
Merge Sort - won 12  
Quick Sort – 1 tie won 4

Test 1 favored none of the search algorithm,
merge liked the large size and the chase for repeat numbers  
quick liked when there were no repeats
hybrid like when there was a little bit of both.

Test 2 favored merge sort by making the data set larger, but making the range larger made duplicates less likely  
This lead to quick sort failing to get any points and an almost tie between merge and hybrid sort

Test 3 favored quick sort by having less data in it, but has a higher chance for repeated numbers do to the smaller range for the numbers
With all sort almost tied for first place, but the hybrid did stand out with 1 more victory and 1 tie.  

When running tests to see if the sorts work all tests passed
