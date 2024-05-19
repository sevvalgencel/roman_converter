from roman_converter import roman_to_arabic

def main():
    while True:
        roman_input = input("Roma rakamı giriniz (çıkmak için 'q' tuşlayın): ").upper()
        if roman_input == 'Q':
            break
        result = roman_to_arabic(roman_input)
        print(f"{roman_input} => {result}")

if __name__ == "__main__":
    main()
