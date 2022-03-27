# OPTIMAL-IPB

OPTIMAL-IPB (Oil Palm Trees Identification based on Machine Learning – IPB University) is an open access plugin in Quantum GIS software used to detect oil palm trees canopy on high-resolution satellite images. This plugin was developed based on deep learning models on Retinanet architecture implemented on the repository by [Fizyr](https://github.com/fizyr/keras-retinanet). Some modifications were applied to enhance the model’s accuracy in detecting oil palm trees canopy as small objects. OPTIMAL-IPB was built by researchers from the Center for Regional System, Analysis, Planning and Development (P4W/CRESTPENT), IPB University, Indonesia. It was based on research funded by the Indonesia Endowment Fund for Education (LPDP) – the Ministry of Finance.

## Installation Steps

### 1. Module Required
Open python console in QGIS and run `import pip` then `pip.main(['install', '-q', '--disable-pip-version-check', 'six ', 'scipy', 'cython', 'keras-resnet==0.2.0', 'h5py', 'keras', 'matplotlib', 'numpy>=1.14', 'opencv-python>=3.3.0', 'pillow', 'progressbar2', 'tensorflow>=2.3.0'])` to install all the prerequisites.

The installation process time depends on the internet connection speed.

### 2. GPU Configuration (Optional)
:warning: This plugin is built using tensorflow as a machine learning framework. For faster process, it is highly recommended to use a GPU. You can find complete instructions for GPU Support through [this link](https://www.tensorflow.org/install/gpu#software_requirements).

### 3. Plugin Installation
There are two ways to install this plugin.
1. From official QGIS Plugin Repository - Use the QGIS Plugins menu to install the OPTIMAL-IPB Plugin (see [QGIS manual](http://docs.qgis.org/latest/en/docs/user_manual/plugins/plugins.html)).
2. From [Zipfile](https://github.com/p4wlppmipb/OPTIMAL-IPB/archive/master.zip) of this repository. Then follow this [instruction](http://docs.qgis.org/latest/en/docs/user_manual/plugins/plugins.html#the-install-from-zip-tab).

### 4. Pick a Model

xxx

## Usage

xxxx

## Sources

1) [fizyr/keras-retinanet](https://github.com/fizyr/keras-retinanet)
2) [Martin Zlocha](https://github.com/martinzlocha/anchor-optimization)
3) [(Faster) Non-Maximum Suppression in Python](https://pyimagesearch.com/2015/02/16/faster-non-maximum-suppression-python/) by Adrian Rosebrock
4) [Sliding Windows for Object Detection with Python and OpenCV](https://pyimagesearch.com/2015/03/23/sliding-windows-for-object-detection-with-python-and-opencv/) by Adrian Rosebrock

## For developers

If you have any idea or trouble, please [post an Issue](https://github.com/p4wlppmipb/OPTIMAL-IPB/issues) first.

We very much welcome contributions from all developers out there. This project is a community-driven open-source tool - please help us to make it better.


## License

OPTIMAL-IPB is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

<em>Copyright © 2018-2022 Muhammad Nurdin, Didit Okta Pribadi, La Ode Syamsul Iman. [P4W-LPPM IPB](https://p4w.ipb.ac.id/en/)</em>
