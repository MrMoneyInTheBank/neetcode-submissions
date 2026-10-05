func twoSum(nums []int, target int) []int {
    var seen map[int]int = make(map[int]int)

    for idx, num := range nums {
        var comp int = target - num

        if jdx, ok := seen[comp]; ok {
            return []int{jdx, idx}
        }
        seen[num] = idx
    }

    return []int{}
}
