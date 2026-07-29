class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        mid = ''
        counts = [0] * 26
        for i in range(26):
            counts[i] = freq[i] // 2
            if freq[i] % 2:
                mid = chr(ord('a') + i)

        half_len = sum(counts)

        # Build total_perms incrementally (O(half_len) total, stays integer)
        total_perms = 1
        L = 0
        for i in range(26):
            for j in range(1, counts[i] + 1):
                L += 1
                total_perms = total_perms * L // j

        if total_perms < k:
            return ""

        result = []
        rem = half_len
        cur_total = total_perms

        for _ in range(half_len):
            for i in range(26):
                if counts[i] == 0:
                    continue
                # arrangements if we place letter i here
                new_total = cur_total * counts[i] // rem
                if k <= new_total:
                    result.append(chr(ord('a') + i))
                    counts[i] -= 1
                    rem -= 1
                    cur_total = new_total
                    break
                else:
                    k -= new_total

        half_str = ''.join(result)
        return half_str + mid + half_str[::-1]