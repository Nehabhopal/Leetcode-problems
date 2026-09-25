class Solution(object):
    def convertToBase7(self, num):
        if num==0:
            return "0"

        sign=""

        if num<0:
            sign="-"
            num=-num

        ans=[]

        while num>0:
            ans.append(str(num%7))
            num=num//7
        ans.reverse()

        return sign + "".join(ans)