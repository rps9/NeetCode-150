from test_runner import test

class Solution:
    def isValid(self, s: str) -> bool:    
        stack = []

        counterpart = {
            '}': '{',
            ')': '(', 
            ']': '['
        }

        for item in s:
            if item not in counterpart:
                stack.append(item)
            elif len(stack) == 0:
                return False
            elif stack[-1] !=  counterpart[item]:
                return False
            else:
                stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False


def main():
    test_cases = [
        {"args": ("([{}])",), "expected_result": True},
        {"args": ("([)]",), "expected_result": False},
        {"args": ("",), "expected_result": True},
        {"args": ("({[]})",), "expected_result": True},
        {"args": ("({[}])",), "expected_result": False},
    ]
    
    test(Solution().isValid, test_cases)

if __name__ == "__main__":
    main()
                