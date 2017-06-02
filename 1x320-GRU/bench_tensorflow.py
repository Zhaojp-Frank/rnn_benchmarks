import tensorflow as tf
from data import toy_batch, default_params, write_results, print_results, plot_results
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import os

# Experiment_type
framework = 'tensorflow'
experiment = '1x320GRU'

# Get data
bX, b_lenX, bY, classes = toy_batch()
batch_size, max_len, inp_dims = bX.shape
rnn_size, learning_rate, epochs = default_params()

# Create symbolic vars
x = tf.placeholder(tf.float32, [None, None, inp_dims])
seq_len = tf.placeholder(tf.int32, [None])
y = tf.placeholder(tf.int32, [None])

# Create network
fw_cell = tf.contrib.rnn.GRUCell(rnn_size)
h1, _ = tf.nn.dynamic_rnn(cell=fw_cell, inputs=x, sequence_length=seq_len, dtype=tf.float32)
h2 = h1[:, -1, :]
h3 = tf.layers.dense(h2, units=classes, activation=tf.nn.relu)

# Create loss, optimizer and train function
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=h2, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)

train_step = optimizer.minimize(loss)

# Initialize session
init = tf.global_variables_initializer()
config = tf.ConfigProto()
config.gpu_options.allow_growth = False  # dynamic allocation of VRAM

# Print parameter count
params = 0
for variable in tf.trainable_variables():
    # shape is an array of tf.Dimension
    shape = variable.get_shape()
    variable_parametes = 1
    for dim in shape:
        variable_parametes *= dim.value
    params += variable_parametes
print('# network parameters: ' + str(params))

# Start training
with tf.Session(config=config) as sess:
    sess.run(init)
    time = []
    for i in range(epochs):
        print('Epoch {}/{}'.format(i, epochs))
        start = timer()
        _, output = sess.run([train_step, h3], feed_dict={x: bX, y: bY, seq_len: b_lenX})
        end = timer()
        time.append(end - start)
        assert (output.shape == (batch_size, classes))
write_results(script_name=os.path.basename(__file__), framework=framework, experiment=experiment, parameters=params, run_time=time)
print_results(time)
