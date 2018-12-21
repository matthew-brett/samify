""" For dephasing images

"""

import numpy as np


def dephase(arr, s):
    r""" Dephase image by adding noise to angles in frequency space

    The 2D FFT converts `arr` to complex representation of frequency, which can
    also be represented as angle and radius, at each frequency position $f$
    (corresponding to pixel position $i).

    Phase noise $n_f$ is (for each frequency position $f$) a sample from a
    uniform random variable with interval $[-\pi, \pi)$.

    Call the old angle $a_f$. The new angle is $a_f + s * n_i$.

    Then we reconstruct the image with the inverse FFT, using the new angles
    and the original magnitudes.

    Parameters
    ----------
    arr : array shape (M, N)
        Real-valued array containing grayscale image to dephase.
    s : proportion of phase noise to add.

    Returns
    -------
    deph_arr: array shape (M, N)
        Real-valued array containing dephased grayscale image.
    """
    arr = np.array(arr, np.float64, copy=False)
    # 2D FFT, complex representation
    f_arr = np.fft.rfft2(arr)
    noise = np.random.uniform(-np.pi, np.pi, size=f_arr.shape)
    noisy_angles = np.angle(f_arr) + s * noise
    # Reconstruct complex representation
    dpf_arr = np.abs(f_arr) * np.exp(1j * noisy_angles)
    return np.fft.irfft2(dpf_arr)


def test_dephase():
    # Zero noise should return the original image, more or less.
    img = np.random.uniform(size=(12, 12))
    assert np.allclose(img, dephase(img, 0))
    assert np.allclose(img * 2, dephase(img, 0) * 2)
    # Not so for non-zero noise
    assert not np.allclose(img, dephase(img, 1))
