import re
def extract_integers(input_string, allow_negative=False):
    pattern = r'-?\d+' if allow_negative else r'\d+'
    integers = re.findall(pattern, input_string)
    integers = [int(num) for num in integers]

    return integers


with open("input.txt", "r") as f:
    inp = f.read().strip().split("\n\n")
res = 0
for system in inp:
    ax,ay,bx,by,px,py = extract_integers(system)
    #part2
    px+=10000000000000
    py+=10000000000000

    a = (px*by - py*bx) / (ax*by -ay*bx)
    b = (px -ax*a)/bx

    if (int(a) == a) and (int(b) == b):
        res += int(a*3 + b)
print(res)
