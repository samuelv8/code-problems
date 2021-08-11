'''Verifying an Alien Dictionary'''

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            for j in range(min(len(w1), len(w2))):
                equal = False
                o1 = order.find(w1[j])
                o2 = order.find(w2[j])
                if o1 > o2:
                    return False
                if o1 < o2:
                    break
                equal = True
            if equal and len(w1) > len(w2):
                return False
        return True
