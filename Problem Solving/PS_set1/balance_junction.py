N, M, R = map(int, input().split())

RC1, RC2, RC3 = map(int, input().split())
RC4, RC5, RC6= map(int, input().split())


new_RC1 = RC1 - R
new_RC2 = RC2 - R
new_RC3 = RC3 - R

new_RC4 = RC4 - R
new_RC5 = RC5 - R
new_RC6 = RC6 - R

summ_ac_in = new_RC1 + new_RC2 + new_RC3
summ_ac_out = new_RC4 + new_RC5 + new_RC6

if summ_ac_in < summ_ac_out:
    req = (summ_ac_out - summ_ac_in) + R
    print(req * 1)
elif summ_ac_in > summ_ac_out:
    requird = (summ_ac_in - summ_ac_out) + R
    print(requird* -1)
else:
    print("balanced")