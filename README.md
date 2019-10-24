## Calculus  

A simple and elegant way of calculating mathematical derivatives    

Uses overloaded operators on a custom Var class to construct an Expression tree that can be evaluated, deived and simplified.  
Supports addition, multiplication and partly exponents. Only about 80 effective Lines of code

Example :  
``` python
a, b, c = Var(2.), Var(3.), Var(6.)
	
	expr = a + b * c
	
	print("a =", a.value, "  b =", b.value, "  c =", c.value, "   and f =", expr,"=", expr.evaluate())
	print("f'(a) =", expr.d(a), "=", expr.d(a).simplify(), "=", expr.d(a).evaluate()) # 1 + (0 * 3 + 6 * 0)
	print("f'(b) =", expr.d(b), "=", expr.d(b).simplify(), "=", expr.d(b).evaluate()) # 0 + (0 * 3 + 6 * 1)
	print("f'(c) =", expr.d(c), "=", expr.d(c).simplify(), "=", expr.d(c).evaluate()) # 0 + (1 * 3 + 6 * 0)
	#print("who's your daddy now ?")
```  
Result:    
![alt text](https://github.com/Lcbx/Calculus/blob/master/Capture.PNG "screenshot")
