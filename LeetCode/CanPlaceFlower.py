class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                if i==0:
                    if flowerbed[i+1]==0:
                        flowerbed[i]=1
                        k+=1
                   
                elif i==len(flowerbed)-1:
                    if flowerbed[i-1]==0:
                        flowerbed[i]=1
                        k+=1
                else:
                    if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                        flowerbed[i]=1
                        k+=1           

        if k==n:
            return True
        else:
            return False

        
