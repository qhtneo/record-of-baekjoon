# 나무의 수 N, 필요 나무 길이 M
N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
first = 0
end = trees[-1]

while first <= end:
  mid = (first + end) // 2
  # tree_sum = 0
  # for tree in trees:
  #   if tree - mid > 0:
  #     tree_sum += (tree - mid)
  tree_sum = sum(tree - mid for tree in trees if tree > mid)
  if tree_sum < M:
    end = mid - 1
  else:
    first = mid + 1
print(end)
