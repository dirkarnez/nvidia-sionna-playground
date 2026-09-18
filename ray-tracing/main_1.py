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

# Compute coverage map
cm = scene.coverage_map()

# Render scene with coverage map and paths
scene.render(paths=paths, coverage_map=cm)

# Convert paths to channel impulse responses
p2c = paths.cir(sampling_frequency=1e6, scene=scene)
a, tau = p2c(paths.as_tuple())

print(a)
print(tau)
