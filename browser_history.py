
#https://leetcode.com/problems/design-browser-history/submissions/1279474564/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.back_st = []
        self.forward_st = []
        self.current_page = homepage

    def visit(self, url: str) -> None:
        self.back_st.append(self.current_page)
        self.current_page = url 
        self.forward_st.clear()

    def back(self, steps: int) -> str:
        while steps != 0 and self.back_st :
            self.forward_st.append(self.current_page)
            self.current_page = self.back_st.pop()
            steps -= 1
        return self.current_page

    def forward(self, steps: int) -> str:
        while steps != 0 and self.forward_st :
            self.back_st.append(self.current_page)
            self.current_page = self.forward_st.pop()
            steps -= 1
        return self.current_page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
