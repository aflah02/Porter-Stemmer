class PorterStemmer:
    vowels = ['a', 'e', 'i', 'o', 'u']
    def __init__(self):
        pass

    def StarX(self, word, X):
        if (word[-1] == X):
            return True
        return False

    def StarVStar(self, word):
        for i in word:
            if i in self.vowels:
                return True
        return False

    def StarD(self, word):
        if (word[-1] == word[-2] and word[-1] not in self.vowels):
            return True
        return False

    def StarO(self, word):
        if (word[-1] not in ['w', 'x', 'y'] and word[-1] not in self.vowels and word[-2] in self.vowels and word[-3] not in self.vowels):
            return True
        return False

    def Step1a(self, word):
        if word.endswith('sses'):
            return word[:-2] + 'ss'
        elif word.endswith('ies'):
            return word[:-2] + 'i'
        elif word.endswith('ss'):
            return word
        elif word.endswith('s'):
            return word[:-1]
        return word

    def Step1b(self, word, m):
        flag = False
        if (m > 0 and word.endswith('eed')):
            return word[:-3] + 'ee'
        elif (self.StarVStar(word) and word.endswith('ed')):
            word = word[:-2]
            flag = True
        elif (self.StarVStar(word) and word.endswith('ing')):
            word = word[:-3]
            flag = True
        if (flag):
            if (word.endswith('at') or word.endswith('bl') or word.endswith('iz')):
                return word + 'e'
            if (self.StarD(word) and not (self.StarX(word, 'l') or self.StarX(word, 's') or self.StarX(word, 'z'))):
                return word[:-1]
            if (m == 1 and self.StarO(word)):
                return word + 'e'
        return word

    def Step1c(self, word):
        if (self.StarVStar(word) and word.endswith('y')):
            return word[:-1] + 'i'
        return word

    def Step2(self, word, m):
        if (m <= 0):
            return word
        if (word.endswith('ational')):
            return word[:-7] + 'ate'
        elif (word.endswith('tional')):
            return word[:-6] + 'tion'
        elif (word.endswith('enci')):
            return word[:-4] + 'ence'
        elif (word.endswith('anci')):
            return word[:-4] + 'ance'
        elif (word.endswith('izer')):
            return word[:-4] + 'ize'
        elif (word.endswith('abli')):
            return word[:-4] + 'able'
        elif (word.endswith('alli')):
            return word[:-4] + 'al'
        elif (word.endswith('entli')):
            return word[:-5] + 'ent'
        elif (word.endswith('eli')):
            return word[:-3] + 'e'
        elif (word.endswith('ousli')):
            return word[:-5] + 'ous'
        elif (word.endswith('ization')):
            return word[:-7] + 'ize'
        elif (word.endswith('ation')):
            return word[:-5] + 'ate'
        elif (word.endswith('ator')):
            return word[:-5] + 'ate'
        elif (word.endswith('alism')):
            return word[:-5] + 'al'
        elif (word.endswith('iveness')):
            return word[:-7] + 'ive'
        elif (word.endswith('fulness')):
            return word[:-7] + 'ful'
        elif (word.endswith('ousness')):
            return word[:-7] + 'ous'
        elif (word.endswith('aliti')):
            return word[:-5] + 'al'
        elif (word.endswith('iviti')):
            return word[:-5] + 'ive'
        elif (word.endswith('biliti')):
            return word[:-6] + 'ble'
        return word

    def Step3(self, word, m):
        if (m <= 0):
            return word
        if (word.endswith('icate')):
            return word[:-4] + 'ic'
        elif (word.endswith('ative')):
            return word[:-5]
        elif (word.endswith('alize')):
            return word[:-4] + 'al'
        elif (word.endswith('iciti')):
            return word[:-4] + 'ic'
        elif (word.endswith('ical')):
            return word[:-4] + 'ic'
        elif (word.endswith('ful')):
            return word[:-3]
        elif (word.endswith('ness')):
            return word[:-4]
        return word

    def Step4(self, word, m):
        if (m <= 1):
            return word
        if (word.endswith('al')):
            return word[:-2]
        if (word.endswith('ance')):
            return word[:-4]
        if (word.endswith('ence')):
            return word[:-4]
        if (word.endswith('er')):
            return word[:-2]
        if (word.endswith('ic')):
            return word[:-2]
        if (word.endswith('able')):
            return word[:-4]
        if (word.endswith('ible')):
            return word[:-4]
        if (word.endswith('ant')):
            return word[:-3]
        if (word.endswith('ement')):
            return word[:-5]
        if (word.endswith('ment')):
            return word[:-4]
        if (word.endswith('ent')):
            return word[:-3]
        if (word.endswith('ion') and self.StarX(word, 's') and self.StarX(word, 't')):
            return word[:-3]
        if (word.endswith('ou')):
            return word[:-2]
        if (word.endswith('ism')):
            return word[:-3]
        if (word.endswith('ate')):
            return word[:-3]
        if (word.endswith('iti')):
            return word[:-3]
        if (word.endswith('ous')):
            return word[:-3]
        if (word.endswith('ive')):
            return word[:-3]
        if (word.endswith('ize')):
            return word[:-3]
        return word

    def Step5a(self, word, m):
        if (m > 1 and word[-1] == 'e'):
            return word[:-1]
        if (m == 1 and not self.StarO(word) and word[-1] == 'e'):
            return word[:-1]
        return word

    def Step5b(self, word, m):
        if (m > 1 and self.StarD(word) and self.StarX(word, 'l')):
            return word[:-1]
        return word

    def stem(self, word):
        word = word.lower()
        wordLen = len(word)
        if wordLen <= 2:
            return word
        startPointer = 0
        while (startPointer < wordLen and word[startPointer] not in self.vowels):
            startPointer += 1
        endPointer = wordLen - 1
        while (endPointer >= 0 and word[endPointer] in self.vowels):
            endPointer -= 1
        if (endPointer <= startPointer):
            return word
        midWord = word[startPointer:endPointer + 1]
        midWordPointer = 0
        VCString = "V"
        while (midWordPointer < len(midWord)):
            if (midWord[midWordPointer] in self.vowels):
                if VCString[-1] != 'V':
                    VCString += "V"
            else:
                if VCString[-1] != 'C':
                    VCString += "C"
            midWordPointer += 1
        m = len(VCString)/2
        word = self.Step1a(word)
        word = self.Step1b(word, m)
        word = self.Step1c(word)
        word = self.Step2(word, m)
        word = self.Step3(word, m)
        word = self.Step4(word, m)
        word = self.Step5a(word, m)
        word = self.Step5b(word, m)
        return word

if __name__ == "__main__":
    ps = PorterStemmer()
    print(ps.stem("bowdlerize"))