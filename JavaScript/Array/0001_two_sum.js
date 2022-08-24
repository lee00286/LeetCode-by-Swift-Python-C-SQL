/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    let i = 0;
    let j = 1;
    while (i < nums.length) {
        while (j > i && j < nums.length) {
            if (nums[i] + nums[j] === target) return [i, j];
            j += 1;
        }
        i += 1;
        j = i + 1;
    }
    return [i, j];
};