list1 = [ 1,2,3]

# do not support operation broadcasting
print("list1 * 4 = ",list1 * 4 )
# expected value is [4,8,12]
# but output is [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

# --------------------------------------------------------
import numpy as np
nparr = np.array( [1, 2, 3] )
print( nparr )
print(" nparr * 4 = ",nparr * 4 )   # it support operation broadcasting
print( "nparr + 4 = ", nparr + 4)

