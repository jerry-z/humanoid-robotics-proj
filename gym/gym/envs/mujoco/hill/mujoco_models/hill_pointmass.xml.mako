<%
    difficulty = opts.get("difficulty", 1.0)
    texturedir = opts.get("texturedir", "/tmp/mujoco_textures")
    hfield_file = opts.get("hfield_file", "/tmp/mujoco_terrains/hills.png")
%>
<mujoco model='pointmass'>
  <compiler inertiafromgeom="true" angle="degree" coordinate="local" texturedir="${texturedir}"/>
  <option timestep="0.02" integrator="RK4" />
  <default>
    <joint limited="false" armature="0" damping="0" />
    <geom condim="3" conaffinity="0" margin="0" friction="1 0.5 0.5" rgba="0.8 0.6 0.4 1" density="100" />
  </default>
  <asset>
    <texture type="skybox" builtin="gradient" width="100" height="100" rgb1="1 1 1" rgb2="0 0 0" />
    <texture name="texgeom" type="cube" builtin="flat" mark="cross" width="127" height="1278" rgb1="0.8 0.6 0.4" rgb2="0.8 0.6 0.4" markrgb="1 1 1" random="0.01" />
    <texture name="texplane" type="2d" builtin="checker" rgb1="0 0 0" rgb2="0.8 0.8 0.8" width="100" height="100" />
    <texture name="hilltexture" file="hills_texture.png" height="40" rgb1="0.62 0.81 0.55" rgb2="0.62 0.81 0.55" type="2d" width="40"/>
    <material name="MatPlane" reflectance="0.0" shininess="1" specular="1" texrepeat="1 1" texture="hilltexture"/>
    <material name='geom' texture="texgeom" texuniform="true" />
    <hfield name="hill" file="${hfield_file}" size="40 40 ${difficulty} 0.1"/>
  </asset>
  <worldbody>
    <light directional="true" cutoff="100" exponent="1" diffuse="1 1 1" specular=".1 .1 .1" pos="0 0 1.3" dir="-0 0 -1.3" />
    <geom name="floor" conaffinity="1" condim="3" material="MatPlane" pos="0 0 -0.1" rgba="0.8 0.9 0.8 1" size="40 40 0.1" type="hfield" hfield="hill"/>
    <body name="torso" pos="0 0 1.75">
      <geom name="pointbody" type="sphere" size="0.5" pos="0 0 0.5" />
      <geom name="pointarrow" type="box" size="0.5 0.1 0.1" pos="0.6 0 0.5" />
      <joint name='ballx' type='slide' axis='1 0 0' pos='0 0 0'/>
      <joint name='bally' type='slide' axis='0 1 0' pos='0 0 0'/>
      <joint name='ballz' type='slide' axis='0 0 1' pos='0 0 0'/>
    </body>
  </worldbody>
  <actuator>
    <!-- Those are just dummy actuators for providing ranges -->
    <motor name="slidex" joint="ballx" ctrlrange="-1.0 1.0" ctrllimited="true" gear="1500"/>
    <motor name="slidey" joint="bally" ctrlrange="-1.0 1.0" ctrllimited="true" gear="1500"/>
  </actuator>
</mujoco>
