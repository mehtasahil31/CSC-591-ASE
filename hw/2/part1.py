from Tbl import Tbl

if __name__ == "__main__":
	
	s="""
	$cloudCover, $temp, $humid, $wind,  $playHours
	100,        68,    80,    0,    3   # comments
	0,          85,    85,    0,    0
	0,          80,    90,    10,   0
	60,         83,    86,    0,    4
	100,        70,    96,    0,    3
	100,        65,    70,    20,   0
	70,         64,    65,    15,   5
	0,          72,    95,    0,    0
	0,          69,    70,    0,    4
	?,          75,    80,    0,    3  
	0,          75,    70,    18,   4
	60,         72,    
	40,         81,    75,    0,    2    
	100,        71,    91,    15,   0	
	"""

	tbl = Tbl(s)
	print(tbl.Row["cells"])