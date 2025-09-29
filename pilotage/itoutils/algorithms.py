def check_luhn(n):
    # Source: https://rosettacode.org/wiki/Luhn_test_of_credit_card_numbers#Functional_2
    r = [int(ch) for ch in str(n)][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(d * 2, 10)) for d in r[1::2])) % 10 == 0
