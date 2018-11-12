#!/usr/bin/python
import numpy as np
import pylab


def gaussian(x, y):
    return np.exp(-(x**2 + y**2) / (2 * (25**2)))


def part_a():
    img_data = np.loadtxt('blur.txt')
    pylab.imshow(img_data)
    pylab.set_cmap('Greys_r')
    pylab.show()


def part_b():
    # TODO Check part B
    img_data = np.loadtxt('blur.txt')
    shape = img_data.shape
    blur = [[
        gaussian(x, y) + gaussian(x - shape[0], y) + gaussian(x, y - shape[1]) +
        gaussian(x - shape[0], y - shape[1]) for x in range(shape[0])
    ] for y in range(shape[1])]
    pylab.imshow(blur)
    pylab.set_cmap('Greys_r')
    pylab.show()


def part_c():
    # TODO Finish part C
    img_data = np.loadtxt('blur.txt')
    shape = img_data.shape
    blur = [[
        gaussian(x, y) + gaussian(x - shape[0], y) + gaussian(x, y - shape[1]) +
        gaussian(x - shape[0], y - shape[1]) for x in range(shape[0])
    ] for y in range(shape[1])]
    fft_img = np.fft.rfft2(img_data)
    fft_blur = np.fft.rfft2(blur)
    fft_unblured = np.divide(fft_img, fft_blur)
    unblured = np.fft.irfft2(fft_unblured)
    pylab.imshow(unblured)
    pylab.set_cmap('Greys_r')
    pylab.show()


def main():
    part_a()
    part_b()
    part_c()


if __name__ == "__main__":
    main()
