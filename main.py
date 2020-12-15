import urllib
import re

url= 'https://vmsensorlog.westeurope.cloudapp.azure.com:1880/huckleberry-finn'

def read_url(url):

    file= urllib.request.urlopen(url)

    text= []
    words_all=[]

    for line in file:
        decoded_line= line.decode('utf-8')
        text.append(decoded_line)
        words= decoded_line.split()
        words_all.append(words)

    # merged text
    merged_text=''.join(text).replace('\n', '')


    # number of words
    print('{} words'.format(len(re.findall(r'\w+', merged_text))))
    # number of letters
    print('{} letters'.format(sum(c.isalpha() for c in merged_text)))
    # number of non alphabets
    print('{} symbols'.format(len(re.findall('r\W+', merged_text))))
    # top 3 frequently appearing words
    # split text into words
    from collections import Counter
    words= re.findall(r'\w+', merged_text)
    dict= Counter(words)
    top_words=dict.most_common(3)
    print('Top 3 most common words are: {}'.format(','.join('{}'.format(value[0])for value in top_words)))
    no_words=[]
    for k,v in dict.items():
        if v==1:
            no_words.append(k)
    print('Words used only once:{}'.format(no_words))

    # most frequent letters
    letters_dict= Counter(merged_text.lower())
    # deleting space counts
    del letters_dict['' '']
    top_letter= letters_dict.most_common(4)
    print('Top 3 most common words are: {}'.format(','.join('{}'.format(value[0]) for value in top_letter)))
    # letters not used
    import string
    no_letter=[]
    for key in letters_dict.keys():
        if key.isalpha():
            if key not in list(string.ascii_lowercase[:]):
                no_letter.append(key)
    if len(no_letter)==0:
        print('Text contains all the letter from a to z')
    else:
        print('Letters not used in the document: {}'.format(no_letter))


    # most common first letter in a paragraph
    # indices of '\n' block
    #n_text= ''.join(text)
    #new_idx= [m.start() for m in re.finditer('\n\n',n_text)]
    #first_words=[]
    #for idx in new_idx:
    #    while n_text[idx+1]!= '\n':
    #        first_words.append(n_text[idx+10].split()[0])



