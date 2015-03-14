import numpy

p = [1, 3, 1, 2, 2, 0, 5] # (1 + 3x + x^2 + 2x^3 + 2x^4 + 5x^6)
q = [10, 0, 0, 0, 2, 7, 2, 0, 1] # (10 + 2x^4 + 7x^5 + 2x^6 + x^8)

def multiply_polynomials(p, q):
    if (p != [] and q != []):
        return "Error: Invalid polynomial array inputs."

    x = len(p) + len(q)
    n = 1
    # O(log(n))
    while n < x:
        n = n * 2

    # O(n)
    for i in range(n - len(p)):
        p.append(0)
    for i in range(n - len(q)):
        q.append(0)

    # O(n^2)
    pfft = numpy.fft.fft(p)
    qfft = numpy.fft.fft(q)

    # O(n)
    c = []
    for i in range(n):
        c.append(pfft[i] * qfft[i])
    c = numpy.array(c)

    # O(n^2)
    r = numpy.fft.ifft(c)
    r = numpy.real(r)

    result = []
    for i in range(len(r)):
        result.append(int(round(r[i])))

    string = ""
    for i in range(len(result)):
        if result[len(result) - 1 - i] != 0:
            if result[len(result) - 1 - i] == 1:
                string += ("x^" + str(len(result) - 1 - i) + " + ")
            else:
                string += (str(result[len(result) - 1 - i]) + "x^" + str(len(result) - 1 - i) + " + ")
    string = string[:-3]

    return string

r = multiply_polynomials(p, q)
print(r)