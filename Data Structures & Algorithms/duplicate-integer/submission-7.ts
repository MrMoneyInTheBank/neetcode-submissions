class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const seen: Set<number> = new Set<number>();

        for (const num of nums) {
            if (seen.has(num)) {
                return true;
            } else {
                seen.add(num);
            }
        }
        return false;
    }
}
