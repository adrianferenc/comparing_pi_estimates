# comparing_pi_estimates
This estimates pi using six different methods. The png file "The number of steps..." shows how many steps of each estimation technique needs to be used to get within $\epsilon$ of $\pi$. The higher the number of steps, the more work it takes to get close to $\pi$.

The first method is by finding the partial sum of the Basel problem, which is the infinite sum $\sum_{n=1}^\infty \frac{1}{n^2}$. This sum converges to $\pi^2/6$, so after the partial sum is taken, it is multiplied by 6 and square rooted. As can be seen in "The number of steps..." png file, this gets within $\epsilon$ of $\pi$ at a rate nearly proportional to 1/$\epsilon$.

The second method is estimating the integral of a quarter of the unit circle using the trapezoidal rule on the integral $\int_0^1 \sqrt{1-x^2}dx$. The trapezoidal rule takes the average of the Riemann sums using left and right endpoints. This converges to $\pi/4$, so the final result is multiplied by 4. As can be seen in "The number of steps..." png file, this gets within $\epsilon$ of $\pi$ fairly quickly and behaves linearly. 

The third method is by finding the partial sum $\sum_{n=1}^\infty \frac{(-1)^{n+1}}{2n-1}$. This converges to $\pi/4$, so the final result is multiplied by 4. As can be seen in "The number of steps..." png file, this gets within $\epsilon$ of $\pi$ at a rate exactly proportional to 1/$\epsilon$.

The fourth method is by finding the partial sum of the Nilakantha sum $3 + \sum_{n=1}^\infty \frac{(-1)^{n+1}4}{(2n)(2n+1)(2n+2)}$. This converges to $\pi$ exactly. As can be seen in "The number of steps..." png file, this gets within $\epsilon$ of $\pi$ at a rate extremely quickly as it is practically flat.

The fifth method is by using Borwein's Algorithm. It uses three terms, $a_n$, $b_n$, and finally $p_n$ which estimates $\pi$. 
$a_1 = \sqrt{2}$ and for $n \geq 2$, $a_n = \frac{\sqrt{a_{n-1}} + 1/\sqrt{a_{n-1}}}{2}$, 
$b_1 = 0$ and for $n \geq 2$, $b_n = \frac{(1+b_{n-1})\sqrt{a_{n-1}}{a_{n-1}+b_{n-1}}$, and
$p_1 = 2+\sqrt{2}$ and for $n \geq 2$, $p_n = \frac{(1+a_n)p_{n-1}b_n}{1+b_n}$
This method gets within $\epsilon$ of $\pi$ the fastest of all of these methods.

The final method is the classic Monte Carlo method. In the unit square $[0,1]\times[0,1]$, $n$ points are randomly distributed. We count those that land within the quarter unit circle. This converges to $\pi/4$, the area of a quarter unit circle divided by the area of the unit square, so the final result is multiplied by 4. This gets within $\epsilon$ of $\pi$ somewhat quickly, however there is a curious jump when $\epsilon \approx 1/800$. Because this method relies on randomness, instead of using the value from this method, we apply the method 100 times and take the median of the outputs.

There is another png file, "Convergence to pi", which shows the output of each of these estimates for $n$ from 10 to 1000, jumping by 10s. 

Included in this graph is an estimation not used above, which is the Riemann sum of $\int_0^1 \frac{1}{1-x^2}dx$ using left endpoints and $n$ rectangles. The integrand is the derivative of $\arcsin(x)$, so by the Fundamental Theorem of Calculus, this integral evaluates to $\arcsin(1) - \arcsin(0) = \pi/2$ so the result is multiplied by 2. However, since this is an improper integral (the integrand does not exist at $x=1$), it gets within $\epsilon$ of $\pi$ extremely slowly and would be an extreme outlier for the "The number of steps..." graph. This made clear in the "Convergence to pi" graph which shows it barely reaching 3 with a partial sum of 1000 summands.
