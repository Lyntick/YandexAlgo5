P,V= map(int, input().split())
Q,M = map(int, input().split())
result = V*2 + M*2 + 2
result -= max(min(P+V,Q+M) - max(P-V,Q-M) + 1,0)
print(result)