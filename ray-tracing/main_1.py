from sionna.rt import load_scene, Paths2CIR

# Load integrated scene
scene = load_scene(sionna.rt.scene.munich)

# Compute propagation paths
paths = scene.compute_paths()

# Compute coverage map
cm = scene.coverage_map()

# Render scene with coverage map and paths
scene.render(paths=paths, coverage_map=cm)

# Convert paths to channel impulse responses
p2c = Paths2CIR(sampling_frequency=1e6, scene=scene)
a, tau = p2c(paths.as_tuple())
