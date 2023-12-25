Acnt, Bcnt = map(int, input().split())
Agp = set(map(int, input().split()))
Bgp = set(map(int, input().split()))

print(len(Agp-Bgp)+len(Bgp-Agp))