def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums
        
   
def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    N = sum(nums)
    left = 0
    for i in range(len(nums)):
        right = N - left - nums[i]
        if left == right:
            return i
        left = left + nums[i]
    return -1

def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        print(f"WORKING ON {strs}")
        prefix = ""
        dic = {}
        current = ""
        for word in strs:
          
        
            for letter in word:
                
                current += letter
                print(current)
                if current not in dic:
                    
                    dic[current] = 1
                else:
                    dic[current] +=1
                    #print(dic[current])
                
            current = ""


        if dic:
            longest = max(dic.values())
            #print()
            print(f"Longest {longest})")
            #if longest == 0:
                
                
                
            for key, value in dic.items():
                 if value == longest:
                     if len(key) > len(prefix):
                         prefix = key
                         print(prefix)
            print(f"Returning : {prefix}")
            return  prefix
        else:
            print(f"Returning NOTHING)")
            return ""

        
def isIsomorphic(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}
        
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] not in mapping.values():
                    mapping[s[i]] = t[i]
                else:
                    return False
            else:
                if t[i] != mapping[s[i]]:
                    return False
        return True
                    
                

                
print(isIsomorphic("badc", "baba"))
print(isIsomorphic("egg", "add"))
      
"""
print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix( ["dog","racecar","car"])) 
           
print(longestCommonPrefix( ["a"]))
print(longestCommonPrefix( ["", ""])) 
print(longestCommonPrefix( ["", "", "dog"])"""
#print(pivotIndex([1,2,3,1,2]))
#print(runningSum([1,2,3,4]))

