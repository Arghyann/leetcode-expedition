class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(num: int) -> int:

            if num < 100:
                return 0
            s = str(num)
            n = len(s)

            memo_cnt = [[[-1] * 10 for _ in range(10)] for _ in range(16)]

            memo_sum = [[[-1] * 10 for _ in range(10)] for _ in range(16)]

            from functools import lru_cache

            @lru_cache(None)
            def dfs(
                pos: int, prev: int, curr: int, isLimit: bool, isLeading: bool
            ):

                if pos == n:
                    return 1, 0
                cnt = 0
                waviness = 0
                up = int(s[pos]) if isLimit else 9
                for digit in range(up + 1):
                    newLeading = isLeading and (digit == 0)

                    newPrev = curr

                    newCurr = -1 if newLeading else digit
                    subCnt, subSum = dfs(
                        pos + 1,
                        newPrev,
                        newCurr,
                        isLimit and (digit == up),
                        newLeading,
                    )

                    if not newLeading and prev >= 0 and curr >= 0:

                        if (prev < curr and curr > digit) or (
                            prev > curr and curr < digit
                        ):
                            waviness += subCnt

                    cnt += subCnt
                    waviness += subSum

                return cnt, waviness

            _, totalSum = dfs(0, -1, -1, True, True)
            return totalSum

        return solve(num2) - solve(num1 - 1)