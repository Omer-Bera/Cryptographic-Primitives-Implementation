# Elliptic Curve Parameters: y^2 = x^3 + ax + b (mod p)
p = 13
a = 0
b = 4

# We will use 'None' for the pt at infinity.
INFINITY = None

def modular_inverse(n, p):
    return pow(n, -1, p)

def point_add(P, Q):
    if P is INFINITY: return Q
    if Q is INFINITY: return P
    
    x1, y1 = P
    x2, y2 = Q
    
    # Case 1: if the points are symetric according to x-axis
    if x1 == x2 and y1 != y2:
        return INFINITY
    
    # Case 2: Doubling
    if P == Q:
        return point_double(P)
    
    # Case 3: Addition operation for distinct points (Slope: (y2-y1)/(x2-x1))
    num = (y2 - y1) % p
    den = (x2 - x1) % p
    lam = (num * modular_inverse(den, p)) % p
    x3 = (lam**2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3, y3)

def point_double(P):
    if P is INFINITY: return INFINITY
    
    x1, y1 = P
    
    # If y1 = 0, the tangent is perpendicular -> Infinity
    if y1 == 0:
        return INFINITY
        
    # Slope (lambda) formula: (3x1^2 + a) / (2y1)
    num = (3 * x1**2 + a) % p
    den = (2 * y1) % p
    
    lam = (num * modular_inverse(den, p)) % p
    
    x3 = (lam**2 - 2 * x1) % p
    y3 = (lam * (x1 - x3) - y1) % p
    
    return (x3, y3)

def multiply_point(k, P):
    current_point = INFINITY
    for _ in range(k):
        current_point = point_add(current_point, P)
    return current_point

def find_order(P):
    if P is INFINITY: return 1
    
    k = 1
    current = P
    while current is not INFINITY:
        k += 1
        current = point_add(current, P)
        # For safety, prevent infinite loops (stop if group level exceeds 21)
        if k > 25: return "Error" 
    return k

def find_all_points():
    points = []
    # try x values
    for x in range(p):
        rhs = (x**3 + a*x + b) % p # y^2 = x^3 + 4
        # try y values
        for y in range(p):
            if (y**2) % p == rhs:
                points.append((x, y))
    
    points.sort() # sort by x
    return points

# --- Main ---

print(f"Slope: y^2 = x^3 + {b} (mod {p})")
print("-" * 40)

# 1. Find and list the points
all_points = find_all_points()
print(f"Total Number of Points: {len(all_points)}")
print(f"Group Order: {len(all_points) + 1}")
print("-" * 40)

print(f"{'Point (P)':<15} | {'Order':<15}")
print("-" * 40)

print(f"{'O (Infinity)':<15} | {1:<15}")

for P in all_points:
    order = find_order(P)
    print(f"{str(P):<15} | {order:<15}")