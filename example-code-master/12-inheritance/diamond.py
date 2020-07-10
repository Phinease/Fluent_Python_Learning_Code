class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def pong(self):
        print('pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):

    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


print('-'*20, 'A', '-'*20)
a = A()
a.ping()

print('-'*20, 'B', '-'*20)

b = B()
b.ping()
b.pong()

print('-'*20, 'C', '-'*20)

c = C()
c.ping()
c.pong()

print('-'*20, 'D', '-'*20)

d = D()
d.ping()
print('-'*41)
d.pong()
print('-'*41)
d.pingpong()

print('-'*43)
print(D.__mro__)
