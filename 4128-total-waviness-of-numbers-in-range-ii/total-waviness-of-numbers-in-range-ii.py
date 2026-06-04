class Solution:
    def wavyDP(self, i, prev_dig, tight, trend, leading_zeros, num):
        if i == len(num):
            return (0, 1)

        if self.cache.get((i, prev_dig, tight, trend, leading_zeros, num)) is not None:
            return self.cache.get((i, prev_dig, tight, trend, leading_zeros, num))

        max_dig = int(num[i]) if tight else 9
        total_score = 0
        valid_suffs = 0
        for dig in range(max_dig + 1):
            is_peak_or_valley = 0
            if leading_zeros == False:
                if trend == "<" and  prev_dig > dig:
                    is_peak_or_valley = 1
                elif trend == ">" and prev_dig < dig:
                    is_peak_or_valley = 1
                if dig > prev_dig:
                    curr_trend = "<"
                elif dig < prev_dig:
                    curr_trend = ">"
                else:
                    curr_trend = "="
            else:
                curr_trend = "="
            score, num_suffs= self.wavyDP(i + 1, dig, tight and dig == int(num[i]), curr_trend, leading_zeros and dig == 0, num)

            total_score += score + (is_peak_or_valley * num_suffs)
            valid_suffs += num_suffs


        self.cache[(i, prev_dig, tight, trend, leading_zeros, num)] = (total_score, valid_suffs)

        return total_score, valid_suffs

    def init_cache(self):
        self.cache = {}


    def totalWaviness(self, num1: int, num2: int) -> int:
        lb, ub = str(num1 - 1), str(num2)

        self.init_cache()
        lb_score, _ = self.wavyDP(0, 0, True, "=", True, lb)
        
        self.init_cache()
        ub_score, _ = self.wavyDP(0, 0, True, "=", True, ub)

        return ub_score - lb_score
        