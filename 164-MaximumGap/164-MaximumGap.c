// Last updated: 8/20/2025, 5:49:24 PM
 void merge(int *arr,int l,int m,int h){
	int i=l,j=m+1,k=0,B[h-l+1];
	while (i<=m && j<=h){
		if (arr[i]<=arr[j]){
			B[k]=arr[i];
			i++;
			k++;
		}
		else {
			B[k]=arr[j];
			j++;
			k++;
		}
	}
	while (i<=m){
		B[k]=arr[i];
		k++;
		i++;
	}
	while (j<=h){
		B[k]=arr[j];
		k++;
		j++;
	}
	k=0;
	for (int i=l;i<=h;i++){
		arr[i]=B[k];
		k++;
	}
}
void merge_sort(int *arr,int l,int h){
	if (l<h){
		int m=(l+h)/2;
		merge_sort(arr,l,m);
		merge_sort(arr,m+1,h);
		merge(arr,l,m,h);
	}
}
int maximumGap(int* arr, int a) {
    merge_sort(arr,0,a-1);
    int s=0;
    for (int i=0;i<a-1;i++){
        int d=arr[i+1]-arr[i];
        if (d>s){
            s=d;
        }
    }
    return s;

}