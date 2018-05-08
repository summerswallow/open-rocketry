$fn=100;


union() {
	translate(v = [0.0000000000, 0.0000000000, 0]) {
		union() {
			difference() {
				difference() {
					intersection() {
						scale(v = [1, 1, 2.7624309392]) {
							sphere(r = 6.8961000000);
						}
						cylinder(h = 19.0500000000, r = 6.8961000000);
					}
					intersection() {
						scale(v = [1, 1, 3.2894736842]) {
							sphere(r = 5.3086000000);
						}
						cylinder(h = 17.4625000000, r = 5.3086000000);
					}
				}
				translate(v = [0, 0, 35.5600000000]) {
					sphere(r = 25.4000000000);
				}
			}
			intersection() {
				hull() {
					difference() {
						intersection() {
							scale(v = [1, 1, 2.7624309392]) {
								sphere(r = 6.8961000000);
							}
							cylinder(h = 19.0500000000, r = 6.8961000000);
						}
						intersection() {
							scale(v = [1, 1, 3.2894736842]) {
								sphere(r = 5.3086000000);
							}
							cylinder(h = 17.4625000000, r = 5.3086000000);
						}
					}
				}
				translate(v = [0, 0, 35.5600000000]) {
					difference() {
						sphere(r = 26.9875000000);
						sphere(r = 25.4000000000);
					}
				}
			}
		}
	}
	translate(v = [25.4000000000, 0.0000000000, 0]) {
		union() {
			difference() {
				difference() {
					intersection() {
						scale(v = [1, 1, 2.7624309392]) {
							sphere(r = 6.8961000000);
						}
						cylinder(h = 19.0500000000, r = 6.8961000000);
					}
					intersection() {
						scale(v = [1, 1, 3.2894736842]) {
							sphere(r = 5.3086000000);
						}
						cylinder(h = 17.4625000000, r = 5.3086000000);
					}
				}
				translate(v = [0, 0, 29.2100000000]) {
					sphere(r = 19.0500000000);
				}
			}
			intersection() {
				hull() {
					difference() {
						intersection() {
							scale(v = [1, 1, 2.7624309392]) {
								sphere(r = 6.8961000000);
							}
							cylinder(h = 19.0500000000, r = 6.8961000000);
						}
						intersection() {
							scale(v = [1, 1, 3.2894736842]) {
								sphere(r = 5.3086000000);
							}
							cylinder(h = 17.4625000000, r = 5.3086000000);
						}
					}
				}
				translate(v = [0, 0, 29.2100000000]) {
					difference() {
						sphere(r = 20.6375000000);
						sphere(r = 19.0500000000);
					}
				}
			}
		}
	}
	translate(v = [0.0000000000, 25.4000000000, 0]) {
		union() {
			difference() {
				difference() {
					intersection() {
						scale(v = [1, 1, 2.7624309392]) {
							sphere(r = 6.8961000000);
						}
						cylinder(h = 19.0500000000, r = 6.8961000000);
					}
					intersection() {
						scale(v = [1, 1, 3.2894736842]) {
							sphere(r = 5.3086000000);
						}
						cylinder(h = 17.4625000000, r = 5.3086000000);
					}
				}
				translate(v = [0, 0, 22.8600000000]) {
					sphere(r = 12.7000000000);
				}
			}
			intersection() {
				hull() {
					difference() {
						intersection() {
							scale(v = [1, 1, 2.7624309392]) {
								sphere(r = 6.8961000000);
							}
							cylinder(h = 19.0500000000, r = 6.8961000000);
						}
						intersection() {
							scale(v = [1, 1, 3.2894736842]) {
								sphere(r = 5.3086000000);
							}
							cylinder(h = 17.4625000000, r = 5.3086000000);
						}
					}
				}
				translate(v = [0, 0, 22.8600000000]) {
					difference() {
						sphere(r = 14.2875000000);
						sphere(r = 12.7000000000);
					}
				}
			}
		}
	}
	translate(v = [25.4000000000, 25.4000000000, 0]) {
		union() {
			union() {
				difference() {
					difference() {
						intersection() {
							scale(v = [1, 1, 2.7624309392]) {
								sphere(r = 6.8961000000);
							}
							cylinder(h = 19.0500000000, r = 6.8961000000);
						}
						intersection() {
							scale(v = [1, 1, 3.2894736842]) {
								sphere(r = 5.3086000000);
							}
							cylinder(h = 17.4625000000, r = 5.3086000000);
						}
					}
					translate(v = [0, 0, 35.5600000000]) {
						sphere(r = 25.4000000000);
					}
				}
				intersection() {
					hull() {
						difference() {
							intersection() {
								scale(v = [1, 1, 2.7624309392]) {
									sphere(r = 6.8961000000);
								}
								cylinder(h = 19.0500000000, r = 6.8961000000);
							}
							intersection() {
								scale(v = [1, 1, 3.2894736842]) {
									sphere(r = 5.3086000000);
								}
								cylinder(h = 17.4625000000, r = 5.3086000000);
							}
						}
					}
					translate(v = [0, 0, 35.5600000000]) {
						difference() {
							sphere(r = 26.9875000000);
							sphere(r = 25.4000000000);
						}
					}
				}
			}
			translate(v = [0, 0, 10.1600000000]) {
				cylinder(h = 10.1600000000, r1 = 3.1750000000, r2 = 0);
			}
		}
	}
	translate(v = [0.0000000000, 50.8000000000, 0]) {
		union() {
			union() {
				difference() {
					difference() {
						cylinder(h = 19.0500000000, r1 = 6.8961000000, r2 = 0);
						cylinder(h = 17.4625000000, r1 = 5.3086000000, r2 = 0);
					}
					translate(v = [0, 0, 30.4800000000]) {
						sphere(r = 25.4000000000);
					}
				}
				intersection() {
					hull() {
						difference() {
							cylinder(h = 19.0500000000, r1 = 6.8961000000, r2 = 0);
							cylinder(h = 17.4625000000, r1 = 5.3086000000, r2 = 0);
						}
					}
					translate(v = [0, 0, 30.4800000000]) {
						difference() {
							sphere(r = 26.9875000000);
							sphere(r = 25.4000000000);
						}
					}
				}
			}
			translate(v = [0, 0, 5.0800000000]) {
				cylinder(h = 10.1600000000, r1 = 3.1750000000, r2 = 0);
			}
		}
	}
	translate(v = [25.4000000000, 50.8000000000, 0]) {
		union() {
			union() {
				difference() {
					rotate_extrude() {
						difference() {
							intersection() {
								translate(v = [-22.8641046961, 0]) {
									circle(r = 29.7602046961);
								}
								square(size = [6.8961000000, 19.0500000000]);
							}
							intersection() {
								translate(v = [-26.0669171053, 0]) {
									circle(r = 31.3755171053);
								}
								square(size = [5.3086000000, 17.4625000000]);
							}
						}
					}
					translate(v = [0, 0, 35.5600000000]) {
						sphere(r = 25.4000000000);
					}
				}
				intersection() {
					hull() {
						rotate_extrude() {
							difference() {
								intersection() {
									translate(v = [-22.8641046961, 0]) {
										circle(r = 29.7602046961);
									}
									square(size = [6.8961000000, 19.0500000000]);
								}
								intersection() {
									translate(v = [-26.0669171053, 0]) {
										circle(r = 31.3755171053);
									}
									square(size = [5.3086000000, 17.4625000000]);
								}
							}
						}
					}
					translate(v = [0, 0, 35.5600000000]) {
						difference() {
							sphere(r = 26.9875000000);
							sphere(r = 25.4000000000);
						}
					}
				}
			}
			translate(v = [0, 0, 10.1600000000]) {
				cylinder(h = 10.1600000000, r1 = 3.1750000000, r2 = 0);
			}
		}
	}
}