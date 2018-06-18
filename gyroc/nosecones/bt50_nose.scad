$fn=200;


difference() {
	union() {
		difference() {
			intersection() {
				scale(v = [1, 1, 4.6195652174]) {
					sphere(r = 12.3952000000);
				}
				cylinder(h = 57.2604347826, r = 12.3952000000);
			}
			intersection() {
				scale(v = [1, 1, 5.1512287335]) {
					sphere(r = 10.8077000000);
				}
				cylinder(h = 55.6729347826, r = 10.8077000000);
			}
		}
		translate(v = [0, 0, -15.8750000000]) {
			cylinder(h = 15.8750000000, r = 12.0650000000);
		}
	}
	translate(v = [0, 0, -14.2875000000]) {
		cylinder(h = 14.2875000000, r = 10.4775000000);
	}
}