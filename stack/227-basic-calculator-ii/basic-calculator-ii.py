class Solution:
    def calculate(self, s: str) -> int:
        st = []
        prev = "+"
        cu = 0

        for c in s + "+":
            if c.isdigit():
                cu = cu * 10 + int(c)

            if c in "+-*/":
                if prev == "+":
                    st.append(cu)
                elif prev == "-":
                    st.append(-cu)
                elif prev == "*":
                    st.append(st.pop() * cu)
                elif prev == "/":
                    st.append(int(st.pop() / cu))

                prev = c
                cu = 0

        return sum(st)