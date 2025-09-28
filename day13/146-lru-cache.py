# https://leetcode.com/problems/lru-cache/
# 146-lru-cache


# 1. OrderedDict
# class LRUCache:
#     from collections import OrderedDict

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = OrderedDict()

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.cache.move_to_end(key)
#             return self.cache[key]
#         return -1
# 노두
#     def put(self, key: int, value: int) -> None:
#         self.cache[key] = value
#         self.cache.move_to_end(key)
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)


# 2. Linked List
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key: Node

        # Dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # 내부 helper: 노드 제거
    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # 내부 helper: 노드를 tail 바로 앞에 삽입 (최근 사용됨)
    def _add_to_tail(self, node: Node):
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 기존 노드 제거
            self._remove(self.cache[key])

        # 새 노드 생성 or 업데이트
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_tail(new_node)

        # 용량 초과 처리
        if len(self.cache) > self.capacity:
            # head 다음 노드가 가장 오래된 것
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]


# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)
