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
        if i + 1 < len(roman) and roman[i:i+2] in subtractive_combinations:
            subtractive_combination_used = True
            prev_value = roman_numerals_order[roman[i + 1]]
            continue

        # Geçerli bir toplama kombinasyonu mu?
        if current_value > prev_value and prev_value != 0:
            if current_value > 10 * prev_value:
                return False

        prev_value = current_value

    return True
