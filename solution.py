class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = len(isConnected)
        visited_cities = set()

        for i, city in enumerate(isConnected):
            if i not in visited_cities:
                connections = self.giveConnections(isConnected, i)
                print(i, connections)
                visited_cities.update(connections)
                provinces -= len(connections) - 1

        return provinces

    def giveConnections(self, isConnected, index):
        connections = {index}
        stack = [index]

        while stack:
            city = stack.pop()
            for i, connection in enumerate(isConnected[city]):
                if i not in connections and connection == 1:
                    connections.add(i)
                    stack.append(i)
        
        return connections


