import string

lwr = string.ascii_lowercase
upr = string.ascii_uppercase

given = """Ypw'zj zwufpp hwu txadjkcq dtbtyu kqkwxrbvu! Mbz cjzg kv IAJBO{ndldie_al_aqk_jjrnsxee}. Xzi utj gnn olkd qgq ftk ykaqe uei mbz ocrt qi ynlu, etrm mff'n wij bf wlny mjcj"""

deciphered = ""

for index, element in enumerate(given):
    if element in upr:
        alpha = upr
    elif element in lwr:
        alpha = lwr
    else:
        deciphered += element
        continue

    deciphered += alpha[(alpha.index(element) - index) % len(alpha)]
print(deciphered)

flag = ""