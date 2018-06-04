# rnn_benchmarks
Welcome to the rnn_benchmarks repository! We offer:
- A training speed comparison of different LSTM implementations across deep learning frameworks
- Common input sizes, network configurations and cost functions from continuous speech recognition and isolated speech recognition scenarios
- Best-practice scripts on how to code up a network, optimizers, loss functions etc. when you are learning a new framework!

# Updates
 
## June 4th 2018
 - arxiv paper release pending
 - [LSTM benchmarks between PyTorch 0.4, TensorFlow 1.8, Keras 2.1.6 and latest Lasagne](https://github.com/stefbraun/rnn_benchmarks/tree/master/results/10/framework_comparison)
 ![alt text](https://github.com/stefbraun/rnn_benchmarks/blob/master/results/10/framework_comparison/1x320-LSTM_cross-entropy.png)
 - [LSTM benchmarks between PyTorch versions 0.1.12 to 0.4.0](https://github.com/stefbraun/rnn_benchmarks/tree/master/results/10/pytorch_comparison)
 ![alt text](https://github.com/stefbraun/rnn_benchmarks/blob/master/results/10/pytorch_comparison/1x320-LSTM_cross-entropy.png)


## Run the benchmarks
Go to the folder 'main' and execute the 'main.py' script in the corresponding benchmark folder. Before running 'main.py', you need to give the paths to the python environment that contain the corresponding framework. The 'main.py' script creates a 'commands.sh' script that will execute the benchmarks. The measured execution times will be written to 'results/results.csv'. The toy data and default parameters are provided by 'support.py', to make sure every script uses the same hyperparameters.

