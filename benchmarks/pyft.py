from PIL import Image
import numpy as np
import scipy.fftpack as fp
# Based on http://stackoverflow.com/a/38507628


def img_fft(image_in):
    ## Functions to go from image to frequency-image and back
    im2freq = lambda data: fp.rfft(fp.rfft(data, axis=0),
                                   axis=1)
    freq2im = lambda f: fp.irfft(fp.irfft(f, axis=1),
                                 axis=0)

    ## Read in data file and transform
    #data = np.array(Image.open('./cat.jpg'))
    data = np.array(image_in)

    freq = im2freq(data)
    back = freq2im(freq)
    # Make sure the forward and backward transforms work!
    assert(np.allclose(data, back))

    ## Helper functions to rescale a frequency-image to [0, 255] and save
    remmax = lambda x: x/x.max()
    remmin = lambda x: x - np.amin(x, axis=(0,1), keepdims=True)
    touint8 = lambda x: (remmax(remmin(x))*(256-1e-4)).astype(int)

    # def arr2im(data, fname):
    #     out = Image.new('RGB', data.shape[1::-1])
    #     out.putdata(map(tuple, data.reshape(-1, 3)))
    #     out.save(fname)

    #arr2im(touint8(freq), 'freq.png')
    def arr2im(data):
        out = Image.new('RGB', data.shape[1::-1])
        out.putdata(map(tuple, data.reshape(-1, 3)))
        return out

    return arr2im(touint8(freq))
