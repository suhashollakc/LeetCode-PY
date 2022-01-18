class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        skip = 0
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if i+skip >= len(flowerbed):
                return False
            if flowerbed[i+skip] == 1:
                skip += 1
            elif i + skip + 1 >= len(flowerbed) or flowerbed[i + skip + 1] == 0:
                n += -1
                skip += 1
            if n == 0:
                return True

        return False