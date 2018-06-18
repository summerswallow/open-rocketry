use <threads.scad>
$fn=100;


union() {
	translate(v = [0.0000000000, 0.0000000000, 0]) {
		intersection() {
			difference() {
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
						cylinder(h = 1.5875000000, r = 19.6215000000);
					}
					translate(v = [0, 0, -12.7000000000]) {
						english_thread(diameter = 0.3900000000, length = 0.5625000000, threads_per_inch = 6);
					}
					hull() {
						intersection() {
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
							translate(v = [0, 0, 1.5875000000]) {
								cylinder(h = 1.5875000000, r = 20.6883000000);
							}
						}
					}
				}
				translate(v = [0, 0, -11.1125000000]) {
					cylinder(h = 14.2875000000, r = 1.2868257906);
				}
			}
			translate(v = [0, 32.8422000000, 0]) {
				cube(center = true, size = 65.6844000000);
			}
		}
	}
	translate(v = [25.4000000000, 0.0000000000, 0]) {
		intersection() {
			difference() {
				union() {
					union() {
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
						hull() {
							intersection() {
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
								translate(v = [0, 0, 0]) {
									cylinder(h = 0.0625000000, r = 20.6883000000);
								}
							}
						}
					}
					translate(v = [0, 0, -12.7000000000]) {
						english_thread(diameter = 0.3900000000, length = 0.5000000000, threads_per_inch = 6);
					}
				}
				translate(v = [0, 0, -11.1125000000]) {
					cylinder(h = 14.2875000000, r = 1.2868257906);
				}
			}
			translate(v = [0, 32.8422000000, 0]) {
				cube(center = true, size = 65.6844000000);
			}
		}
	}
	translate(v = [50.8000000000, 0.0000000000, 0]) {
		intersection() {
			difference() {
				union() {
					translate(v = [0, 0, -12.7000000000]) {
						cylinder(h = 12.7000000000, r = 6.5405000000);
					}
					hull() {
						intersection() {
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
							translate(v = [0, 0, 0]) {
								cylinder(h = 1.5875000000, r = 20.6883000000);
							}
						}
					}
				}
				translate(v = [0, 0, -12.7000000000]) {
					english_thread(diameter = 0.3900000000, internal = true, length = 0.5625000000, threads_per_inch = 6);
				}
			}
			translate(v = [0, 32.8422000000, 0]) {
				cube(center = true, size = 65.6844000000);
			}
		}
	}
	translate(v = [76.2000000000, 0.0000000000, 0]) {
		intersection() {
			union() {
				difference() {
					union() {
						difference() {
							union() {
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
								translate(v = [0, 0, -12.7000000000]) {
									cylinder(h = 12.7000000000, r = 6.5405000000);
								}
							}
							translate(v = [0, 0, -11.1125000000]) {
								cylinder(h = 11.1125000000, r = 4.9530000000);
							}
						}
						difference() {
							translate(v = [0, 0, -6.3500000000]) {
								cylinder(h = 1.5875000000, r = 6.5405000000);
							}
							translate(v = [-6.5405000000, -6.5405000000, -6.3500000000]) {
								cube(size = [7.5692000000, 13.0810000000, 6.3500000000]);
							}
						}
						intersection() {
							translate(v = [1.0287000000, -7.1859425784, -12.7000000000]) {
								cube(size = [1.5875000000, 14.3718851568, 6.3500000000]);
							}
							translate(v = [0, 0, -12.7000000000]) {
								cylinder(h = 12.7000000000, r = 6.5405000000);
							}
						}
					}
					translate(v = [2.6162000000, -6.5405000000, -13.7000000000]) {
						cube(size = [3.9243000000, 13.0810000000, 7.3500000000]);
					}
				}
				translate(v = [3.4099500000, 0, -6.3500000000]) {
					translate(v = [0, 0, -2.3812500000]) {
						rotate(a = [90, 0, 0, 0]) {
							rotate_extrude() {
								translate(v = [1.5875000000, 0, 0]) {
									circle(r = 0.7937500000);
								}
							}
						}
					}
				}
			}
			translate(v = [0, 32.8422000000, 0]) {
				cube(center = true, size = 65.6844000000);
			}
		}
	}
	translate(v = [0.0000000000, 25.4000000000, 0]) {
		intersection() {
			union() {
				difference() {
					union() {
						difference() {
							union() {
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
								translate(v = [0, 0, -12.7000000000]) {
									cylinder(h = 12.7000000000, r = 6.5405000000);
								}
							}
							translate(v = [0, 0, -11.1125000000]) {
								cylinder(h = 11.1125000000, r = 4.9530000000);
							}
						}
						difference() {
							translate(v = [0, 0, -6.3500000000]) {
								cylinder(h = 1.5875000000, r = 6.5405000000);
							}
							translate(v = [-6.5405000000, -6.5405000000, -6.3500000000]) {
								cube(size = [7.5692000000, 13.0810000000, 6.3500000000]);
							}
						}
						intersection() {
							translate(v = [1.0287000000, -7.1859425784, -12.7000000000]) {
								cube(size = [1.5875000000, 14.3718851568, 6.3500000000]);
							}
							translate(v = [0, 0, -12.7000000000]) {
								cylinder(h = 12.7000000000, r = 6.5405000000);
							}
						}
					}
					translate(v = [2.6162000000, -6.5405000000, -13.7000000000]) {
						cube(size = [3.9243000000, 13.0810000000, 7.3500000000]);
					}
				}
				translate(v = [2.6162000000, 0, -12.7000000000]) {
					union() {
						translate(v = [0, 0, 0.7937500000]) {
							rotate(a = [0, 90, 0]) {
								cylinder(h = 1.5430500000, r = 0.7937500000);
							}
						}
						translate(v = [3.1305500000, 0, 2.3812500000]) {
							cylinder(h = 3.9687500000, r = 0.7937500000);
						}
						intersection() {
							translate(v = [1.5430500000, 0, 4.7625000000]) {
								translate(v = [0, 0, -2.3812500000]) {
									rotate(a = [90, 0, 0, 0]) {
										rotate_extrude() {
											translate(v = [1.5875000000, 0, 0]) {
												circle(r = 0.7937500000);
											}
										}
									}
								}
							}
							translate(v = [2.7336750000, 0, 1.1906250000]) {
								cube(center = true, size = [2.3812500000, 1.5875000000, 2.3812500000]);
							}
						}
					}
				}
			}
			translate(v = [0, 32.8422000000, 0]) {
				cube(center = true, size = 65.6844000000);
			}
		}
	}
	translate(v = [25.4000000000, 25.4000000000, 0]) {
		intersection() {
			difference() {
				union() {
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
					translate(v = [0, 0, -12.7000000000]) {
						cylinder(h = 12.7000000000, r = 6.5405000000);
					}
				}
				translate(v = [2.6162000000, -6.5405000000, -13.7000000000]) {
					cube(size = [3.9243000000, 13.0810000000, 7.3500000000]);
				}
			}
			translate(v = [0, 32.8422000000, 0]) {
				cube(center = true, size = 65.6844000000);
			}
		}
	}
	translate(v = [50.8000000000, 25.4000000000, 0]) {
		intersection() {
			difference() {
				union() {
					difference() {
						union() {
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
							translate(v = [0, 0, -12.7000000000]) {
								cylinder(h = 12.7000000000, r = 6.5405000000);
							}
						}
						translate(v = [0, 0, -11.1125000000]) {
							cylinder(h = 11.1125000000, r = 4.9530000000);
						}
					}
					difference() {
						translate(v = [0, 0, -6.3500000000]) {
							cylinder(h = 1.5875000000, r = 6.5405000000);
						}
						translate(v = [-6.5405000000, -6.5405000000, -6.3500000000]) {
							cube(size = [7.5692000000, 13.0810000000, 6.3500000000]);
						}
					}
					intersection() {
						translate(v = [1.0287000000, -7.1859425784, -12.7000000000]) {
							cube(size = [1.5875000000, 14.3718851568, 6.3500000000]);
						}
						translate(v = [0, 0, -12.7000000000]) {
							cylinder(h = 12.7000000000, r = 6.5405000000);
						}
					}
				}
				translate(v = [2.6162000000, -6.5405000000, -13.7000000000]) {
					cube(size = [3.9243000000, 13.0810000000, 7.3500000000]);
				}
			}
			translate(v = [0, 32.8422000000, 0]) {
				cube(center = true, size = 65.6844000000);
			}
		}
	}
	translate(v = [76.2000000000, 25.4000000000, 0]) {
		intersection() {
			difference() {
				union() {
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
					translate(v = [0, 0, -12.7000000000]) {
						cylinder(h = 12.7000000000, r = 6.5405000000);
					}
				}
				translate(v = [0, 0, -12.7000000000]) {
					cylinder(h = 6.3500000000, r = 0.7937500000);
				}
			}
			translate(v = [0, 32.8422000000, 0]) {
				cube(center = true, size = 65.6844000000);
			}
		}
	}
	translate(v = [0.0000000000, 50.8000000000, 0]) {
		intersection() {
			difference() {
				union() {
					difference() {
						union() {
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
							translate(v = [0, 0, -12.7000000000]) {
								cylinder(h = 12.7000000000, r = 6.5405000000);
							}
						}
						translate(v = [0, 0, -11.1125000000]) {
							cylinder(h = 11.1125000000, r = 4.9530000000);
						}
					}
					translate(v = [0, 0, -12.7000000000]) {
						cylinder(h = 6.3500000000, r = 1.5875000000);
					}
					translate(v = [0, 0, -7.9375000000]) {
						cylinder(h = 1.5875000000, r = 6.5405000000);
					}
				}
				translate(v = [0, 0, -12.7000000000]) {
					cylinder(h = 6.3500000000, r = 0.7937500000);
				}
			}
			translate(v = [0, 32.8422000000, 0]) {
				cube(center = true, size = 65.6844000000);
			}
		}
	}
	translate(v = [25.4000000000, 50.8000000000, 0]) {
		intersection() {
			difference() {
				union() {
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
					translate(v = [0, 0, -12.7000000000]) {
						cylinder(h = 12.7000000000, r = 6.5405000000);
					}
				}
				translate(v = [0, 0, -11.1125000000]) {
					cylinder(h = 11.1125000000, r = 4.9530000000);
				}
			}
			translate(v = [0, 32.8422000000, 0]) {
				cube(center = true, size = 65.6844000000);
			}
		}
	}
	translate(v = [50.8000000000, 50.8000000000, 0]) {
		intersection() {
			difference() {
				union() {
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
					translate(v = [0, 0, -12.7000000000]) {
						cylinder(h = 12.7000000000, r = 6.5405000000);
					}
				}
				translate(v = [0, 0, -12.7000000000]) {
					cylinder(h = 12.7000000000, r = 4.9530000000);
				}
			}
			translate(v = [0, 32.8422000000, 0]) {
				cube(center = true, size = 65.6844000000);
			}
		}
	}
	translate(v = [76.2000000000, 50.8000000000, 0]) {
		intersection() {
			union() {
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
				translate(v = [0, 0, -12.7000000000]) {
					cylinder(h = 12.7000000000, r = 6.5405000000);
				}
			}
			translate(v = [0, 32.8422000000, 0]) {
				cube(center = true, size = 65.6844000000);
			}
		}
	}
	translate(v = [0.0000000000, 76.2000000000, 0]) {
		intersection() {
			union() {
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
				hull() {
					intersection() {
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
						translate(v = [0, 0, 0]) {
							cylinder(h = 0.0625000000, r = 20.6883000000);
						}
					}
				}
			}
			translate(v = [0, 32.8422000000, 0]) {
				cube(center = true, size = 65.6844000000);
			}
		}
	}
}
