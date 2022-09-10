def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s
    output = ""
    index = 0
    strings = []
    flag = -1
    for i in range(numRows):
        new = ""
        strings.append(new)
    for i in s:  
        strings[index] = strings[index] + i
        if (index == numRows-1) or (index == 0):
            flag = flag * -1 
        index = index + (1*flag)
    for i in range(numRows):
        output = output + strings[i]



    return output


def test():
    
    s = "PAYPALISHIRING"
    numRows = 3
    """
    Output: "PAHNAPLSIIGYIR"
    """
    print(convert(s, numRows))
    
    s = "PAYPALISHIRING"
    numRows = 4
    """
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    """
    print(convert(s, numRows))
    s = "AB"
    numRows = 1
    print(convert(s, numRows))


test()
