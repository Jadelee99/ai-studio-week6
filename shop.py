class Customer:
    def add_points(self, amount):
        self.points += int(amount*0.07)
    def get_discount_rate(self):
        if self.grade=="vip":
            return 0.10
        else :
            return 0.03
    def summary(self):
        return f"[{self.grade}]{self.name}(포인트: {self.points:,})"
class Order:
    def add_item(self,name,price):
        self.items.append((name,price))
    def total_price(self):
        raw_total=0
        for item in self.items:
            raw_total+=item[1]
        discount_rate=self.customer.get_discount_rate()
        final_price=int(raw_total*(1-discount_rate))
        return final_price
    def pay(self):
        final_price=self.total_price()
        self.customer.add_points(final_price)
        return final_price
vip_user=Customer()
vip_user.name="김철수"
vip_user.grade="vip"
vip_user.points=0
basic_user=Customer()
basic_user.name="김영희"
basic_user.grade="basic"
basic_user.points=0
order1=Order()
order1.order_id="Order1"
order1.customer=vip_user
order1.items=[]
order1.add_item("초코케이크",50000)
order1.add_item("아메리카노",5000)
order2=Order()
order2.order_id="Order2"
order2.customer=basic_user
order2.items=[]
order2.add_item("딸기케이크", 30000)
order3=Order()
order3.order_id="Order3"
order3.customer=vip_user
order3.items=[]
order3.add_item("말차라떼", 8000)
print("=== 주문 결제 내역 ===")
print(f"주문 1 결제 금액: {order1.pay():,}원")
print(f"주문 2 결제 금액: {order2.pay():,}원")
print(f"주문 3 결제 금액: {order3.pay():,}원")
print("\n=== 최종 고객 상태 ===")
print(vip_user.summary())
print(basic_user.summary())