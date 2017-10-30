under_ten_digit_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                        'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
under_hundred_digit_list = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

hundred = 'hundred'
thousand = 'thousand'
and_word = 'and'

SUMM = 0


def under_twenty(digit):
    return len(under_ten_digit_list[digit - 1])   # 1, 2, 3 ....


def under_hundred(two_digit):
    first_digit_len = len(under_hundred_digit_list[two_digit//10 - 2])

    last_digit = two_digit % 10
    if last_digit:
        last_digit_len = under_twenty(last_digit)
        return first_digit_len + last_digit_len

    return first_digit_len


for i in range(1, 1001):
    if i < 20:
        SUMM += under_twenty(i)
    elif i < 100:
        SUMM += under_hundred(i)
    elif i < 1000:
        SUMM += under_twenty(i // 100)
        if i % 100 == 0:
            SUMM += len(hundred)  # 100, 200, 300....
        else:
            SUMM += len(hundred + and_word)  # 1XX, 2XX, 3XX.....
            j = i % 100
            if j < 20:
                SUMM += under_twenty(j)
            else:
                SUMM += under_hundred(j)
    else:
        SUMM += len(under_ten_digit_list[0] + thousand)
print(SUMM)
