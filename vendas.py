class cart:
    def __init__(self, user, itens = []):
        self.user = user
        self.itens = itens
        
    def include(self, product, desired_amount):
        if product.amount == 0:
            print("Produto em falta no estoque!")
        elif product.amount >= desired_amount:
            self.itens.apppend(product)
        else:
            print("Quantidade solicítada indisponível!\n")
            
    def calculate_cart_value(self):
        total = 0.
        for i in self.itens:
            total += i.price
        return total
        
    def clear_cart(self):
        self.itens = []
        print("Carrinho esvaziado")
        
    def remove_item(self, product):
        self.itens.remove(product)
        
class item:
    def __init__(self, id_number, name, price, amount):
        self.id_number = id_number
        self.name = name
        self.price = price
        self.amount = amount
        
    def show_item(self):
        print("ID: %s\n%s\nPrice: R$%.2f" %(self.id_number, self.name, 
                self.price))
    
    
        
