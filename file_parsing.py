math_B =[]
for line in open("sslc1.txt"):
    fields = line.split(';')
    reg_code = fields[0].strip()
    math_str = fields[5]
    if math_str == 'A':
        
    math_mark = float(fields[5]) if fields[5] != 'AA' else 0
    if reg_code == 'B':
        math_B.append(math_mark)