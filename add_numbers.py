def add(*args):
    return sum(args)

def main():
    numbers = []

    while True:
        c = input("Enter a number (or 's' to stop): ")
        if c.lower() == 's':
            break
        try:
            # Convert to int before appending
            value = int(c)
            numbers.append(value)
        except ValueError:
            print(f" '{c}' is not a valid integer. Please try again.")

    # If you want to guard against the empty-list case:
    if not numbers:
        print("No numbers entered.")
    else:
        total = add(*numbers)
        print(f"You entered: {numbers}")
        print(f"Sum = {total}")

if __name__ == "__main__":
    main()