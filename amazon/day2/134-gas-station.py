# https://leetcode.com/problems/gas-station/
# 134-gas-station


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # residual_gas_for_start = [x - y for x, y in zip(gas, cost)] # 인터넷 검색한 방법

        # max_value = max(residual_gas_for_start)
        # max_index = residual_gas_for_start.index(max_value) # 인터넷 검색한 방법
        # print(max_value, max_index)

        # shifted_gas = gas[max_index:] + gas[:max_index] # 인터넷 검색한 방법
        # shifted_cost = cost[max_index:] + cost[:max_index] # 인터넷 검색한 방법

        # print(shifted_gas)
        # print(shifted_cost)

        # tank = 0
        # for i in range(n):
        #     tank += shifted_gas[i]
        #     tank -= shifted_cost[i]

        #     if tank < 0:
        #         return -1
        # return max_index

        # if sum(gas) - sum(cost) < 0:
        # return -1
        total_gas = 0
        tank = 0
        start = 0

        for i in range(n):
            diff = gas[i] - cost[i]

            total_gas += diff
            tank += diff

            if tank < 0:
                start = i + 1
                tank = 0

        return start if total_gas >= 0 else -1
