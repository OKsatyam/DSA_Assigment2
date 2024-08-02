
#https://leetcode.com/problems/online-stock-span/submissions/1281939233/

class StockSpanner:

    def __init__(self):
        self.stockSpanner = [] 
    def next(self, price: int) -> int:
        span = 1
        while self.stockSpanner and self.stockSpanner[-1][0] <= price :
            span += self.stockSpanner.pop()[1]
        
        self.stockSpanner.append([price,span])
        return span
        
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)