from postcode import verify_postcode

def main() -> None:
    print("""
    +----------------------------------------------+
    |          Welcome to my UK Postcode           |
    |            Validation Program!               |
    |   This program will validate UK postcodes.   |
    +----------------------------------------------+
    \n""")
    verify_postcode()

if __name__ == "__main__":
    main()
