import re
def tocount(s, not_begin):
    import re
    s = re.sub(r'[?!,.]', '', s)
    s = s.replace('\r\n',' ')
    s = s.strip()
    l1 = len(s.split(' '))


    n = s.split(' ')
    unic = []

    #Сімвалы, з якіх можа складацца, але не можа пачынацца слова
    nb = list(not_begin)

    for element in s.split(' '):
      if any(element[0] == i for i in nb):
        continue
      else:
        unic.append(element)

    result={}

    l2 = len(set(n))

    for i in unic:
        result[i]=n.count(i)

    return result, l1, l2



def context(s, num):

    s = s.replace('\r\n', ' ')
    s = s.replace('? ', ' ?')
    s = s.replace('! ', ' !')
    s = s.replace('. ', ' .')
    s = s.replace(', ', ' ,')
    # s = s.replace('(','')
    # s = s.replace(')','')
    # s = s.replace(': ', ' :')
    s = s.split(' ')
    n = s.copy()



    context_list = []
    global context_item

    for i in range(len(s)):

        s[i] = re.sub(r'[,?.!]', '', s[i])

       # print('\n')

        context_item = ''

        if i > 0:  # левы кантэкст
            k = num
            sp = []  # list creation for showing left words in a reversed order
            ind = 1  # increasing counter to grab the words into the list one by one
            while k > 0:  # context-limit counter
                d = i - ind  # a word to grab!!!
                if d >= 0:  # prohibits the counting going below a zero index
                    sp.append(n[d])

                    k -= 1  # context-limit counter decrease
                    ind += 1  # word-grabbing counter increases to grab "lefter" word

                else:
                    break  # if context-limit is depleted, the cycle goes to the next word in a sentence
            # print(*reversed(sp), end = ' ')

            context_item = ' '.join(reversed(sp))
            # print(context_item)

        # print('*{}* '.format(s[i]),end='') #слова, ад якога будуецца кантэкст

        context_item += '*' + s[i] + '*'

        if len(s) - 1 - i >= num:  # правы кантэкст

            k = 1
            while k <= num:
                # print(s[i + k], end=' ')
                context_item += n[i + k] + ' '
                k += 1
        else:
            ind = 1
            while i + ind <= len(s) - 1:
                # print(s[i+ind])
                context_item += n[i + ind] + ' '
                ind += 1

        context_list.append(context_item)


    d_2 = {}
    for i in range(len(context_list)):

        if context_list[i].split('*')[1] in d_2.keys():

            d_2[context_list[i].split('*')[1]].append([context_list[i].split('*')[0], context_list[i].split('*')[2]])
        else:
            d_2.update({context_list[i].split('*')[1]: [[context_list[i].split('*')[0], context_list[i].split('*')[2]]]})

    return d_2


result, l1, l2 = tocount('Груша вось цвіла, апошні год, сябры, вось так!','')
# print(result)
# print(context("Груша вось цвіла, апошні год, сябры, вось так!",3))

def commonize(a,b):
    sp = []
    for i in a.keys():
        item_list = []
        item_list.append(i)
        item_list.append(a[i])

        if a[i] >= 2:

            for k in range(a[i]):

                t = [b[i][k][0], b[i][k][1]]
                item_list.append(t)
        else:

            t = [b[i][0][0], b[i][0][1]]
            item_list.append(t)


        sp.append(item_list)
    return sp



# print(commonize(result,context('Груша вось цвіла, апошні год, сябры, вось так!',3)))


