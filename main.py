import sys


def main(a, b, match, miss, gap):
    # Creating the matrix
    m = []
    for i in range(len(a) + 1):
        r = []
        for j in range(len(b) + 1):
            r.append(0)
        m.append(r)

    # Filling the first row
    for i in range(len(m[0])):
            m[0][i] = i*gap

    # Filling the first column
    for j in range(len(m)):
            m[j][0] = j*gap

    for i in range(1, len(m)):
        for j in range(1, len(m[i])):
            # Check if match or not
            if a[i-1] == b[j-1]:
                topleft = m[i-1][j-1] + match
            else:
                topleft = m[i-1][j-1] + miss

            # Compute other two values
            top = m[i-1][j] + gap
            left = m[i][j-1] + gap

            # Compute the max
            m[i][j] = max(topleft, top, left)

    print("a:%s" % a)
    print("b:%s" % b)
    print("Global alignment score: %f\n" % m[len(a)][len(b)])

    print_matrix(m)

    # Initialing variable for traceback
    af = []
    align = []
    bf = []
    # Used for managing gap in sequence
    skip = 0
    print("\nFinal alignment:")
    for i in range(len(m)-1):
        if a[len(a)-i-1] == b[len(b)-i-1+skip]:
            af.append(a[len(a)-i-1])
            align.append("|")
            bf.append(b[len(b)-i-1+skip])
        else:
            af.append(a[len(a)-i-1])
            align.append(" ")
            bf.append("-")
            # Count a skip and not increase counter for rewind of matrix (only if len() not match)
            if len(a) != len(b):
                skip += 1
            i -= 1

    print_list(af)
    print_list(align)
    print_list(bf)


def print_list(l):
    for i in range(len(l), 0, -1):
        print(l[i-1], end='')
    print()


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end='\t')
        print()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))