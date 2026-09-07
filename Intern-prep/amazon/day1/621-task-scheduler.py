# Idea:
# hash set?
## https://leetcode.com/problems/task-scheduler/description/
# 621-task-scheduler


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # task_counter = Counter(tasks)
        # need_interval = defaultdict(int)
        # remaining = len(tasks)
        # count = 0

        # while remaining > 0:
        #     Flag = False
        #     target = None

        #     for task, val in task_counter.most_common():
        #         if task_counter[task] == 0: # only schedule remaining task
        #             continue
        #         elif need_interval[task] > 0: # do not schedule task that need interval
        #             continue
        #         else: #
        #             need_interval[task] = n
        #             task_counter[task] -= 1
        #             target = task
        #             remaining -= 1
        #             Flag = True
        #             # print(task)
        #             break

        #     for task in need_interval:
        #         if need_interval[task] > 0 and task != target:
        #             need_interval[task] -= 1
        #     # if not Flag:
        #         # print("idle")
        #     count += 1
        # return count

        # Optimized
        count = Counter(tasks)
        max_freq = max(count.values())
        max_count = sum(1 for val in count.values() if val == max_freq)
        return max((max_freq - 1) * (n + 1) + max_count, len(tasks))
