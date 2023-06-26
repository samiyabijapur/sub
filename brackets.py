def brackets(expression):
    stack=[]
    opening_brackets=['(','[','{']
    closing_brackets=[')',']','}']
    bracket_pairs={')':'(',']':'[','}':'{'}

    for char in(expression):
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:                return False
            if bracket_pairs[char]!=stack.pop():
                return False

    return len(stack)==0

a=["(8*7)+(2-9)","[(7-7)]-(8=7"]
for expression in a:
    if brackets(expression):
        print(f"the brackets{expression}are matched")
    else:
        print(f"the brackets{expression}are not matched")
