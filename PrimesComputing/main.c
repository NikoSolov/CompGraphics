#include <stdio.h>

int n=2, i, flag=1;

int main(){
	while (n<1000000){
	    flag=1;
		for (i=2; i<n; i++){
			if (i%n==0) {flag=0; i=n;}
		}
		if (flag==1) {printf("%d\n", n);}
		n++;
	}
	return 0;
}
