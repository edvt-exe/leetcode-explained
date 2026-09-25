class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)
        i = 0
        def parse_expression():
            nonlocal i

            result = parse_term()

            while i < n and expression[i] == ',':
                i += 1
                result |= parse_term()

            return result

        def parse_term():
            nonlocal i

            result = {""}

            while i < n and expression[i] not in '},':
                factor = parse_factor()
                result = {
                    a + b
                    for a in result
                    for b in factor
                }

            return result

        def parse_factor():
            nonlocal i
            if expression[i] == '{':
                i += 1
                result = parse_expression()
                i += 1
                return result
            start = i
            while i < n and expression[i].islower():
                i += 1

            return {expression[start:i]}

        return sorted(parse_expression())