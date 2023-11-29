#!/usr/bin/env python3

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("ERROR : La division par zero n'est pas possible")
        else:
            return x / y

    def calculate(self, operation, x, y):
        result = {
            '+': self.add(x, y),
            '-': self.subtract(x, y),
            'x': self.multiply(x, y),  # Utilisation de 'x' pour la multiplication
            '/': self.divide(x, y)
        }.get(operation, "Error: Invalid operation.")

        self.history.append((operation, x, y, result))
        return result

    def view_history(self):
        for entry in self.history:
            print(f"{entry[1]} {entry[0]} {entry[2]} = {entry[3]}")

    def clear_history(self):
        self.history = []

def validate_input(input_value):
    try:
        float_value = float(input_value)
        return True, float_value
    except ValueError:
        return False, None

def main():
    calculator = Calculator()
    while True:
        operation = input("Enter operation (+, -, x, /): ")
        x = input("Enter le premier nombre : ")
        y = input("Enter le second nombre: ")

        is_valid_x, x = validate_input(x)
        is_valid_y, y = validate_input(y)

        if is_valid_x and is_valid_y:
            try:
                result = calculator.calculate(operation, x, y)
                print(f"Resultat : {result}")
            except ValueError as e:
                print(e)
        else:
            print(f"Erreur : Entrée invalide. Veuillez entrer un nombre valide.")

        user_input = input("Voir l'historique ? (yes/no): ")
        if user_input.lower() == 'yes':
            calculator.view_history()

        user_input = input("Netoyer l'historique ? (yes/no): ")
        if user_input.lower() == 'yes':
            calculator.clear_history()

        user_input = input("Continue? (yes/no): ")
        if user_input.lower() == 'no':
            break

if __name__ == "__main__":
    main()
