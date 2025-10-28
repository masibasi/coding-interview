# https://leetcode.com/problems/insert-delete-getrandom-o1/
# 380-insert-delete-getrandom-01

class RandomizedSet:

    def __init__(self):
        self.val_to_index = {} 
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        else:
            self.val_to_index[val] = len(self.values)
            self.values.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.values:
            del_index = self.val_to_index[val]
            last_value = self.values[-1]

            self.values[del_index] = last_value
            self.val_to_index[last_value] = del_index

            self.values.pop()
            del self.val_to_index[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()



class RandomizedSet:

    def __init__(self):
        self.rset = set()

    def insert(self, val: int) -> bool:
        if val in self.rset:
            return False
        else:
            self.rset.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.rset:
            self.rset.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        rand = int(random.random() * len(self.rset))
        print(rand)
        if self.rset:
            return list(self.rset)[rand]
        else:
            return None


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()