$fn=200;


difference() {
	union() {
		difference() {
			intersection() {
				scale(v = [1, 1, 4.6195652174]) {
					sphere(r = 9.3472000000);
				}
				cylinder(h = 43.1800000000, r = 9.3472000000);
			}
			intersection() {
				scale(v = [1, 1, 5.3600654664]) {
					sphere(r = 7.7597000000);
				}
				cylinder(h = 41.5925000000, r = 7.7597000000);
			}
		}
		translate(v = [0, 0, -12.7000000000]) {
			cylinder(h = 12.7000000000, r = 9.0043000000);
		}
	}
	translate(v = [0, 0, -11.1125000000]) {
		cylinder(h = 11.1125000000, r = 7.4168000000);
	}
}