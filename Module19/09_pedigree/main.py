pedigree = dict()       # Не знал, что на английском это родословная, а не собачий корм))

for i in range(1, int(input('Введите количество человек: '))):     # закидываем все в словарь {родитель : [дети дети дети]}
    print(i, 'пара:', end=' ')
    relatives = input().split()
    if relatives[1] in pedigree:
        pedigree[relatives[1]].append(relatives[0])
    else:
        pedigree[relatives[1]] = [(relatives[0])]

generations = {}                # находим проотца (человека без родителей) Работает только на большой выборке. с 2-3 парами не сработает
for i in pedigree.keys():
    for q in pedigree.values():
        if i in q:
            break
    else:
        generations[i] = 0          #закидываем отца в новый словарь с нормальным видом {человек : поколение}
        for q in pedigree[i]:
            generations[q] = 1

for i in generations:
    if generations[i] == 0:
        pedigree.pop(i)

tik = 1
while len(pedigree) != 0:           # Закидываем остальных в новый словарь, удаляя при этом закинутых из прошлого, шоб не мешались)
    tik += 1
    for names in generations.copy().keys():
        if names in pedigree:
            for lokal_names in pedigree[names]:
                generations[lokal_names] = tik
    for names in generations.keys():
        if names in pedigree and generations[names] < tik:
            pedigree.pop(names)

print('“Высота” каждого члена семьи:')
for i in sorted(generations.keys()):
    print(i, generations[i])
