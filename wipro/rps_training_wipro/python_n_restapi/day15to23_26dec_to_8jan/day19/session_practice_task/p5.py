import argparse

def main():
    parser = argparse.ArgumentParser(description="Perform a mathematical operation")
    parser.add_argument(
        "--operation",
        choices=["add", "sub", "mul", "div"],
        required=True,
        help="Operation to perform: add, sub, mul, div"
    )
    parser.add_argument(
        "--x",
        type=float,
        required=True,
        help="First number"
    )
    parser.add_argument(
        "--y",
        type=float,
        required=True,
        help="Second number"
    )

    args = parser.parse_args()

    if args.operation == "add":
        result = args.x + args.y
    elif args.operation == "sub":
        result = args.x - args.y
    elif args.operation == "mul":
        result = args.x * args.y
    elif args.operation == "div":
        if args.y == 0:
            print("Error: Division by zero")
            return
        result = args.x / args.y
    else:
        print("Invalid operation")
        return

    print(f"The result of {args.operation} is: {result}")

if __name__ == "__main__":
    main()
