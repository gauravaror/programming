def solution(N, K):
#    print("Solving ", N,K)
    seen = {}
    def solve(current, left):
        nonlocal seen
        if (current,left) in seen:
            return seen[current, left]
  #      print("dsfd", N, K, current, left)
        if current == N:
#            print(current, N, K)
            return 0
        elif current > N:
            return float('inf')
        if left > 0:
            ans = 1 + min(solve(current+1, left), solve(2*current, left-1))
        else:
            ans = 1 + solve(current+1, left)
        seen[current,left] = ans
        return ans

    return solve(1, K)

print(solution(1,0))
print(solution(8,0))
print(solution(18,2))
print(solution(10,10))
print(solution(700,100))
