def get_data():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    return x1, y1, x2, y2

def get_line(x1, y1, x2, y2):
    if x1 == x2:
        rst = f"x = {x1}"
    else:
        slp = (y2 - y1) / (x2 - x1)
        y_i= y1 - slp * x1
        rst = f"y = {slp}x + {y_i}" if y_i >= 0 else f"y = {slp}x - {abs(y_i)}"
    return rst

x1, y1, x2, y2 = get_data()
line = get_line(x1, y1, x2, y2)
print(line)