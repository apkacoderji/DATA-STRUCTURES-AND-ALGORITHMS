class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        freq = {
            "b":1,
            "a":1,
            "l":2,
            "o":2,
            "n":1
        }


        t_freq = {}
        #hashtable of text
        for i in range(len(text)):
            if text[i] in t_freq:
                t_freq[text[i]] += 1
            else:
                t_freq[text[i]] = 1

        result = float('inf')
        for i in freq:
            need = freq.get(i,0)
            have = t_freq.get(i,0)
            times = have / need
            result = min(result,times)
        
        return result

