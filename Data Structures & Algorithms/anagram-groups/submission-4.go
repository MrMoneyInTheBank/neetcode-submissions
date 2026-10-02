func groupAnagrams(strs []string) [][]string {
    encode := func(s string) [26]int {
        var res [26]int
        for _, char := range s {
            idx := char - 'a'
            res[idx]++
        }
        return res
    }

    groups := make(map[[26]int][]string)

    for _, word := range strs {
        key := encode(word)
        groups[key] = append(groups[key], word)
    }

    res := make([][]string, 0)

    for _, val := range groups {
        res = append(res, val)
    }

    return res
}
