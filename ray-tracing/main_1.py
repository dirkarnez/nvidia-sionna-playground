import matplotlib.pyplot as plt
import numpy as np
from sionna.rt import load_scene, Transmitter, Receiver, scene, PathSolver, PlanarArray

# Load integrated scene
scene = load_scene(scene.munich)
scene.add(Transmitter("tx-1", [-10,0,10]))
scene.add(Receiver("rx-1", [10,0,10]))
scene.add(Transmitter("tx-2", [-10,1,10]))
scene.add(Receiver("rx-2", [10,-1,10]))

scene.tx_array = PlanarArray(num_cols=3, num_rows=3,
                            pattern="iso", polarization="V")
scene.rx_array = PlanarArray(num_cols=1, num_rows=2,
                            pattern="iso", polarization="VH")

# Compute propagation paths
p_solver = PathSolver()
paths = p_solver(scene, los=True, specular_reflection=True, 
                 diffuse_reflection=False, refraction=False,
                 diffraction=True, edge_diffraction=True)

# # Compute coverage map
# cm = scene.coverage_map()

# # Render scene with coverage map and paths
# scene.render(paths=paths, coverage_map=cm)

# Convert paths to channel impulse responses
# a_rt, _ = paths.cir(sampling_frequency=1e6)

# a = paths.a[0].numpy() + 1j*paths.a[1].numpy()
# tau = paths.tau.numpy()
# doppler = paths.doppler.numpy()
# print(a)
# print(tau)


a, tau = paths.cir(normalize_delays=True, out_type="numpy")

# Shape: [num_rx, num_rx_ant, num_tx, num_tx_ant, num_paths, num_time_steps]
print("Shape of a: ", a.shape)

# Shape: [num_rx, num_rx_ant, num_tx, num_tx_ant, num_paths]
print("Shape of tau: ", tau.shape)

t = tau[0,0,:]/1e-9 # Scale to ns
a_abs = np.abs(a)[0,0,:,0]
a_max = np.max(a_abs)

# And plot the CIR
plt.figure()
plt.title("Channel impulse response")
plt.stem(t, a_abs)
plt.xlabel(r"$\tau$ [ns]")
plt.ylabel(r"$|a|$");