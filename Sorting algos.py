def bubble_sort(nums):
    nums=list(nums)

    for j in range (len(nums)-1):
        for i in range (len(nums)-1):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]

    return nums

def insertion_sort(nums):
    nums=list(nums)

    for i in range(1,len(nums)):
        cur=nums.pop(i)
        j=i-1
        while j>=0 and nums[j]>cur:
            j-=1
        nums.insert(j+1,cur)

    return nums

def merge_sort(nums):
     if len(nums)<=1:
         return nums

     mid=len(nums)//2
     left=nums[:mid]
     right=nums[mid:]

     left_sorted,right_sorted=merge_sort(left),merge_sort(right)

     sorted_nums=merge(left_sorted,right_sorted)

     return sorted_nums

def merge(nums1,nums2):
    merged=[]
    i,j=0,0

    while i in len(nums1) and j in len(nums2):
        if nums1[i]<nums2[j]:
            merged.append(nums1[i])
            i+=1
        else:
            merged.append(nums2[j])
            j+=1

    nums1_tail=nums1[i:]
    nums2_tail=nums2[j:]

    return merged + nums1_tail +nums2_tail

def quick_sort(nums, start=0,end=None):

    if end is None:
        nums=list(nums)
        end=len(nums)-1

    if start <end:
        pivot=partition(nums,start,end)
        quick_sort(nums,start,pivot-1)
        quick_sort(nums,pivot+1,end)

    return nums

def partition(nums,start=0,end=None):
    if end is None:
        end =len(nums)-1

    l,r=start,end-1

    while l<r:
        if nums[l]<=nums[end]:
            l+=1
        elif nums[r]>nums[end]:
            r-=1
        else:
            nums[l],nums[r]=nums[r],nums[l]

    if nums[l]>nums[end]:
        nums[l],nums[end]=nums[end],nums[l]
        return l
    else:
        return end

