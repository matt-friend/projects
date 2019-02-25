class Network(object):
    
    #sizes is going to be an array containing the number of nodes in each layer respectively
    def _init_(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        #intialise random values for weights and biases in arrays using numpy
        #no biases needed for the input layer
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]] 
        #weights for connections between the xth and yth connections in adjacent layers n and n-1
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

    def sigmoid(z):
        return 1.0/(1.0+np.exp(-z))

    def feedforward(self, a):
        #returns the output of the network if a is the input (assuming use of numpy (n,1) ndarray)
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a

    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        if test_data: n_test = len(test_data)
        n = len(training_data)
        for j in xrange(epochs):
            random.shuffle(training_data)
            mini_batches = [
                    training_data[k:k+mini_batch_size]
                    for k in xrange(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print "Epoch {0}: {1} / {2}".format(j, self.evaluate(test)data), n_test)
            else:
                print "Epoch {0} complete".format(j)


