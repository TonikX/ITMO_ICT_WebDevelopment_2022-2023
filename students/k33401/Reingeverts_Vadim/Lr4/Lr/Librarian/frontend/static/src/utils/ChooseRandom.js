import SeedRandom from "seedrandom";

// ref: https://github.com/justinmahar/random-seed-weighted-chooser/blob/master/src/index.ts
const chooseWeightedIndex = (weights, seed = Math.random(), defaultWeight = 1) => {
    // If the array is falsy, not an array, or empty, return -1.
    if (!weights || !Array.isArray(weights) || weights.length <= 0) {
        return -1;
    }

    // Keep it positive.
    defaultWeight = Math.abs(defaultWeight);

    let cumulative = 0;
    // Add all weights to cumulative, and build an array of each cumulative value.
    // For example, if the weights are [5, 30, 10], this would build an array
    // containing [5, 35, 45], and cumulative=45.
    const ranges = weights.map(
        (weight) =>
            (cumulative +=
                typeof weight === "number" && weight >= 0 ? Math.abs(weight) : defaultWeight)
    );
    // Get our PRNG function using the seed.
    const seededRandFunc = new SeedRandom(seed);
    // Select our value.
    const selectedValue = seededRandFunc() * cumulative;
    // If the selected value is within one of the ranges, that's our choice!
    for (let index = 0; index < ranges.length; index++) {
        if (selectedValue < ranges[index]) {
            return index;
        }
    }

    // If nothing was chosen, all weights were 0 or something went wrong.
    return -1;
};
export default chooseWeightedIndex;
