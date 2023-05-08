class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [(temperatures[0],0)]
        resultArr = [0] * len(temperatures)

        for i in range(1,len(temperatures)):
                
            if(stack[-1][0] < temperatures[i]):
                while(len(stack) > 0 and stack[-1][0] < temperatures[i]):
                    elementIndex = stack.pop(-1)[1]
                    resultArr[elementIndex] = (i - elementIndex)

            stack.append((temperatures[i],i))            
            
        return resultArr
