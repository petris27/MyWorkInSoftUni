n_broj, m_broj = [int(XxX) for XxX in input().split()]
set_one = set()
set_two = set()
for purvi_set in range(n_broj):
    chislo = int(input())
    set_one.add(chislo)
for vtori_set in range(m_broj):
    chislo = int(input())
    set_two.add(chislo)

obsht_set = set_one & set_two
for izbranite_chisla in obsht_set:
    print(izbranite_chisla)