def soundex(word):
    """Soundex algorithm implementation.

    :param word: word to encode
    :type word: str
    :return: Soundex code
    :rtype: str
    """
    word = word.upper()
    soundex_code = word[0]
    for char in word[1:]:
        if char in "BFPV":
            soundex_code += "1"
        elif char in "CGJKQSXZ":
            soundex_code += "2"
        elif char in "DT":
            soundex_code += "3"
        elif char in "L":
            soundex_code += "4"
        elif char in "MN":
            soundex_code += "5"
        elif char in "R":
            soundex_code += "6"
        else:
            soundex_code += "0"

    soundex_code = soundex_code[0] + "".join(
        [char for char in soundex_code[1:] if char != soundex_code[0]]
    )
    soundex_code = soundex_code.replace("0", "")

    return (soundex_code + "000")[:6]


print(soundex("Robert"))
print(soundex("Rupert"))
