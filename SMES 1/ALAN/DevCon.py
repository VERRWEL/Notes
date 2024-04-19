def minmax(a, i, j):
    if (i == j):
        min = a[i]
        max = a[j]
    else:
        if(i == j-1):
            if(a[i]< a[j]):
                min = a[i]
                max = a[j]
            else:
                min = a[j]
                max = a[i]
        else:
            k = int((i+j)/2)
            min1,max1 = minmax(a,i,k)
            min2,max2 = minmax(a,k+1,j)

            if(min1 < min2):
                min = min1
            else:
                min = min2
            
            if(max1 > max2):
                max = max1
            else:
                max=max2
    return min,max



