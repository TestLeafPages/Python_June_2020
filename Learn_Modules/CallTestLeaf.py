#WAY: 1
import Learn_Modules.TestLeaf



Learn_Modules.TestLeaf.Test_Leaf_v01
Learn_Modules.TestLeaf.Test_Leaf_v02

# Way:2

from Learn_Modules.TestLeaf import Test_Leaf_v01

Test_Leaf_v01.registration()

# Way: 3

from Learn_Modules.TestLeaf import sample

from Learn_Modules.TestLeaf import Test_Leaf_v01 as tv1
tv1.registration()

# multiple classes import
from Learn_Modules.TestLeaf import Test_Leaf_v01, Test_Leaf_v02
Test_Leaf_v01.registration()
Test_Leaf_v02.python()


from Learn_Modules.TestLeaf import Test_Leaf_v01 as tv1, Test_Leaf_v02 as tv2
tv1.registration()
tv2.python()