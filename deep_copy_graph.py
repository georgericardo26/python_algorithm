"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a node in a connected directional graph, create a copy of it.

"""
class Node:
  def __init__(self, value, adj=None):
    self.value = value
    self.adj = adj

    # Variable to help print graph
    self._print_visited = set()
    if self.adj is None:
      self.adj = []

  # Able to print graph
  def __repr__(self):
    return f"{self.value}"
    # if self in self._print_visited:
    #   return ''
    # else:
    #   self._print_visited.add(self)
    #   final_str = ''
    #   for n in self.adj:
    #     final_str += f'{n}\n'
    #
    #   self._print_visited.remove(self)
    #   return final_str + f'({self.value}, ({[n.value for n in self.adj]}))'


def deep_copy_graph(node, visited):
  # position = node.value - 1

  if node.value in visited:
    return node

  # visited[position] = node
  visited[node.value] = Node(node.value)

  if node.adj is None:
    return node

  for n in node.adj:
    visited[node.value].adj.append(deep_copy_graph(n, visited))

  return visited

n5 = Node(5)
n4 = Node(4)
n3 = Node(3, [n4])
n2 = Node(2)
n1 = Node(1, [n5])
n5.adj = [n3]
n4.adj = [n3, n2]
n2.adj = [n4]
visited = {}
graph_copy = deep_copy_graph(n1, visited)
print(graph_copy)
# (2, ([4]))
# (4, ([3, 2]))
# (3, ([4]))
# (5, ([3]))
# (1, ([5]))