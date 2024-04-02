class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = {}

        def is_safe(node):
            if node in safe_nodes:
                return safe_nodes[node]

            safe_nodes[node] = False
            for neighbor in graph[node]:
                if not is_safe(neighbor):
                    return safe_nodes[node]

            safe_nodes[node] = True
            return safe_nodes[node]

        def find_safe_nodes():
            safe_list = []
            for node_index in range(len(graph)):
                if is_safe(node_index):
                    safe_list.append(node_index)
            return safe_list

        return find_safe_nodes()