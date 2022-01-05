class Neuron:

    def __init__(self, w, f = lambda x: x):
        self.w = w
        self.f = f
        self.x = list()

    def forward(self, x):
        self.x = x
        return self.f(sum(self.w[i]*x[i] for i in range(len(x))))

    def backlog(self):
            return self.x



neron = Neuron([i for i in range(1,5)])


print(neron.forward([i for i in range(1,5)]))
print(neron.backlog())

