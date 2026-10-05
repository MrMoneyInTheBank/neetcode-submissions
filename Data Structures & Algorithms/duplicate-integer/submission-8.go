func hasDuplicate(nums []int) bool {
    var seen map[int]bool = make(map[int]bool)

    for _, num := range nums {
        if _, exists := seen[num]; exists {
            return true
        } else {
            seen[num] = true;
        }
    }
    
    return false
}
