#   https://leetcode.com/problems/fruit-into-baskets/
# 904-Fruit-Into-Baskets
# two baskets
# sliding window??


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        counter = defaultdict(int)
        type_of_fruit = set()
        max_fruits = 0
        cur_fruits = 0

        for r, fruit in enumerate(fruits):
            # ADD NEXT FRUIT
            type_of_fruit.add(fruit)
            counter[fruit] += 1
            cur_fruits += 1

            # if basket is full
            if len(type_of_fruit) > 2:
                while True:
                    r_fruit = fruits[l]
                    counter[r_fruit] -= 1  # get rid of left fruit
                    cur_fruits -= 1
                    l += 1
                    if counter[r_fruit] == 0:
                        type_of_fruit.remove(r_fruit)
                        break

            # if not full
            else:
                max_fruits = max(max_fruits, cur_fruits)

        return max_fruits
