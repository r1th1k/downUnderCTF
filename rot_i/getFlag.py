import subprocess

# given = """IAJBO{ndldie_al_aqk_jjrnsxee}"""
given = list(
    """Ypw'zj zwufpp hwu txadjkcq dtbtyu kqkwxrbvu! Mbz cjzg kv IAJBO{ndldie_al_aqk_jjrnsxee}. Xzi utj gnn olkd qgq ftk ykaqe uei mbz ocrt qi ynlu, etrm mff'n wij bf wlny mjcj""")

# print(given)
i = 0
for x in given:
    i += 1
    if x == "I":
        print(i)

flag = []


# for i in range(21, -1, -1):
# for i in range(173, -1, -1):
#     x = subprocess.check_output(
#         "echo " + given + " | caesar " + str(i), shell=True).decode()
#     flag.append(x)


# print(flag)
# ans = ""
# u = 0
# try:
#     while u <= len(flag):
#         for i in flag:
#             ans += str(i[u])
#             u += 1
# except:
#     print("done")


# print(ans)
# DUCTF{crypto_is_fun_kjmhlpvu}
