import numpy as np
import matplotlib.pyplot as plt

# Parameters
wavelength = 500e-9  # Wavelength of light (meters)
slit_separation = 1e-3  # Distance between the two slits (meters)
slit_width = 50e-6  # Width of each slit (meters)
screen_distance = 1  # Distance to the screen (meters)

# Simulation setup
num_points = 1000  # Number of points in the interference pattern
screen_width = 0.01  # Width of the screen (meters)

# Screen positions (x coordinates)
x = np.linspace(-screen_width / 2, screen_width / 2, num_points)

# Calculate wave amplitude from each slit
def wave_amplitude(x, slit_position):
    # Path difference from the slit to the point on the screen
    path_difference = np.sqrt(screen_distance**2 + (x - slit_position)**2) - screen_distance
    # Phase difference due to the path difference
    phase_difference = 2 * np.pi * path_difference / wavelength
    # Amplitude contribution from this slit, assuming uniform amplitude
    amplitude = np.sinc(slit_width * phase_difference / np.pi)
    return amplitude

# Total amplitude from both slits (superposition principle)
total_amplitude = (wave_amplitude(x, -slit_separation / 2) + wave_amplitude(x, slit_separation / 2))

# Calculate intensity (proportional to the square of the amplitude)
intensity = np.abs(total_amplitude)**2

# Plotting the result
plt.figure(figsize=(10, 4))
plt.plot(x * 1e3, intensity, color='blue')  # Convert x to millimeters for plotting
plt.title('Double-slit Interference Pattern')
plt.xlabel('Position on screen (mm)')
plt.ylabel('Intensity (arbitrary units)')
plt.grid(True)
plt.show()
