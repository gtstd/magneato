"""
"""

from magneato.constants import MU_0
import numpy as np

class StraightWire(object):

    """
    """

    def __init__(self, start=None, end=None, current=None):

        """
        Parameters
        ----------
        start : tuple
            location (x, y, z) of the start of the wire
        end : tuple
            location (x, y, z) of the end of the wire

        """

        # initialize as vertical wire of length 1.0 (cm)
        self._start = start if start is not None\
            else np.array([0.0, 0.0, 0.0])
        self._end = end if end is not None\
            else np.array([0.0, 0.0, 1.0])
        self._current = current if current is not None\
            else 0.0


    def magnetic_field(self, location):

        """
        """

        if self._current == 0:
            return np.zeros(3)

        # map the functions
        norm = np.linalg.norm
        dot = np.dot

        # make an array
        location = np.array(location, dtype=np.float64)
        
        # getting distance from the location    
        r_1 = self._start - location
        r_2 = self._end - location
        ell = self._end - self._start

        if norm(r_1) == 0 or norm(r_2) == 0:
            return np.zeros(3)

        # get angles of the triangle
        arg = dot(r_1, r_2) / (norm(r_1)*norm(r_2))
        if abs(arg) > 1.0:
            arg /= abs(arg)
        alpha = np.arccos(arg)

        arg = norm(r_1)*np.sin(alpha)/norm(ell)
        if abs(arg) > 1.0:
            arg /= abs(arg)
        beta = np.arcsin(arg)

        arg = norm(r_2)*np.sin(alpha)/norm(ell)
        if abs(arg) > 1.0:
            arg /= abs(arg)
        gamma = np.arcsin(arg)

        # get the theta values
        theta_1 = np.arccos(np.sin(gamma))
        theta_2 = np.arccos(np.sin(beta))
        if alpha >= theta_1 and alpha >= theta_2:
            theta_1 *= -1

        # distance
        arr = norm(r_2) * np.cos(theta_2)
        if abs(arr) < 1e-10:
            return np.zeros(3)

        magnitude = MU_0 * self._current * \
                    (np.sin(theta_2) - np.sin(theta_1)) / \
                    (4*np.pi*arr)
        
        direction = np.cross(r_2, r_1)
        direction = direction / norm(direction)

        return magnitude * direction











