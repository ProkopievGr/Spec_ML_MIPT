from os import chdir


f_old = open('checkins.dat')
f_new = open('data.csv', 'w')

content = f_old.readlines() 

header = ','.join(content[0].replace(' ', '').split('|'))
f_new.write(header)

for line in content[2:]:
    line_content = line[:-22].replace(' ', '').split('|')
    line_content.append(line[-20:])
    # print(line_content)
    if line_content[3] != '' and line_content[4] != '':
        f_new.write(','.join(line_content))
    
f_old.close()
f_new.close()