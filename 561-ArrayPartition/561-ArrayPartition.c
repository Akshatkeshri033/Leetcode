// Last updated: 7/4/2026, 7:02:41 PM
 void print_Array(int *A,int size)
{
    for(int i=0;i<size;i++)
    {
        printf("%d ",A[i]);
    }
    printf("\n");
}
void merge(int *A,int l,int m,int h)
{
	int i=l,j=m+1,k=0;
	int result[h-l+1];
	while(i<=m && j<=h)
	{
		if(A[i]<A[j])
		{
			result[k]=A[i];
			i++;
			k++;
		}
		else 
		{
			result[k]=A[j];
			j++;
			k++;
		}
	}
	while(i<=m)
	{
		result[k]=A[i];
		i++;
		k++;
	}
	while(j<=h)
	{
		result[k]=A[j];
		j++;
		k++;
	}
	k=0;
	for(i=l;i<=h;i++)
	{
		A[i]=result[k];
		k++;
	}
}
void merge_sort(int *A,int l,int h)
{
	if(l<h)
	{
		int m=(l+h)/2;
		merge_sort(A,l,m);
		merge_sort(A,m+1,h);
		merge(A,l,m,h);	
	}
}
int arrayPairSum(int* nums, int numsSize) {
    int count=0,max=0;
    merge_sort(nums,0,numsSize-1);
    //  print_Array(nums,numsSize);
    //  return 0;
     for(int i=0;i<numsSize-1;i+=2)
    {
        if(nums[i]<=nums[i+1])
        count+=nums[i];
        else count+=nums[i+1];
    }
    return count;
}