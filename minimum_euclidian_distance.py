# import numpy as np
# from scipy import spatial
#
# xy1 = np.array(
#     [[243,  3173],
#      [525,  2997]])
#
# xy2 = np.array(
#     [[682, 2644],
#      [277, 2651],
#      [396, 2640]])
#
# # This solution is optimal when xy2 is very large
# tree = spatial.cKDTree(xy2)
# mindist, minid = tree.query(xy1)
# print(mindist)
#
# # This solution by @denis is OK for small xy2
# mindist = np.min(spatial.distance.cdist(xy1, xy2), axis=1)
# print(mindist)
#
# from scipy.spatial import distance

# A = [(1,1),(2,1),(3,1)]
# B = [(2,2),(3,3)]
#
# min_dist = []
# for a in A:
#     dist = []
#     # for b in B:
#     #     dist.append(distance.euclidean(a,b))
#     min_dist.append(min(dist))

# >> min_dist
# >> [1.4142135623730951, 1.0, 1.4142135623730951]
# def closestPointPair(pairs):
#     minDist = infinity
#     for i = 1 to length(P) - 1 do
#     for j = i + 1 to length(P) do
#     let
#     p = P[i], q = P[j]
#     if dist(p, q) < minDist  then
#     minDist = dist(p, q)
#     closestPair = (p, q)
#
#
# return closestPair

# min_dist = sys.maxsize
#
# for i in range(len(pairs)):
#     for j in range(i+1, len(pairs)):
#         dist = calc_euclidean_dist(pairs[i], pairs[j])
#         if dist < min_dist:
#             min_dist = dist
#
# return min_dist


import math
import sys

v1 = [1.2, 2, 3.8, 4.5]
v2 = [0.5, 4.5, 9.6, 3.4]


def dist_euclidiana(v1, v2):
    dim, soma = len(v1), 0
    for i in range(dim):
        soma += math.pow(v1[i] - v2[i], 2)
    return math.sqrt(soma)


def closestPointPair(p):
    min_dist = sys.maxsize
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            dist = dist_euclidiana(p[i], p[j])
            if dist < min_dist:
                min_dist = dist


# print('%.2f' % dist_euclidiana(v1, v2))
print(closestPointPair([[1.2, 2], [3.8, 4.5], [9.6, 3.4]]))
# distância euclidiana com numpy

# import numpy as np
# ''
# def dist_euclidiana_np(v1, v2):
# 	v1, v2 = np.array(v1), np.array(v2)
# 	diff = v1 - v2
# 	quad_dist = np.dot(diff, diff)
# 	return math.sqrt(quad_dist)
#
# print('%.2f' % dist_euclidiana_np(v1, v2))
