class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        sort = []

        for i in range(len(position)):
            sort.append([position[i], speed[i]])

        sort = sorted(sort, key=lambda x : x[0], reverse=True)

        for car in sort:
            time = (target - car[0]) / car[1]
            if len(stack) == 0:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)

        return len(stack)


        
            



        

        
