def find_generator(G):
    n = G.order()
    factors = [f[0] for f in factor(n)]
    one = G.identity()

    while True:
        g = G.random_element()
        if g == one: continue
        
        is_generator = True
        for p in factors:
            if g^(n // p) == one:
                is_generator = False
                break
        
        if is_generator:
            return g

# --- Main Script ---

ID_SUM = 2559003 + 2612521  
mod_val = ID_SUM % 10
bound = 2^15 + 2^mod_val

print(f"Lower Bound: {bound}")

p = next_prime(bound)
print(f"p = {p}")

F = GF(p)
G = F.unit_group() 

print(f"Group Order: {G.order()}")

gen = find_generator(G)

print("-" * 20)
print(f"Generator (g): {gen}")
print("-" * 20)

# print(f"Order check: {gen.multiplicative_order() == p-1}")