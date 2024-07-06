#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//#include <sys/ioctl.h>

int main(){
    srand(time(NULL));
    struct winsize w;
    ioctl(0, TIOCGWINSZ, &w);

    int count=10, size=3;
    char arr[count*4];

    for (int i=0; i<count; i++){
    	arr[4*i]=rand()%(w.ws_col-size);
    	arr[4*i+1]=rand()%(w.ws_row-size);

        if (rand()%2){arr[4*i+2]=-1;}
        else {arr[4*i+2]=1;}
        if (rand()%2){arr[4*i+3]=-1;}
        else {arr[4*i+3]=1;} 
    }

//    printf("\033[0;0H\033[2JHi");

//    for (int i=0; i<count*4; i++){printf("%d\n", arr[i]);}
//    for (double i=0; i<1000000000; i++){}

	while (1){
//     printf("\033[2J\033[0;0H");
     printf("\033[2J");
//     fflush(stdout);
	 // draw 
	 for (int i=0; i<count; i++){

	  for (int y=0; y<size; y++){
	  printf("\033[%d;%dH", arr[4*i+1]+y, arr[4*i]);
      for (int x=0; x<size; x++){ printf("#"); }}
//	  fflush(stdout);	
	 }
	 fflush(stdout);
	 // update
	 for (int i=0; i<count; i++){
	  if (arr[4*i]<1 || arr[4*i]>w.ws_col-size-1){arr[4*i+2]*=-1;}
	  if (arr[4*i+1]<1 || arr[4*i+1]>w.ws_row-size-1){arr[4*i+3]*=-1;}
     
	  arr[4*i]+=arr[4*i+2];
	  arr[4*i+1]+=arr[4*i+3];
	 // wait
	 }
	 for (double i=0; i<100000000; i++){;}
	}
		
	return 0;
}
