import numpy as np
import caffe

caffe.set_mode_cpu()
solver = caffe.get_solver('simple_solver.prototxt')
solver.share_weights(solver.test_nets[0])
solver.step(1)

print('Solver step test: OK')
