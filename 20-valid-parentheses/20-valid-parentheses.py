class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        # for c in s:
        #     if c =='(' or c=='[' or c=='{':
        #         print(c)
        #         print("appended",stack.append(c))
        #         print(stack)
        #     elif c==')':
        #         if stack and stack[-1] == '(':
        #             print("popped:",stack.pop())
        #         else:
        #             print(stack.append(c))
        #     elif c==']':
        #         if stack and stack[-1] == '[':
        #             print(stack.pop())
        #         else:
        #             print(stack.append(c))
        #     elif c == '}':
        #         if stack and stack[-1] == '{':
        #             print(stack.pop())
        #         else:
        #            print(stack.append(c))
        # return len(stack)==0
        pairs = {
            ')': '(',
            '}':'{',
            ']':'[',
        }
        
        for c in s:
            if c in pairs: # c is an closing parenthisis
                if stack and stack[-1] == pairs[c]: # a matching brackets exists at top of the stack
                    stack.pop()
                else:
                    return False
            else: # c is an opening parenthesis, push onto the stack
                stack.append(c)
        return False if stack else True
    
                
                