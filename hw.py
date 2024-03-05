# Create a class called cart that retains items and has methods to add, remove, and show

class ShoppingCart:
    def __init__(self):
        self.cart = []
        self.total_cost = 0

    def add_item(self, name, quantity, price):
        self.cart.append({'name': name, 'quantity': quantity, 'price': price})
        self.total_cost += quantity * price
        print('Item added to the cart!')

    def remove_item(self, name):
        for item in self.cart:
            if item['name'] == name:
                self.total_cost -= item['quantity'] * item['price']
                self.cart.remove(item)
                print('Item removed from the cart!')
                break
        else:
            print('Item not found in the cart. Try again')

    def show_cart(self):
        print('\nCurrent Cart:')
        for item in self.cart:
            print(f'{item['name']} - Quantity: {item['quantity']}, Price: ${item['price']:.2f}')
        print(f'Total Cost: ${self.total_cost:.2f}')

    def exit_program(self):
        print('\nThank you for using the Shopping Cart Program!')
        print('\nThe Receipt:')
        for item in self.cart:
            print(f'{item['name']} - Quantity: {item['quantity']}, Price: ${item['price']:.2f}')
        print(f'Total Cost: ${self.total_cost:.2f}')
     
    def shopping_cart_program(self):
        print('Welcome to my Shopping Cart!')

        while True:
            print('\nMenu:')
            print('1. Add item to cart')
            print('2. Remove item from cart')
            print('3. Show cart')
            print('4. Quit')

            choice = input('Enter your choice (1, 2, 3, 4): ')

            if choice == '1':
                name = input('Enter the item name: ')
                quantity = int(input('Enter the quantity: '))
                price = float(input('Enter the price: '))
                self.add_item(name, quantity, price)

            elif choice == '2':
                name_to_remove = input('Enter the item name to remove: ')
                self.remove_item(name_to_remove)

            elif choice == '3':
                self.show_cart()

            elif choice == '4':
                self.exit_program()
                break

            else:
                print('Invalid choice. Please enter 1, 2, 3, or 4.')

cart = ShoppingCart()
cart.shopping_cart_program()   


#Exercise 1 - Write a Python class for an Animal that has a name and energy attributes. The animal class should also have methods for eat, sleep, and play that will take in an integer and increase/decrease the energy of the animal with a formatted print statement

#video game skills came into play for this hw
class Animal:
    def __init__(self, name, energy=50):
        self.name = name
        self.energy = energy

    def eat(self, food):
        self.energy += food
        print(f'{self.name} is eating. Energy increased by {food}. Current energy: {self.energy}')

    def sleep(self, hours):
        self.energy += 10 * hours
        print(f'{self.name} is sleeping. Energy increased by {10 * hours}. Current energy: {self.energy}')

    def play(self, play):
        self.energy -= 5 * play
        print(f'{self.name} is playing. Energy decreased by {5 * play}. Current energy: {self.energy}')

    def get_energy(self):
        return self.energy

my_animal = Animal(name='Tyrone')
print(f'My name is {my_animal.name} and my energy is {my_animal.get_energy()}')

my_animal.eat(30)
my_animal.sleep(2)
my_animal.play(1)

print(f'WHEWWW! My name is {my_animal.name} and my energy is {my_animal.get_energy()}')

