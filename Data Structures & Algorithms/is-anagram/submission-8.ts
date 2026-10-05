class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        const freq_array = (s: string) => {
            const freq: Array<number> = new Array(26).fill(0);

            const a_code = "a".charCodeAt(0);

            for (const char of s) {
                const idx = char.charCodeAt(0) - a_code;
                freq[idx]++;
            }

            return freq;
        }

        const s_freq: Array<number> = freq_array(s);
        const t_freq: Array<number> = freq_array(t);
        return s_freq.every((count, idx) => t_freq[idx] == count);
    }
}
