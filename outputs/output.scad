// Crescent Wrench with Notched Handle

module crescent_wrench() {
    handle();
    head();
}

module handle() {
    difference() {
        union() {
            // Main handle
            translate([0, 0, 0])
                cube([150, 20, 10]);
            // Notch in handle
            translate([50, 5, 0])
                cube([10, 10, 10]);
        }
    }
}

module head() {
    translate([150, 0, 0])
        union() {
            // Fixed jaw
            translate([0, 0, 0])
                cube([20, 20, 10]);
            // Movable jaw
            translate([0, 10, 0])
                cube([10, 10, 10]);
            // Adjustment mechanism
            translate([10, 5, 0])
                cylinder(h=10, r=2, $fn=50);
        }
}

crescent_wrench();