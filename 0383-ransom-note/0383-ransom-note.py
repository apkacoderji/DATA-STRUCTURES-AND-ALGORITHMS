class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r_freq = {}
        #create a hashtable
        for i in range(len(ransomNote)):
            if ransomNote[i] in r_freq:
                r_freq[ransomNote[i]] += 1
            else:
                r_freq[ransomNote[i]] = 1
        
        
        m_freq = {}
        #create a hashtable
        for i in range(len(magazine)):
            if magazine[i] in m_freq:
                m_freq[magazine[i]] += 1
            else:
                m_freq[magazine[i]] = 1

        for i in range(len(ransomNote)):
            if ransomNote[i] in m_freq:
                if r_freq[ransomNote[i]] > m_freq[ransomNote[i]]:
                    return False
            else:
                return False
        
        return True


    
        