# Leetcode Tasks


### 1.

![](https://i.imgur.com/NP6gi3W.png)

```js
/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
const kidsWithCandies = (candies, extraCandies) => {
    const max = Math.max(...candies)
    const maxIndex = candies.indexOf(max)
    return candies.map((candy, index) =>
        (candy + extraCandies >= max) || index === maxIndex
    )
};
```

### 2.

![](https://i.imgur.com/xayYyRV.png)


```js
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
const licenseKeyFormatting = (s, k) => {
    const dashlessKey = s.replaceAll('-', '').toUpperCase()
    const groupCount = Math.floor(dashlessKey.length / k)
    const remainder = dashlessKey.length % k
    let key = dashlessKey.slice(0, remainder)
    
    let currPos = remainder
    for (let i = 0; i < groupCount; i++) {
        endPos = currPos + k
        key += "-" + dashlessKey.slice(currPos, endPos)

        currPos = endPos
    }
    return key[0] === "-" ? key.replace('-', '') : key
};
```

### 3.

![](https://i.imgur.com/aVlCPbH.png)


```js
/**
 * @param {number[][]} matrix
 * @return {boolean}
 */
const isToeplitzMatrix = (matrix) => {
    return matrix.every((curr_row, curr_row_index) => {
        return matrix.every((row, row_index) => {
            if (curr_row_index >= row_index) return true
        
            return row.every((number, number_index) => {
                if (number_index < row_index - curr_row_index) return true
                
                const curr_number = curr_row[number_index - row_index + curr_row_index]
                if (typeof curr_number !== undefined) return number === curr_number

                return true
            })
        })
    })
};
```

### 4.

![](https://i.imgur.com/GFHGYbs.png)


```js
/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
const countOdds = (low, high) => {
    const isLowOdd = low % 2 === 1
    const isHighOdd = high % 2 === 1
    const totalCount = high - low + 1
    let oddCount = Math.floor(totalCount / 2)

    if (isLowOdd && isHighOdd) oddCount++
    return oddCount
}
```

### 5.

![](https://i.imgur.com/MD06KLu.png)


```js
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isSubsequence = (s, t) => {
    let currLetterIndex = 0;
    for (let letter of t) {
        if (letter === s[currLetterIndex]) {
            currLetterIndex++
        }
    }
    return currLetterIndex === s.length
}
```

### 6.

![]()


```js
```

### 7.

![]()


```js
```

### 8.

![]()


```js
```