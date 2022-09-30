def split_idx(l, idx):
    return l[:idx], l[idx+1:]

def calc(l):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return l[0]
    # print(l)
    m = min(l)
    idx = l.index(m)
    l = [v - m for v in l]
    left ,right = split_idx(l, idx)
    # print(left, right)
    return calc(left) + calc(right) + m


def main():
    N = int(input())
    l = [int(v) for v in input().split()]
    c = calc(l)
    print(c)



if __name__ == '__main__':
    main()
