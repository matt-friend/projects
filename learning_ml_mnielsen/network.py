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
        if test_data: #optional, allows for evaluation of network training progress after each epoch
            n_test = len(test_data)
        n = len(training_data) #training data - tuples with input and corresponding desired outputs
        for j in xrange(epochs): #epochs - number of epochs to train for
            random.shuffle(training_data) #randomly shuffle the training data
            mini_batches = [ #partition training data into mini batches
                    training_data[k:k+mini_batch_size] #take mini-batch sized slice of training data
                    for k in xrange(0, n, mini_batch_size)] #range of values incremented by mini-batch size up to training data size n
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta) #apply single step of gradient descent
            if test_data:
                print "Epoch {0}: {1} / {2}".format(j, self.evaluate(test_data), n_test)
            else:
                print "Epoch {0} complete".format(j)

    def update_mini_batch(self, mini_batch, eta):
        #update weights and biases of a network by applying gradient descent using backpropagation to a single mini batch
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nable_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabbla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw 
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb 
                       for b, nb in zip(self.biases, nabla_b)]
