## hbar

This repository contains files for bars, holders and other 3d parts for imaging and electrophysiology.

The designs were created in FreeCAD - an open source design software.  

These designs are currently maintained by Joao Couto and used in the Churchland lab.

### Holder for imaging and electrophysiology

This holder can be fabricated in stainless steel and we have been using it for imaging and electrophysiology. Use the latest version for the mesoscope.

![picture](images/headbar_holder.png)


Model: [headbar_holder.FCStd](models/headbar_holder_mesoscope.FCStd)

3d for visualization:
 - [holder main](stl/mesoscope_headbar_holder_main.stl)
 - [left clamp](stl/mesoscope_headbar_holder_clamp_left.stl)
 - [right clamp](stl/mesoscope_headbar_holder_clamp_right.stl)

To manufacture use the step files
 - [holder main](step/mesoscope_headbar_holder_main.step)
 - [left clamp](step/mesoscope_headbar_holder_clamp_left.step)
 - [right clamp](step/mesoscope_headbar_holder_clamp_right.step)

The holes are designed to be treaded for 8-32 screws and the design is for 1mm tick post implants. If you want metric screws, thread for M4 should also work but hasn't been tested.

For behavior training one can use a cheaper holder - IBL rig compatible:
 - [holder main](stl/behavior_holder_main.stl) [manufacture](step/behavior_holder_main.step)
 - [right clamp](stl/behavior_holder_clamp.stl) [manufacture](step/behavior_holder_clamp.step)
 
The latter works but can be made better.

Files: 

### Post implant for imaging (11 mm)

The implant can be cut from a 1mm titanium sheet.

![picture](images/imaging_post.png)

Model: [headbar.FCStd](models/headbar.FCStd)
3d: [imaging headbar](stl/headbar_imaging.stl)

There are also versions with:
   - [a smaller ring (8.6mm)](stl/headbar_imaging_8.6mm.stl).
   - [for ephys/cortex-wide imaging](stl/headbar_ephys.stl).

To manufacture use the drawing in: [11mm implant post](drawings/2p_headbar.pdf)


#### Imaging ring

When implanting the post, we also center a ring on the window, this will interface with a light shielding sleeve that wraps around the objective.  

Model for the ring: [shield](models/imaging_shield.FCStd) - this file will also have the sleeve in the future.

To manufacture or visualize use the [stl file](stl/ring_imaging.stl). 


**Please drop me a line for feedback and let the world know if you use this.**

Joao Couto - jpcouto@gmail.com

Churchland lab - June 2021