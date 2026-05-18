import time

def print_happy_diwali():
    # Decorative elements
    fireworks = [
        "🎆", "🎇", "✨", "🎉", "🪔"
    ]
    
    # Print a happy diwali message with decorations
    print("\n" + "🎆" * 10)
    print("🎇" + " " * 8 + "🎇")
    print("✨  Happy Diwali! 🎉")
    print("🎇" + " " * 8 + "🎇")
    print("🎆" * 10 + "\n")
    
    # Create a fireworks effect
    for i in range(5):
        print(" ".join(fireworks))
        time.sleep(0.5)  # Pause for half a second
        print("\033[F\033[K" * 5)  # Clear the previous line

if __name__ == "__main__":
    print_happy_diwali()