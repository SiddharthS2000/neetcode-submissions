class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     self.min_dist_heap = list()
    #     self.dist_map = defaultdict(list)
    #     res = []
    #     for i in range(k):
    #         dist = self.dist(points[i])
    #         heapq.heappush(self.min_dist_heap, dist)
    #         self.dist_map[dist].append(points[i])

    #     for dist in self.min_dist_heap:
    #         for point in self.dist_map[dist]:
    #             res.append(point)
    #     return res

    # def dist(self, point):
    #     return point[0]**2 + point[1]**2

        points.sort(key=lambda k: k[0]**2 + k[1]**2)
        return points[:k]