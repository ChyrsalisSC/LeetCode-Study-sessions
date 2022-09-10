def isHappy(n):
        """
        :type n: int
        :rtype: bool
        """
        x = 0
        save = []
        while(True):
            n = str(n)
            for i in n:
                print(i)
            
                x += int(i)**2
                print(x)

            if x == 1:
                return True
            if x in save:
                return False

            save.append(x)
            n = x
            x = 0


            
print(isHappy(20))
