class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for today in range(n):
            while stack and temperatures[today] > temperatures[stack[-1]]:
                prev_day = stack.pop() 
                answer[prev_day] = today - prev_day
            stack.append(today)
            
        return answer