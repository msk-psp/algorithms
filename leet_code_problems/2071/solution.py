from typing import List
from collections import deque

class Solution:
    def check(self, k, tasks, workers, strength, pills):
        if k == 0:
            return True
    
        if k > len(workers):
            return False
        _workers = workers.copy()
        worker_queue = deque(_workers)
        pills_left = pills

        for index in range(k - 1, -1, -1):
            task = tasks[index]

            if len(worker_queue) == 0:
                return False

            if worker_queue[-1] >= task:
                worker_queue.pop()
            elif pills_left > 0 and len(worker_queue) > 0:
                found = False

                for j in range(len(worker_queue)):
                    if worker_queue[j] + strength >= task:
                        worker_queue.remove(worker_queue[j])
                        pills_left -= 1
                        found = True
                        break
                if not found:
                    return False

            else:
                return False
        return True
        
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks = sorted(tasks)
        workers = sorted(workers)

        n = len(tasks)
        m = len(workers)

        low = 0
        high = min(n, m)

        while low <= high:
            k = (low + high) // 2

            if k == 0:
                possible = True
            else:
                possible = self.check(k, tasks, workers, strength, pills)

            if possible:
                ans = k
                low = k + 1
            else:
                high = k - 1

        return ans

if __name__ == "__main__":
    s = Solution()
    # Example usage
    tasks = [3, 5, 2]
    workers = [8, 6, 4]
    pills = 1
    strength = 5
    print(s.maxTaskAssign(tasks, workers, pills, strength))  # Output: 3

    # Example usage
    tasks = [5,4]
    workers = [0, 0, 0]
    pills = 1
    strength = 5
    print(s.maxTaskAssign(tasks, workers, pills, strength))  # Output: 1

    # Example usage
    tasks = [10,15,30]
    workers = [0,10,10,10,10]
    pills = 3
    strength = 10
    print(s.maxTaskAssign(tasks, workers, pills, strength))  # Output: 2

    tasks = [5,9,8,5,9]
    workers = [1,6,4,2,6]
    pills = 1
    strength = 5
    print(s.maxTaskAssign(tasks, workers, pills, strength))    # Output: 3

    tasks = [5181,2717,7678,7730,5931,8066,2266,5873,3645,6636,3308,2848,2082,7158,5398,4030,4942,1723,6614,5165,8086,7526,9503,2051,5305,6606,7514,5078,1149,5782,4717,5969,4966,1292,4370,3863,4111,1140,2980,5295,5347,8700,2833,6750,2352,7604,6305,2697,7501,7719,7955,7901,1779,6850,6456,1040,9230,2712,8129,9875,9385,1814,8167,2960,9191,3588,7339,2255,5314,2873,3294,5375,6745,5984,9717,4983,2558,8075,7988,6490,4499,7236,2097,8097,2923,2972,8609,8993,6354,6502,3340,1666,1281,9703,8869,5274,8150,5270,3437,3171,7423,5865,1995,7002,8550,9908,7114,8777,1250,5855,3501,9316,5380,3877]

    workers = [2167,4646,1582,1102,2113,1258,4341,3193,3136,4096,3311,1501,3499,1815,1282,4914,772,4785,2632,1223,3479,3010,3505,1613,4257,1192,2918,2664,4274,4036,1039,1250,4713,3443,4514,4117,3400,3825,1782,3552,2386,865,2290,3618,793,1297,908,2187,3273,4531,3859,605,4274,3951,583,1135,2802,3585,727,2359,4011,4071,2035,4775,764,4702,2050,3304,3876,3772,4946,4371,1993,4746,1124,1221,1368,831,2337,506,951,3874,3094,2744,4258,4704,3229,1015,4876,1893,3098,4464,4189,4201,3986,3673,4126,2424,4280,2780,1748,1650,1591,753,3392,2498,835,608,1746,1243,3778,1382,4207,1909,832,4501,781,1274,973,4966,1873,2512,3644,3244,1120,4979,3945,1481,2172,4410,3572,4597,3414,4306,4714,4047,3239,4557,3226,3273,4997,3374]

    pills = 139

    strength = 2075

    print(s.maxTaskAssign(tasks, workers, pills, strength))    # Output: 77



        