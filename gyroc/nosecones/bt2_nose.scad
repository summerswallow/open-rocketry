$fn=200;


difference() {
	union() {
		difference() {
			intersection() {
				scale(v = [1, 1, 4.6195652174]) {
					sphere(r = 3.5687000000);
				}
				cylinder(h = 16.4858423913, r = 3.5687000000);
			}
			intersection() {
				scale(v = [1, 1, 7.5198578595]) {
					sphere(r = 1.9812000000);
				}
				cylinder(h = 14.8983423913, r = 1.9812000000);
			}
		}
		translate(v = [0, 0, -6.3500000000]) {
			cylinder(h = 6.3500000000, r = 3.2385000000);
		}
	}
	translate(v = [0, 0, -4.7625000000]) {
		cylinder(h = 4.7625000000, r = 1.6510000000);
	}
}