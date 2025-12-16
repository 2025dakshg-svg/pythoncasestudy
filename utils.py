# utils.py
def require_positive(func):
    """Decorator to ensure amount > 0"""
    def wrapper(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
            return False
        return func(self, amount)
    return wrapper
