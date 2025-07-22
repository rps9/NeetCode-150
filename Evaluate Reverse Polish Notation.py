from test_runner import test
from typing import List

class Solution:
    def isInt(self, s: str) -> bool:
        try:
            int(s)
            return True 
        except:
            return False 
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.isInt(token):
                stack.append(int(token))
            else:
                arg2 = stack.pop()
                arg1 = stack.pop()
                if token == '+':
                    stack.append(arg1 + arg2)
                elif token == '-':
                    stack.append(arg1 - arg2)
                elif token == '*':
                    stack.append(arg1 * arg2)
                else:
                    stack.append(int(arg1 / arg2))
        
        return stack[0]

def main():
    print("-11".isalnum())
    test_cases = [
        {"args": (["1","2","+","3","*","4","-"],), "expected_result": 5},
        {"args": (["3","4","+","5","6","+","*"],), "expected_result": 77},
        {"args": (["4","13","5","/","+"],), "expected_result": 6},
        {"args": (["4","13","5","/","+"],), "expected_result": 6},
        {"args": (["10","6","9","3","+","-11","*","/","*","17","+","5","+"],), "expected_result": 22},
    ]

    test(Solution().evalRPN, test_cases)

if __name__ == "__main__":
    main()