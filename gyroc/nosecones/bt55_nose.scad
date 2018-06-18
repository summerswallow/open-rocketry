$fn=200;


difference() {
	union() {
		difference() {
			intersection() {
				scale(v = [1, 1, 4.6195652174]) {
					sphere(r = 16.8275000000);
				}
				cylinder(h = 77.7357336957, r = 16.8275000000);
			}
			intersection() {
				scale(v = [1, 1, 4.9966032609]) {
					sphere(r = 15.2400000000);
				}
				cylinder(h = 76.1482336957, r = 15.2400000000);
			}
		}
		translate(v = [0, 0, -19.0500000000]) {
			cylinder(h = 19.0500000000, r = 16.2941000000);
		}
	}
	translate(v = [0, 0, -17.4625000000]) {
		cylinder(h = 17.4625000000, r = 14.7066000000);
	}
}