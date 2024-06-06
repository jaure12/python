class Shoes:
    def __init__(self, name, price):
            self.name = name
            self.price = float(price)

    def budget_check(self, budget):
            if not isinstance(budget, (int, float)):
                    print("Invalid entry. Please enter number")
                    exit()

    def change(self, budget):
            return(budget - self.price)

    def buy(self, budget):
            self.budget_check(budget)

            if budget >= self.price:
                    print(f"You can afford these shoes")

                    if budget == self.price:
                            print("You have the exact amount for these shoes")

                    else:
                            print(f'You can buy these shoes and have ${self.change(budget)} left over')

                    exit("Thank you")

