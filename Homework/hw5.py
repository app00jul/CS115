######################################################
# Name   : Julian Noeske
# Pledge : I pledge my honor that I have abided by the Stevens Honor System.
######################################################
from cs5png import PNGImage

def mult(c,n):
    '''Given numbers c and n, return c*n, using only addition and lööps'''
    result = c
    for i in range(0,n-1):
        result += c
        i += 1
    return result

def update(c,n):
    '''Given numbers c and n,
    return z where z(0, c) = z and z(n, c) = z(n-1, c)**2 + c,
    absolutely no recursion'''
    z = 0
    for i in range(0,n):
        z = z**2 + c
        i += 1
    return z

def inMSet(c,n):
    '''Given a complex c and a number n, return if the magnitude of z
    never goes above 2 in the process of doing update(...). Don't(!)
    call update'''
    z = 0
    for i in range(0,n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True


def scale(pix, pixelMax, floatMin, floatMax):
    '''Given a pixel value, the max pixel value,
    return where that pixel lies on [floatMin, floatMax] where
    pix=0 -> floatMin and pix=pixelMax -> floatMax'''
    result=(((pix/pixelMax)*(floatMax-floatMin))+floatMin)
    return result

def mset(n):
    '''Creates a 300x200 image of the Mandelbrot set, where
    the image is of the complex plane with x real [-2, 1] and y imaginary, [-i, i]'''
    width = 300
    height = 200
    image = PNGImage(width, height)

    for row in range(width):
        for col in range(height):
            # Remove this line once the 'TODO' task is done
            # TODO: how to check if each pixel should go in ?
            #if {belongs}:
            #    image.plotPoint(col,row)
            x = scale(row,300,-2.0,1.0)
            y = scale(col,200,-1.0,1.0)
            c = x+(y*1j)
            if inMSet(c,n):
                image.plotPoint(row,col)

    image.saveFile()

if __name__ == "__main__":
    iterations = 25 # Change this to play with the picture, once everything's working
    mset(iterations)
