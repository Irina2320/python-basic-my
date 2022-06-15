alphabet = list('abcdefghijklmnopqrstuvwxyz')
alphabet2 = list(''.join(alphabet).upper())

message = list('''vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip''')

print(message)
for i in range(len(message)):
    if message[i] in alphabet:
        message[i] = alphabet[(alphabet.index(message[i]) - 1) % len(alphabet)]
    elif message[i] in alphabet2:
        message[i] = alphabet2[(alphabet2.index(message[i]) - 1) % len(alphabet2)]

message = (''.join(message)).split()
new_list = []

shift = 3
for new_string in message:
    for _ in range(shift):
        new_string = list(new_string)
        new_string.insert(0, new_string.pop())

    if new_string[-1] == '/':
        new_string[-1] = '\n'
        shift += 1
    new_list.append(''.join(new_string))
print(str(' '.join(new_list)))

# Если есть более простое решение - можете скинуть))
