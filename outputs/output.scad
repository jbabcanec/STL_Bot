module dumbbell() {
    // Dumbbell bar
    difference() {
        cylinder(h=100, r=10, center=true);
        cylinder(h=110, r=8, center=true);
    }

    // Dumbbell weights
    translate([0, 0, -50]) {
        union() {
            translate([-20, 0, 0]) {
                cube([40, 40, 100]);
            }
            translate([-20, 0, 100]) {
                cylinder(h=20, r=20, center=true);
            }
        }
    }
}

dumbbell();