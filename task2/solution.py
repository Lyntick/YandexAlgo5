match1G1, match1G2 = map(int, input().split(':'))
match2G1, match2G2 = map(int, input().split(':'))
matchIsHome = True if int(input()) == 2 else False
result = 0
if match1G1 + match2G1 <= match1G2 + match2G2:
    result = match1G2 + match2G2 - match1G1 - match2G1
    match2G1 += result
    if matchIsHome and match1G1 <= match2G2 or not matchIsHome and match2G1 <= match1G2:
        result += 1
print(result)