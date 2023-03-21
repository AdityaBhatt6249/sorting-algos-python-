class Notebook:
    def __init__(self,title,username,likes):
        self.title=title
        self.username=username
        self.likes=likes
    def __iter__(self):
        return 'notebook <{}/{}>{} likes'.format(self.username,self.title,self.likes)

    def compare_likes(nb1,nb2):
        if nb1.likes>nb2.likes:
            return 'lesser'
        elif nb1.likes==nb2.likes:
            return 'equal'
        else:
            return 'greater'

    def merge_sort(nums,compare=compare_likes):
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        return merge(merge_sort(nums[:mid],compare),merge_sort(nums[mid:],compare))

    def merge(left,right,compare):
        i,j,merged=0,0,[]
        while i<len(left) and j<len(right):
            result=compare(left,right)
            if result=='lesser' or result=='equal':
                merged.append(left[i])
                i+=1
            else:
                merged.append(right[j])
                j+=1

        return merged +left[i:]+right[j:]
