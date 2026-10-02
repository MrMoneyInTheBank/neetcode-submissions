func isAnagram(s string, t string) bool {
    getFreq := func(s string) map[rune]int {
        freq := make(map[rune]int)

        for _, char := range s {
            freq[char]++;
        }

        return freq;
    }

    comp := func(a, b map[rune]int) bool {
        for key, val := range a {
            if v := b[key]; v != val {
                return false
            }
        }
        for key, val := range b {
            if v := a[key]; v != val {
                return false
            }
        }

        return true
        
    }

    return comp(getFreq(s), getFreq(t));
}
