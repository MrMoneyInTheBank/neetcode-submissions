func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)

    for idx, num := range nums {
        comp := target - num

        if _, ok := seen[comp]; ok {
            return []int{seen[comp], idx}
        }
        seen[num] = idx;
    }
    return []int{}
}
