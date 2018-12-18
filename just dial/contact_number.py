def contact_number(numbers):
    a = []
    for number in numbers:
        number = str(number)
        if 'icon-acb' in number:
            a.append(0)
        if 'icon-yz' in number:
            a.append(1)
        if 'icon-vu' in number:
            a.append(3)
        if 'icon-wx' in number:
            a.append(2)
        if 'icon-ts' in number:
            a.append(4)
        if 'icon-rq' in number:
            a.append(5)
        if 'icon-po' in number:
            a.append(6)
        if 'icon-nm' in number:
            a.append(7)
        if 'icon-lk' in number:
            a.append(8)
        if 'icon-ji' in number:
            a.append(9)
        if 'icon-dc' in number:
            a.append('+')
        if 'icon-fe' in number:
            a.append('(')
        if 'icon-hg' in number:
            a.append(')')
        if 'icon-ba' in number:
            a.append('-')
    stra = ''.join(str(e) for e in a)
    return stra
