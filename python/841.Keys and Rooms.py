class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms) == 0: 
            return True
        tag = [0] * len(rooms)
        tag[0] = 1
        return self.dfs(rooms, tag, 0)

    def dfs(self, rooms, tag, pos):
        if sum(tag) == len(rooms):
            return True
        flag = False
        for key in rooms[pos]:
            if tag[key] == 0:
                tag[key] = 1
                flag = flag or self.dfs(rooms, tag, key)
                # tag[key] = 0
        return flag
        

        