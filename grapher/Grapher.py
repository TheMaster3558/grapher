import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
import math

from .safe import safe_eval

e = math.e # e = 2.718281828459045
pi = math.pi # pi = 3.141592653589793

def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

def tan(x):
    return np.tan(x)

def cosec(x):
    return 1/sin(x)

def sec(x):
    return 1/cos(x)

def cot(x):
    return 1/tan(x)

def factorial(x):
    '''
    Factorial/Repeted Multiplication of number x.
    factorial(3) # 3*2*1
    >>> 6
    '''
    return np.math.factorial(x)

def sqrt(x):
    '''
    Square Root of a number x.
    sqrt(49)
    >>> 7.0
    '''
    return round(x**(0.5), 2)

def cbrt(x):
    '''
    Cube Root of a Number x.
    print(cbrt(125))
    >>> 5.0
    '''
    return round(x**(1./3.), 2)

def ln(x):
    return np.log(x)

def log(x, base=10):
    '''
    Find Logarithm of a number x.
    log(100)
    >>> 2.0

    log(64, 2)
    >>> 6.0
    '''
    return ln(x)/ln(base)


env = {
    'e': e,
    'pi': pi,
    'sin': sin,
    'cos': cos,
    'tan': tan,
    'cosec': cosec,
    'sec': sec,
    'cot': cot,
    'factorial': factorial,
    'sqrt': sqrt,
    'cbrt': cbrt,
    'ln': ln,
    'log': log
}


class Grapher:
    def __init__(self, fx, x_lim=[-50, 50], y_lim=[-50, 50], step=0.01, label=True, grid=True, xlabel='x', title=None, lol="upper left", linestyle='-', mode='light'):
        self.fx = fx
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.grid = grid
        self.label = label
        self.step = step
        self.x = np.arange(*self.x_lim, step=self.step)
        self.xlabel = xlabel
        self.ylabel = f'f ({xlabel})'
        self.title = title
        self.lol = lol
        self.linestyle = linestyle
        self.mode = mode

    def valid_function(self, f):
        '''
        Converts a human readable str(equation) to a more executable form.
        sinx -> sin(x)
        2^4 -> 2**4
        '''
        eq = f.replace('^', '**')
        if 'x' not in eq and len(eq) > 0:
            eq += '* x/x'

        eq = eq.replace('sinx', 'sin(x)')
        eq = eq.replace('cosx', 'cos(x)')
        eq = eq.replace('tanx', 'tan(x)')
        eq = eq.replace('cosecx', 'cosec(x)')
        eq = eq.replace('secx', 'sec(x)')
        eq = eq.replace('cotx', 'cot(x)')
        eq = eq.replace('lnx', 'ln(x)')
        eq = eq.replace('logx', 'log(x)')

        return eq

    def plot(self):
        '''
        Plot the graphs of many equations on one graph to see the relations between the graphs.
        You can use it to see how well Taylor Series match with the actuall graph of a function.

        Eg:
        g = Grapher(['sin(x)', 'x - ((x**3)/factorial(3)) + (x**5)/factorial(5)'], lb=-3, ub=3, grid=True)
        g.plot()
        '''
        fig, ax = plt.subplots()
        ax.set_xlim(*self.x_lim)
        ax.set_ylim(*self.y_lim)

        x = self.x
        for f in self.fx:
            eq = self.valid_function(f)
            y = safe_eval(eq, env | {'x': x})
            ax.plot(x, y, self.linestyle, label=f'{self.ylabel} = {str(f)}')
        if self.label:
            ax.legend(loc=self.lol)

        if self.grid:
            ax.grid()

        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        if self.title is not None:
            plt.title(self.title)
        
        ax.axvline(0, c='k', lw=1)
        ax.axhline(0, c='k', lw=1)
        
        return fig, ax

    def examples(self):
        '''
        See some graphing examples.
        '''
        g = Grapher(['cos(x)', '1 - ((x^2)/factorial(2)) + (x^4)/factorial(4)'], lb=-3, ub=3, label=True, lol='lower center', title='Taylor Polynomial for cos(x)')
        g.plot()
        g = Grapher(['sinx', 'd("sinx")'], step=0.001, mode='dark')
        g.plot()

    def author(self):
        '''
        Well, wanna know about me? Run this method!
        '''
        plt.text(-9, 3, """Hi, I am Shubham. Hope you are enjoying Grapher.
Try plotting something crazy!
How About x^x or sinx.
And now, you need not even calculate it.
Well, close this window to see them.
Note: this project has been forked by The Master""")
        plt.plot(np.arange(-10, 10), np.arange(-10, 10))
        plt.show()
        g = Grapher(['x^x', 'd("x^x")'], 0, 1.5)
        g.plot()
        g = Grapher(['sinx', 'd("sinx")'], mode='dark')
        g.plot()


if __name__ == '__main__':
    # g = Grapher(['cos(x)', '1 - ((x^2)/factorial(2)) + (x^4)/factorial(4)'], lb=-3, ub=3, label=True, lol='lower center', title='Taylor Polynomial for cos(x)')
    g = Grapher(['1 + 1/x', 'x'], step=0.001, y_lim=[-5, 5])
    g.plot()
    
