class Solution(object):
    def LegalWord(self,word):
        return word[:1].upper()+word[1:].lower()
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word==word.upper():
        	return True
        if word==word.lower():
        	return True
        if word==self.LegalWord(word):
        	return True
        return False


