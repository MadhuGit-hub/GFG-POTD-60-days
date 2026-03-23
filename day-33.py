class Solution:
    def longestCycle(self, V, edges):
        # Step 1: Build outgoing edge array
        out = [-1] * V
        for u, v in edges:
            out[u] = v

        visited = [False] * V
        max_cycle = -1

        for i in range(V):
            if visited[i]:
                continue

            curr = i
            time_map = {}
            step = 0

            while curr != -1 and not visited[curr]:
                visited[curr] = True
                time_map[curr] = step
                step += 1
                curr = out[curr]

                if curr in time_map:
                    cycle_len = step - time_map[curr]
                    max_cycle = max(max_cycle, cycle_len)
                    break

        return max_cycle