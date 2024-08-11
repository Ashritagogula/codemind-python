def weight(w, x, y, z):
    if w == x or w == y or w == z:
        return "YES"
    if w == x + y or w == y + z or w == z + x:
        return "YES"
    if w == x + y + z:
        return "YES"
    return "NO"

w, x, y, z = map(int, input().split())
print(weight(w, x, y, z))
