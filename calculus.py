# Tool for simple derviation and simplification of mathematical expressions
# supports additions, multiplications, exponentiation and single variable derivation


# This base class allows for more readable Expressions
class Expr:
	def __add__(self, o):
		return Add(self, o)
	def __mul__(self, o):
		return Mul(self, o)
	def __pow__(self, o):
		return Expo(self, o)
	def __call__(self):
		return self.evaluate()
	def d(self,x):
		return self.derive(x)

# the variable class, base of any mathical expression
class Var(Expr):
	def __init__(self, value = 0.): # name, value):
		self.name = None
		self.value = value
	
	def evaluate(self):
		return self.value
	
	def derive(self, x):
		return one if x == self else zero
	
	def simplify(self):
		return self
	
	def __str__(self):
		# This bloc of code is just for convenience, so you don't have to name variables
		if self.name == None: 
			try:
				self.name = [ k for k,v in globals().items() if v == self][0]
			except:
				try:
					self.name = [ k for k,v in locals().items() if v == self][0]
				except:
					raise NameError("cannot find Variable name")
		return self.name

# those sentinel values are for derived expressions and the simplification of expressions
zero = Var(0.)
one  = Var(1.)

# addition
class Add(Expr):
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def evaluate(self):
		return self.a.evaluate() + self.b.evaluate()
	
	def derive(self, x):
		return self.a.derive(x) + self.b.derive(x)
	
	def simplify(self):
		self.a = self.a.simplify()
		self.b = self.b.simplify()
		if  self.a == zero and self.b == zero: return zero
		if  self.a == zero: return self.b
		if  self.b == zero: return self.a
		return self
	
	def __str__(self):
		return "(" + str(self.a) + " + " + str(self.b) + ")"
	
	def __eq__(self, o):
		return type(o) is Add and ((o.a==self.a and o.b==self.b) or (o.a==self.b and o.b==self.a))
	
	def __ne__(self, obj):
		return not self == obj


# multiplication
class Mul(Expr):
	def __init__(self,a, b):
		self.a = a
		self.b = b
	
	def evaluate(self):
		return self.a.evaluate() * self.b.evaluate()
	
	def derive(self, x):
		return self.a.derive(x) * self.b + self.a * self.b.derive(x)
	
	def simplify(self):
		self.a = self.a.simplify()
		self.b = self.b.simplify()
		if  self.a == zero or self.b == zero: return zero
		if  self.a == one: return self.b
		if  self.b == one: return self.a
		return self
	
	
	def __str__(self):
		return str(self.a) + " * " + str(self.b)
	
	def __eq__(self, o):
		return type(o) is Mul and ((o.a==self.a and o.b==self.b) or (o.a==self.b and o.b==self.a))
	
	def __ne__(self, obj):
		return not self == obj

# exponentiation
class Expo(Expr):
	def __init__(self,a, e):
		self.a = a
		self.e = e
	
	def evaluate(self):
		return self.a.evaluate() ** self.e.evaluate()
	
	def derive(self, x):
		# NOTE : this is not accurate if e depends on x
		# the true result is (u^v)' = (v*ln(u))' * eps^(v*ln(u)) = (u^v)*(v'*ln(u)+v*u'/u)
		return self.e * self.a.derive(x) * self.a ** self.e
	
	def simplify(self):
		self.a = self.a.simplify()
		self.e = self.e.simplify()
		if  self.a == zero: return zero
		if  self.e == zero: return one
		if  self.e == one: return self.a
		return self
	
	
	def __str__(self):
		#return str(self.a) + " ** " + str(self.e)
		return str(self.a) + " ^ " + str(self.e)
	
	def __eq__(self, o):
		return type(o) is Expo and o.a==self.a and o.e==self.e
	
	def __ne__(self, obj):
		return not self == obj

if __name__ == "__main__":
	a = Var(2.)
	b = Var(3.)
	c = Var(6.)
	#d = Var(-1.)
	expr = a + b * c #** d

	print("f =", expr, "where a =", a.value, "b =", b.value, "c =", c.value, "\tresult =", expr.evaluate())
	print("f'(a) =", expr.d(a), "or", expr.d(a).simplify(), "\tresult =", expr.d(a).evaluate()) # 1 + (0 * 3 + 6 * 0)
	print("f'(b) =", expr.d(b), "or", expr.d(b).simplify(), "\tresult =", expr.d(b).evaluate()) # 0 + (0 * 3 + 6 * 1)
	print("f'(c) =", expr.d(c), "or", expr.d(c).simplify(), "\tresult =", expr.d(c).evaluate()) # 0 + (1 * 3 + 6 * 0)
	#print("who's your daddy now ?")

	# h = Mul(b,c)
	# i = Mul(b,c)
	# j = Mul(c,b)
	# k = Mul(a,b)
	# print(h==h)
	# print(h==i)
	# print(h==j)
	# print(h==k)
	# print(h==a)


