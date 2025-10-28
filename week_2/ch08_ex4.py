# Given pre-defined variables:
from future.utils import native_str

n_fins # number of animal ’s fins (integer)
n_wings # number of animal ’s wings (integer)
n_stripes # number of animal ’s stripes (integer)
n_spots # number of animal ’s spots (integer)
has_tail # whether animal has tail (Boolean)

# Write Python expressions to determine if an animal:
# (a) does not have wings
n_wings == 0

# (b) has more stripes than spots or has exactly five spots
n_stripes > n_spots or n_spots == 5

# (c) has five or less stripes and does not have more stripes than spots
(n_stripes <= 5) and not (n_stripes > n_spots)

# (d) does not have fins or spots
n_fins == 0 and n_spots == 0

# (e) has a tail or has exactly two fins and two wings
has_tail or (n_fins == 2 and n_wings == 2)   # () is redundant here, but it helps readability



