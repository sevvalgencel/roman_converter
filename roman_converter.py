def roman_to_arabic(roman):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    subtractive_combinations = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    # Geçersiz desenleri kontrol et
    invalid_patterns = [
        "IIII", "VV", "XXXX", "LL", "CCCC", "DD", "MMMM",
        "IL", "IC", "ID", "IM",
        "VX", "VL", "VC", "VD", "VM",
        "XD", "XM",
        "LC", "LD", "LM",
        "DM"
    ]

    # Saçma veya geçersiz karakterleri kontrol et
    valid_characters = set(roman_numerals.keys())
    for char in roman:
        if char not in valid_characters:
            return "Yanlış giriş yapıldı, lütfen geçerli bir Roma rakamı giriniz."

    for pattern in invalid_patterns:
        if pattern in roman:
            return "Yanlış giriş yapıldı, lütfen geçerli bir Roma rakamı giriniz."

    # Geçerli Roma rakamlarını Arap rakamlarına çevir
    i = 0
    arabic_value = 0
    while i < len(roman):
        # Çıkarma kombinasyonlarını kontrol et
        if i + 1 < len(roman) and roman[i:i + 2] in subtractive_combinations:
            arabic_value += subtractive_combinations[roman[i:i + 2]]
            i += 2
        else:
            arabic_value += roman_numerals.get(roman[i], 0)
            i += 1

    # Çıkarma ve toplama kombinasyonlarının geçerli olup olmadığını kontrol et
    if not is_valid_roman(roman, subtractive_combinations):
        return "Yanlış giriş yapıldı, lütfen geçerli bir Roma rakamı giriniz."

    return arabic_value


def is_valid_roman(roman, subtractive_combinations):
    roman_numerals_order = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value = 0
    subtractive_combination_used = False

    for i in range(len(roman)):
        current_value = roman_numerals_order.get(roman[i], 0)

        # Eğer bir çıkarma kombinasyonu kullanılmışsa, tekrar kullanılıp kullanılmadığını kontrol et
        if subtractive_combination_used:
            if current_value > prev_value:
                return False
            subtractive_combination_used = False

        # Çıkarma kombinasyonunu kontrol et
        if i + 1 < len(roman) and roman[i:i + 2] in subtractive_combinations:
            subtractive_combination_used = True
            prev_value = roman_numerals_order[roman[i + 1]]
            continue

        # Geçerli bir toplama kombinasyonu mu?
        if current_value > prev_value and prev_value != 0:
            if current_value > 10 * prev_value:
                return False

        prev_value = current_value

    return True


