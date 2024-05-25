


for (i=[0:1:100]){
 translate([i, sin(i*$t*100)*10,30+i^2/500])
 sphere(2);

}


for (i=[0:1:500]){
 angle=(i*10+$t*360);
 color(c=[i/500,i/500,i/500])
 translate([sin(i)*100, sin(angle)*10, cos(angle*2)*10])
 sphere(1);
}