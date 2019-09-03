import argparse
import random
import json

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--add-text-file', action='store', help='Add text file to the vocabulary')
parser.add_argument('-f', '--flush', default=False, action='store_true', help='Clear vocabulary')
parser.add_argument('-g', '--generate', help='Generate new text')
parser.add_argument('-l', '--length', help='The length of file in words')
args = parser.parse_args()


class Textgen:
    def __init__(self):
        try:
            with open('dict.txt', 'r') as dict_file:
                self.dic = json.loads(dict_file.read())
        except:
            self.dic = {}
        try:
            with open('doted.txt', 'r') as doted_file:
                self._doted = json.loads(doted_file.read())
        except:
            self._doted = []

    def learn(self, file_name):
        file = open(file_name, 'r')
        word = ''
        prev_word = ''
        for i in file.read():
            if (ord(i) < 65 or 90 < ord(i) < 97 or ord(i) > 122) and i not in '/-"\'':
                if word != '':
                    if ord(i) == 46 and word not in self._doted:
                        self._doted.append(word)
                    try:
                        self.dic[prev_word].append(word)
                    except KeyError:
                        self.dic[prev_word] = [word]
                    prev_word = word
                    word = ''
            else:
                word += i.lower()
        self.dic[prev_word] = self.dic.pop('')
        with open('dict.txt', 'w') as dict_file:
            json.dump(self.dic, dict_file)
        with open('doted.txt', 'w') as doted_file:
            json.dump(self._doted, doted_file)
        file.close()

    def generate(self, key_word, sentence_length, seed=0):
        random.seed(seed)
        choice = random.choice(self.dic[key_word])
        next_is_capital = 0
        res_text = key_word[0].upper() + key_word[1:]
        for i in range(int(sentence_length) - 1):
            if next_is_capital:
                res_text += ' ' + choice[0].upper() + choice[1:]
                next_is_capital = 0
            else:
                res_text += ' ' + choice
            if choice in self._doted:
                dot = random.choice(('.', ''))
                res_text += dot
                if dot == '.':
                    next_is_capital = 1
            choice = random.choice(self.dic[choice])
        return res_text


if __name__ == '__main__':
    tg = Textgen()
    if args.add_text_file:
        tg.learn(args.add_text_file)
    if args.generate:
        if args.length:
            length = args.length
        else:
            length = 20
        text = tg.generate(args.generate.lower(), length, 109)
        if text[-1] != '.':
            text += '...'
        print(text)

    if args.flush:
        file = open('dict.txt', 'w')
        file.close()
