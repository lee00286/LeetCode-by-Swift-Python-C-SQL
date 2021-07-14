class Solution:
    def customSortString(self, order: str, str: str) -> str:
        index = 0
        i = 0

        while i < len(order) and index < len(str):
            if order[i] in str[index:]:
                j = str[index:].find(order[i]) + len(str[:index])
                if j < len(str) - 1:
                    str = str[:index] + str[j] + str[index:j] + str[j + 1:]
                else:
                    str = str[:index] + str[j] + str[index:j]
                index += 1
            else:
                i += 1

        return str
