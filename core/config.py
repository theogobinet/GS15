import os

THIS_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Keys
KL1 = []
KL2 = []
KO1 = [] 
KO2 = [] 
KO3 = []
KI1 = [] 
KI2 = []
KI3 = []

# Watch variables
WATCH_EXEC_STATUS = False
WATCH_READ_TIME = 0
WATCH_WRITE_TIME = 0
WATCH_BLOC_KASUMI = 0
WATCH_GLOBAL_KASUMI = 0
WATCH_CIPHER_TYPE = "ECB"
WATCH_BLOC_CIPHER = 0
WATCH_GLOBAL_CIPHER = 0
WATCH_PERCENTAGE = 0.01
WATCH_GLOBAL_TIME = 0


# Galois Field
DEGREE = 0
ALPHA_ELEMENTS = []
ELEMENTS = []
NBR_ELEMENTS = 0
# GF(2^16) [1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1] -> 
IRRED_POLYNOMIAL= [1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1]
GENERATOR = 0
INVERSIONS_DICT = None