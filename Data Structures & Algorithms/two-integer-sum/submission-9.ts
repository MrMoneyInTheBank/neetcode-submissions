class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const seen: Map<number, number> = new Map();

        for (let idx = 0; idx < nums.length; idx++) {
            const comp = target - nums[idx];

            if (seen.has(comp)) {
                return [seen.get(comp), idx];
            }

            seen.set(nums[idx], idx)
        }

        return []
    }
}
