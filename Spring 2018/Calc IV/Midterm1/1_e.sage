from sage.plot.colors import rgbcolor
def coef(k):
    if k % 2 == 0:
        return prod(((n+1)*(n-4))/(n*(n-1)) for n in range(2, k+2, 2))
    else:
        return prod(((n+1)*(n-4))/(n*(n-1)) for n in range(3, k+2, 2))

def gen_eq(r):
    return 1 + (-3)*pow(x, 2)+x+sum([coef(k) * pow(x, k) for k in range(3, r+2, 2)])

f(x) = 1 + (-3)*pow(x, 2) + x + sum([coef(k) * pow(x, k) for k in range(3, 7, 2)])
plt = plot(gen_eq(5), (x, -2.5, 1.5), ymax=5, ymin=-5, color=rgbcolor((0, 0, 1)))
plt += plot(gen_eq(30), (x, -2.5, 1.5), ymax=5, ymin=-5, color=rgbcolor((0.25, 0, 0.75)))
plt += plot(gen_eq(55), (x, -2.5, 1.5), ymax=5, ymin=-5, color=rgbcolor((0.5, 0, 0.5)))
plt += plot(gen_eq(80), (x, -2.5, 1.5), ymax=5, ymin=-5, color=rgbcolor((0.75, 0, 0.25)))
plt += plot(gen_eq(105), (x, -2.5, 1.5), ymax=5, ymin=-5, color=rgbcolor((1, 0, 0)))
plt.save("1_e.png")
