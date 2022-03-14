n, m = map(int, input().split())
n_dfs = list(map(int, input().split()))
m_dfs = list(map(int, input().split()))
print(max(n_dfs) + max(m_dfs))