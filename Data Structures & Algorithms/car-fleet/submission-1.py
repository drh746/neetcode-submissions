class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda c: c[0], reverse=True)
        desc_stack = []
        # [(7,1), (4,2), (1,2), (0,1)] [3, 3 ]
        for pos, spd in cars:
            time = (target - pos) / spd
            if desc_stack and desc_stack[-1] >= time:
                continue
            else:
                desc_stack.append(time)
        return len(desc_stack)
