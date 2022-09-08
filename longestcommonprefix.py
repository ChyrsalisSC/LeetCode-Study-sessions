def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        out = ""
        for i in range(len(strs[0])):
            let = strs[0][i]
      
            for j in range(len(strs)):
                if len(strs[j]) <= i:
                    print(i)
                    print(strs[j])
                    return out
                
                if strs[j][i] != let:
                    return out
            
            out += let
        return out

    
print(longestCommonPrefix(["ab", "a"]))
