class Graph:

    def __init__(self, graph): 
        self.graph = graph 
        self. ROW = len(graph) 

    def BFS(self, s, t, parent): 
        visited =[False]*(self.ROW) 
        queue=[] 
        queue.append(s) 
        visited[s] = True
        while queue: 
            u = queue.pop(0) 
            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 

        return True if visited[t] else False

    def FordFulkerson(self, source, sink): 

        parent = [-1]*(self.ROW) 

        max_flow = 0 

        while self.BFS(source, sink, parent) : 

            path_flow = float("Inf") 
            s = sink 
            while(s != source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 

            max_flow += path_flow 

            v = sink 
            while(v != source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 

        return max_flow 


def read_graph_from_file(file_name):
    with open(file_name, 'r') as file:
        n = int(file.readline())
        graph = []
        for i in range(n):
            line = list(map(int, file.readline().split()))
            graph.append(line)
    return graph


if __name__ == '__main__':
    graph = read_graph_from_file('input.txt')
    g = Graph(graph)
    source = 0
    sink = len(graph)-1
    max_flow = g.FordFulkerson(source, sink)
    print("Максимальний потік:", max_flow)
