## Calculus  

A simple and elegant way of calculating mathematical derivatives    

Uses overloaded operators on a custom Var class to construct a mathematical expression tree that can be evaluated, derived and simplified.  
Supports addition, multiplication and partly exponents. Only about 80 effective Lines of code

Example :  
``` python
a, b, c = Var(2.), Var(3.), Var(6.)

expr = a + b * c

print("f =", expr, "where a =", a.value, "b =", b.value, "c =", c.value, "\tresult =", expr.evaluate())
print("f'(a) =", expr.d(a), "or", expr.d(a).simplify(), "\tresult =", expr.d(a).evaluate()) # 1 + (0 * 3 + 6 * 0)
print("f'(b) =", expr.d(b), "or", expr.d(b).simplify(), "\tresult =", expr.d(b).evaluate()) # 0 + (0 * 3 + 6 * 1)
print("f'(c) =", expr.d(c), "or", expr.d(c).simplify(), "\tresult =", expr.d(c).evaluate()) # 0 + (1 * 3 + 6 * 0)
```  
Result:    
![alt text](https://github.com/Lcbx/Calculus/blob/master/Capture.PNG "screenshot")
