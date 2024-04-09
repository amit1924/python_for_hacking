import argparse


def main():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(
        description="A simple program to know the person name and his age"
    )

    # Add arguments
    parser.add_argument("name", type=str, help="Please tell me your name")
    parser.add_argument("age", type=int, help="Please tell me your age")

    # Parse the arguments
    args = parser.parse_args()

    # Extract values from parsed arguments
    name = args.name
    age = args.age

    # Print the name and age
    print(f"Name :{name},Age:{age}")


if __name__ == "__main__":
    main()
