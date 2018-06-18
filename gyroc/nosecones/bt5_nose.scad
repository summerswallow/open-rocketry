$fn=200;


difference() {
	union() {
		difference() {
			intersection() {
				scale(v = [1, 1, 4.6195652174]) {
					sphere(r = 6.8961000000);
				}
				cylinder(h = 31.8569836957, r = 6.8961000000);
			}
			intersection() {
				scale(v = [1, 1, 5.7019710838]) {
					sphere(r = 5.3086000000);
				}
				cylinder(h = 30.2694836957, r = 5.3086000000);
			}
		}
		translate(v = [0, 0, -9.5250000000]) {
			cylinder(h = 9.5250000000, r = 6.5405000000);
		}
	}
	translate(v = [0, 0, -7.9375000000]) {
		cylinder(h = 7.9375000000, r = 4.9530000000);
	}
}