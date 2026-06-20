class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 30,0 38,1 -> i=0 res = 1
        # 38,1 30,2 36,3 -> i=2 res =1
        # 38,1 36,3 - 40,5 -> i = 4 res = 1 i=3 res =2
        # i = 1 res =4
        desc_stack = []
        res = [0] * len(temperatures)
        print(res)
        for idx, temp in enumerate(temperatures):
            print(temp, idx)
            while desc_stack and desc_stack[-1][0] < temp:
                val,index = desc_stack.pop()
                print(index,idx, val)
                res[index] = idx - index
            desc_stack.append((temp,idx))
        return res

                    


        