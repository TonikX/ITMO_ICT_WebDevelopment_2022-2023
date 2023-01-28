# Leetcode Tasks


### 1.

![](https://i.imgur.com/vsXEVVS.png)

```js
/**
 * @param {number} num
 * @return {boolean}
 */
const checkPerfectNumber = (num) => {
    const divisors = []
    for (let i = num - 1; i > 0; i--) {
        const isDivisor = num % i === 0
        if (isDivisor) divisors.push(i)
    }
    const devisiorsSum = divisors.reduce((a, b) => a + b, 0)
    return devisiorsSum === num
};
```


### 2.

![](https://i.imgur.com/DhdHO0U.png)

```js
/**
 * @param {string[]} word1
 * @param {string[]} word2
 * @return {boolean}
 */
const arrayStringsAreEqual = (word1, word2) => {
    const str1 = word1.join("")
    const str2 = word2.join("")
    return str1 === str2
};
```

### 3.

![](https://i.imgur.com/Fka3R61.png)

```js
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
const largestSumAfterKNegations = (nums, k) => {
    for (let i = 0; i < k; i++) {
        smallest = Math.min(...nums)
        smallest_index = nums.findIndex(num => num === smallest)
        nums[smallest_index] *= -1
    }
    return nums.reduce((a, b) => a + b, 0);
};
```

### 4.

![](https://i.imgur.com/6kzrRDD.png)

```js
/**
 * @param {number[]} nums
 * @return {number[]}
 */
const frequencySort = (nums) => {
    nums_grouped = []

    nums.forEach(target => {
        if (!nums_grouped.flat(1).includes(target)) {
            targetCount = nums.reduce((a, v) => (v === target ? a + 1 : a), 0)
            nums_grouped.push(Array(targetCount).fill(target))

        }
    })

    nums_grouped.sort((a, b) => a.length - b.length || b[0] - a[0])
    return nums_grouped.flat(1)
};
```

### 5.

![](https://i.imgur.com/KYdtK74.png)

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
const minimumOperations = (nums) => {
    let operations = 0
    while (nums.reduce((a, b) => a + b, 0) !== 0) {
        smallest = Math.min(...nums.filter(num => num > 0))
        nums = nums.map(num => num > 0 ? num - smallest : num)
        operations++
    }
    return operations
};
```

### 6.

![](https://i.imgur.com/gJFuZpK.png)

```js
/**
 * @param {string} sequence
 * @param {string} word
 * @return {number}
 */
const maxRepeating = (sequence, word) => {
    return sequence.split(word).length - 1
};
```

### 7.

![](https://i.imgur.com/rYVdj4r.png)

```js
/**
 * @param {number[]} timeSeries
 * @param {number} duration
 * @return {number}
 */
const findPoisonedDuration = (timeSeries, duration) => {
    totalDurationSet = new Set()
    timeSeries.forEach(time => {
        for (let i = 0; i < duration; i++) {
            totalDurationSet.add(time + i)
        }
    })
    return totalDurationSet.size
};
```

### 8.

![](https://i.imgur.com/wAzP8hA.png)

```js
/**
 * @param {number} n
 * @return {number}
 */
alternateDigitSum = (n) => {
    let isPositive = false
    digits = [...n.toString()].map(letter => {
        isPositive = !isPositive
        if (isPositive) {
            return Number("+" + letter)
        } else {
            return Number("-" + letter)
        }
    })
    return digits.reduce((a, b) => a + b, 0);
};

```

