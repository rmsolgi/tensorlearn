import torch
from tensorlearn.neural_network.torch import utils
import tensorlearn as tl
m=40
n=30

W = torch.randn(n, m)

new_shape=(10,3,4,10)
tensor=W.view(new_shape)

print(tensor.size())

optimal_shape=utils.get_tensorized_layer_balanced_shape(m,n,2,2)
print(optimal_shape)

tt_factors=utils.get_tt_factors(tensor,optimal_shape,0.1)
core_factor, factor_matrices=utils.get_tucker_factors(tensor,optimal_shape,1)
print(tl.tt_ranks(tt_factors))
print(tl.tt_compression_ratio([f.numpy() for f in tt_factors]))