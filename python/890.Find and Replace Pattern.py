class Solution:
    def findAndReplacePattern(self, words: 'List[str]', pattern: 'str') -> 'List[str]':
        ret = []
        for word in words:
            if len(word) != len(pattern):
                continue
            tag = 0
            dic = {}
            reverse_dic = {}
            for word_char, pattern_char in zip(word, pattern):
                if dic.get(pattern_char) == None and reverse_dic.get(word_char) == None:
                    dic[pattern_char] = word_char
                    reverse_dic[word_char] = pattern_char
                elif dic.get(pattern_char) != None and reverse_dic.get(word_char) != None:
                    if dic[pattern_char] != word_char or reverse_dic[word_char] != pattern_char:
                        tag = 1
                        break
                else:
                    tag = 1
                    break
            if tag == 1:
                continue
            ret.append(word)
        return ret

print(Solution().findAndReplacePattern(["abb"], "abb"))