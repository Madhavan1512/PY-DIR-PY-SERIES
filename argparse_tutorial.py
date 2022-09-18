import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number 1", help="First number")
    parser.add_argument("number 2", help="Second number")
    parser.add_argument("operation", help="operation")
    args = parser.parse_args()
    print(args.number1)
    print(args.number2)
    print(args.operation)
    
    