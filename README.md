# pyCuda_Houdini

Hi There

This repository is created to track my development on Cuda and Python  (pyCuda) implementation into Houdini from SideFX.

Firstly, I would like to mention that I have a very limited programming background, I am moderate with VEX, familiar with Python, do know some MEL. Absouletly no knowledge on CUDA. But I am a quick learner and quiet eager on such tasks.

So please help me on this task for speeding up things in Houdini or any other task than can be greatly accelerated by the power of GPU.

First goal was to sucesfully run a random number generation trough python SOP in Houdini.

houdini_python_check.py can be used for this purpose

Second goal was to simply to create an gpu array and move the points from the given geometry in which the code can be seen in

move_pts_GPU_ARRAY.py

So far it is pretty much %50 slower than VEX :)

The idea came from me being bothered for why the FFT displacement calculations were being performed in the CPU in oceanevaluate node. I was quiet curious on which part of the ocean Evaluate could be accelereated by using the oceanFFT already avaliable.

But generally, I just would like to become more faimilar with parallel programing.

Thanks for your contributions
Tim
