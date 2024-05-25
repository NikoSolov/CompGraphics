$vpr=[45,0,$t*360];
$vpt=[0,0,0];

color([1,1,1])
cube([1,1,1], center=true);
r=sin($t*360)*5;
g=sin($t*360-120)*5;
b=sin($t*360-240)*5;


//echo(cos($t*360)*5)
translate([r,0,0])
color([1,0,0])
cube([1,1,1], center=true);

translate([0,g,0])
color([0,1,0])
cube([1,1,1], center=true);

translate([0,0,b])
color([0,0,1])
cube([1,1,1], center=true);

translate([r,0,b])
color([1,0,1])
cube([1,1,1], center=true);

translate([0,g,b])
color([0,1,1])
cube([1,1,1], center=true);

translate([r,g,0])
color([1,1,0])
cube([1,1,1], center=true);