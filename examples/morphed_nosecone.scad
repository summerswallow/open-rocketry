$fn=100;


union() {
	translate(v = [0.0000000000, 0.0000000000, 0]) {
		difference() {
			hull() {
				union() {
					scale(v = [1, 1, 0]) {
						cylinder(h = 0.0010000000, r = 6.8961000000);
					}
					translate(v = [0, 0, 19.0500000000]) {
						scale(v = 1) {
							scale(v = [1, 1, 0]) {
								linear_extrude() {
									square(center = true, size = [9.7525581475, 9.7525581475]);
								}
							}
						}
					}
				}
			}
			hull() {
				union() {
					scale(v = [1, 1, 0]) {
						cylinder(h = 0.0010000000, r = 5.3086000000);
					}
					translate(v = [0, 0, 17.4625000000]) {
						scale(v = 0.7697974217) {
							scale(v = [1, 1, 0]) {
								linear_extrude() {
									square(center = true, size = [9.7525581475, 9.7525581475]);
								}
							}
						}
					}
				}
			}
		}
	}
	translate(v = [25.4000000000, 0.0000000000, 0]) {
		difference() {
			hull() {
				union() {
					scale(v = [1, 1, 0]) {
						cylinder(h = 0.0010000000, r = 6.8961000000);
					}
					translate(v = [0, 0, 19.0500000000]) {
						scale(v = 1) {
							scale(v = [1, 1, 0]) {
								linear_extrude() {
									square(center = true, size = [2.5400000000, 6.3500000000]);
								}
							}
						}
					}
				}
			}
			hull() {
				union() {
					scale(v = [1, 1, 0]) {
						cylinder(h = 0.0010000000, r = 5.3086000000);
					}
					translate(v = [0, 0, 17.4625000000]) {
						scale(v = 0.7697974217) {
							scale(v = [1, 1, 0]) {
								linear_extrude() {
									square(center = true, size = [2.5400000000, 6.3500000000]);
								}
							}
						}
					}
				}
			}
		}
	}
	translate(v = [0.0000000000, 25.4000000000, 0]) {
		difference() {
			hull() {
				union() {
					scale(v = [1, 1, 0]) {
						cylinder(h = 0.0010000000, r = 6.8961000000);
					}
					translate(v = [0, 0, 19.0500000000]) {
						scale(v = 1) {
							scale(v = [1, 1, 0]) {
								linear_extrude() {
									scale(v = [2.0000000000, 1]) {
										circle(r = 3.4480500000);
									}
								}
							}
						}
					}
				}
			}
			hull() {
				union() {
					scale(v = [1, 1, 0]) {
						cylinder(h = 0.0010000000, r = 5.3086000000);
					}
					translate(v = [0, 0, 17.4625000000]) {
						scale(v = 0.7697974217) {
							scale(v = [1, 1, 0]) {
								linear_extrude() {
									scale(v = [2.0000000000, 1]) {
										circle(r = 3.4480500000);
									}
								}
							}
						}
					}
				}
			}
		}
	}
	translate(v = [25.4000000000, 25.4000000000, 0]) {
		union() {
			difference() {
				hull() {
					union() {
						scale(v = [1, 1, 0]) {
							cylinder(h = 0.0010000000, r = 6.8961000000);
						}
						translate(v = [0, 0, 19.0500000000]) {
							scale(v = 1) {
								scale(v = [1, 1, 0]) {
									linear_extrude() {
										polygon(paths = [[0, 1, 2, 3]], points = [[0, 0], [1.3947655237, -1.0133564696], [3.4480500000, 0.0000000000], [1.3947655237, 1.0133564696]]);
									}
								}
							}
						}
					}
				}
				hull() {
					union() {
						scale(v = [1, 1, 0]) {
							cylinder(h = 0.0010000000, r = 5.3086000000);
						}
						translate(v = [0, 0, 17.4625000000]) {
							scale(v = 0.7697974217) {
								scale(v = [1, 1, 0]) {
									linear_extrude() {
										polygon(paths = [[0, 1, 2, 3]], points = [[0, 0], [1.3947655237, -1.0133564696], [3.4480500000, 0.0000000000], [1.3947655237, 1.0133564696]]);
									}
								}
							}
						}
					}
				}
			}
			difference() {
				hull() {
					union() {
						scale(v = [1, 1, 0]) {
							cylinder(h = 0.0010000000, r = 6.8961000000);
						}
						translate(v = [0, 0, 19.0500000000]) {
							scale(v = 1) {
								scale(v = [1, 1, 0]) {
									linear_extrude() {
										polygon(paths = [[0, 1, 2, 3]], points = [[0, 0], [1.3947655237, 1.0133564696], [1.0655060475, 3.2792904210], [-0.5327530237, 1.6396452105]]);
									}
								}
							}
						}
					}
				}
				hull() {
					union() {
						scale(v = [1, 1, 0]) {
							cylinder(h = 0.0010000000, r = 5.3086000000);
						}
						translate(v = [0, 0, 17.4625000000]) {
							scale(v = 0.7697974217) {
								scale(v = [1, 1, 0]) {
									linear_extrude() {
										polygon(paths = [[0, 1, 2, 3]], points = [[0, 0], [1.3947655237, 1.0133564696], [1.0655060475, 3.2792904210], [-0.5327530237, 1.6396452105]]);
									}
								}
							}
						}
					}
				}
			}
			difference() {
				hull() {
					union() {
						scale(v = [1, 1, 0]) {
							cylinder(h = 0.0010000000, r = 6.8961000000);
						}
						translate(v = [0, 0, 19.0500000000]) {
							scale(v = 1) {
								scale(v = [1, 1, 0]) {
									linear_extrude() {
										polygon(paths = [[0, 1, 2, 3]], points = [[0, 0], [-0.5327530237, 1.6396452105], [-2.7895310475, 2.0267129392], [-1.7240250000, 0.0000000000]]);
									}
								}
							}
						}
					}
				}
				hull() {
					union() {
						scale(v = [1, 1, 0]) {
							cylinder(h = 0.0010000000, r = 5.3086000000);
						}
						translate(v = [0, 0, 17.4625000000]) {
							scale(v = 0.7697974217) {
								scale(v = [1, 1, 0]) {
									linear_extrude() {
										polygon(paths = [[0, 1, 2, 3]], points = [[0, 0], [-0.5327530237, 1.6396452105], [-2.7895310475, 2.0267129392], [-1.7240250000, 0.0000000000]]);
									}
								}
							}
						}
					}
				}
			}
			difference() {
				hull() {
					union() {
						scale(v = [1, 1, 0]) {
							cylinder(h = 0.0010000000, r = 6.8961000000);
						}
						translate(v = [0, 0, 19.0500000000]) {
							scale(v = 1) {
								scale(v = [1, 1, 0]) {
									linear_extrude() {
										polygon(paths = [[0, 1, 2, 3]], points = [[0, 0], [-1.7240250000, 0.0000000000], [-2.7895310475, -2.0267129392], [-0.5327530237, -1.6396452105]]);
									}
								}
							}
						}
					}
				}
				hull() {
					union() {
						scale(v = [1, 1, 0]) {
							cylinder(h = 0.0010000000, r = 5.3086000000);
						}
						translate(v = [0, 0, 17.4625000000]) {
							scale(v = 0.7697974217) {
								scale(v = [1, 1, 0]) {
									linear_extrude() {
										polygon(paths = [[0, 1, 2, 3]], points = [[0, 0], [-1.7240250000, 0.0000000000], [-2.7895310475, -2.0267129392], [-0.5327530237, -1.6396452105]]);
									}
								}
							}
						}
					}
				}
			}
			difference() {
				hull() {
					union() {
						scale(v = [1, 1, 0]) {
							cylinder(h = 0.0010000000, r = 6.8961000000);
						}
						translate(v = [0, 0, 19.0500000000]) {
							scale(v = 1) {
								scale(v = [1, 1, 0]) {
									linear_extrude() {
										polygon(paths = [[0, 1, 2, 3]], points = [[0, 0], [-0.5327530237, -1.6396452105], [1.0655060475, -3.2792904210], [1.3947655237, -1.0133564696]]);
									}
								}
							}
						}
					}
				}
				hull() {
					union() {
						scale(v = [1, 1, 0]) {
							cylinder(h = 0.0010000000, r = 5.3086000000);
						}
						translate(v = [0, 0, 17.4625000000]) {
							scale(v = 0.7697974217) {
								scale(v = [1, 1, 0]) {
									linear_extrude() {
										polygon(paths = [[0, 1, 2, 3]], points = [[0, 0], [-0.5327530237, -1.6396452105], [1.0655060475, -3.2792904210], [1.3947655237, -1.0133564696]]);
									}
								}
							}
						}
					}
				}
			}
		}
	}
}