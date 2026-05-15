class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #inputs: positions, speeds, and a target destination
        #output: number of different car fleets
        #constraints:
        #cars cant pass cars ahead of it
        #
        carDetails = sorted([[p, s] for p, s in zip(position, speed)])
        stack = []
        for p,s in carDetails[::-1]:
            if not stack:
                stack.append([p, s])
            else:
                stack.append([p,s])
                travelTimeFirst = (target - stack[-2][0])/ stack[-2][1]
                travelTimeSecond = (target - stack[-1][0])/ stack[-1][1]

                if travelTimeSecond <= travelTimeFirst:
                    stack.pop()
        return len(stack)


