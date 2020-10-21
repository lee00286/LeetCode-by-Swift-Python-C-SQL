class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if (a == '0' or a == ''):
            return b
        if (b == '0' or b == ''):
            return a
        
        add = ''
        carry = '0'
        
        for i in range(1, max(len(a), len(b)) + 1):
            if (i > len(b)):
                if (carry == '1'):
                    # 1 + 1
                    if (a[-i] == '1'):
                        add = '0' + add
                    # 0 + 1
                    else:
                        add = '1' + add
                        carry = '0'
                else:
                    # 1 + 0
                    if (a[-i] == '1'):
                        add = '1' + add
                    # 0 + 0
                    else:
                        add = '0' + add
                    carry = '0'
            elif (i > len(a)):
                if (carry == '1'):
                    # 1 + 1
                    if (b[-i] == '1'):
                        add = '0' + add
                    # 0 + 1
                    else:
                        add = '1' + add
                        carry = '0'
                else:
                    # 1 + 0
                    if (b[-i] == '1'):
                        add = '1' + add
                    # 0 + 0
                    else:
                        add = '0' + add
                    carry = '0'
            else:
                # 1 + 1 + 1
                if (a[-i] == '1' and b[-i] == '1' and carry == '1'):
                    add = '1' + add
                elif (carry == '0'):
                    # 1 + 1 + 0
                    if (a[-i] == '1' and b[-i] == '1'):
                        add = '0' + add
                        carry = '1'
                    # 0 + 0 + 0
                    elif (a[-i] == '0' and b[-i] == '0'):
                        add = '0' + add
                    # 1 + 0 + 0 or 0 + 1 + 0
                    else:
                        add = '1' + add
                else:
                    # 0 + 0 + 1
                    if (a[-i] == '0' and b[-i] == '0'):
                        add = '1' + add
                        carry = '0'
                    # 1 + 0 + 1 or 0 + 1 + 1
                    else:
                        add = '0' + add
        
        if (carry == '1'):
            return carry + add
        return add
