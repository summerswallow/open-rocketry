$fn=200;


difference() {
	union() {
		difference() {
			intersection() {
				scale(v = [1, 1, 4.6195652174]) {
					sphere(r = 9.7409000000);
				}
				cylinder(h = 44.9987228261, r = 9.7409000000);
			}
			intersection() {
				scale(v = [1, 1, 5.3243092239]) {
					sphere(r = 8.1534000000);
				}
				cylinder(h = 43.4112228261, r = 8.1534000000);
			}
		}
		translate(v = [0, 0, -14.2875000000]) {
			cylinder(h = 14.2875000000, r = 9.2075000000);
		}
	}
	translate(v = [0, 0, -12.7000000000]) {
		cylinder(h = 12.7000000000, r = 7.6200000000);
	}
}