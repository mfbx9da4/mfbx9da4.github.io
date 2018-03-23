# bidirectional bfs


class PathFinder(object):
  """docstring for PathFinder"""
  def __init__(self, graph):
    self.graph = graph

  def get_friends(self, node):
    return self.graph[node]

  def find_path(self, user_a_id, user_b_id):
    # two queues
    # if queue1 finds something in queue 2
    # or visa versa => found collision

    seen_from_a = {}
    queue_from_a = [(user_a_id, 0)]
    seen_from_b = {}
    queue_from_b = [(user_b_id, 0)]

    while len(queue_from_a) or len(queue_from_b):

      print('first')
      collision = self.bfs(queue_from_a, seen_from_a, seen_from_b, user_b_id)
      if collision is not None:
        return self.merge_paths(collision, seen_from_a, seen_from_b)

      print('second')
      collision = self.bfs(queue_from_b, seen_from_b, seen_from_a, user_a_id)
      if collision is not None:
        return self.merge_paths(collision, seen_from_a, seen_from_b)

  def merge_paths(self, collision, paths_a, paths_b):
    return collision, paths_a[collision], paths_b[collision]

  def bfs(self, queue, seen, seen_other, dest_id):
    user_id, depth = queue.pop(0)
    friends = self.get_friends(user_id)
    for friend in friends:
      if friend not in seen:
        seen[friend] = (user_id, depth + 1)
        if friend == dest_id or friend == seen_other:
          return dest_id
        queue.append((friend, depth + 1))

graph = {
  0: [2],
  2: [0, 1],
  1: [2]
}
pf = PathFinder(graph)
print(pf.find_path(0, 1))

# graph = {
#   0: [1,2,3],
#   1: [2,3],
#   2: [3,4],
#   3: [4],
#   4: []
# }

# print(find_path())
