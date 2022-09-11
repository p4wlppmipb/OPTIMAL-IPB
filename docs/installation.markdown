---
layout: page
title: Installation
permalink: /installation/
---

## Installation Steps

:warning: This plugin was developed in python 3.7 environment contained in QGIS version 3.10 A Coruña, and works with keras version 2.4.3 and tensorflow version 2.3.0.

### 1. Package Required

Some packages need to be installed in the QGIS environment first. There are two ways to install packages in the QGIS environment.

#### - Package installation via python console in QGIS

Open python console in QGIS and run `import pip` then `pip.main(['install', '-q', '--disable-pip-version-check', 'scipy', 'cython', 'keras-resnet', 'opencv-python', 'pillow', 'progressbar2', 'tensorflow==2.3.0', 'keras==2.4.3'])` to install all the prerequisites.

#### - Module installation via OSGeo4W Shell

Open OSGeo4W Shell then run this command `pip install scipy cython keras-resnet opencv-python pillow progressbar2 tensorflow==2.3.0 keras==2.4.3`

### 2. GPU Configuration (Optional)
This plugin is built using tensorflow as a machine learning framework. For faster process, it is highly recommended to use a GPU. You can find complete instructions for GPU Support through [this link](https://www.tensorflow.org/install/gpu#software_requirements).

For Windows user, we need to add the CUDA®, CUPTI, and cuDNN installation directories to the %PATH% environmental variable on QGIS. Click `Settings > Options`, on the System Tab choose `Environment` then check `Use custom variables (restart required - include separators)`.

Click Plus (+) button, then add configuration bellow:

- `Apply: Prepend`
- `Variable: PATH`
- `Value: C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\bin;C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\extras\CUPTI\lib64;C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\include;`

### 3. Plugin Installation
There are two ways to install this plugin.
1. From official QGIS Plugin Repository - Use the QGIS Plugins menu to install the OPTIMAL-IPB Plugin (see [QGIS manual](http://docs.qgis.org/latest/en/docs/user_manual/plugins/plugins.html)).
2. From [Zipfile](https://github.com/p4wlppmipb/OPTIMAL-IPB/archive/master.zip) of this repository. Then follow this [instruction](http://docs.qgis.org/latest/en/docs/user_manual/plugins/plugins.html#the-install-from-zip-tab).

### 4. Pick a Model

There are three models that have been trained using Backbone Resnet101. You can download the three models in the table below:
| Satellite Imagery Paltform  | mAP@0.5 | Model (inference) |
| --------------------------- | ------- | -------------------- |
| Pleiades Satellite Imagery  | 0.903   | [Pleiades-Resnet101.h5](https://github.com/p4wlppmipb/OPTIMAL-IPB/releases/download/0.1/Pleiades-Resnet101.h5) |
| Geoeye Satellite Imagery    | 0.900   | [Geoeye-Resnet101.h5](https://github.com/p4wlppmipb/OPTIMAL-IPB/releases/download/0.1/Geoeye-Resnet101.h5)     |
| Google Satellite Imagery    | 0.925   | [Google-Resnet101.h5](https://github.com/p4wlppmipb/OPTIMAL-IPB/releases/download/0.1/Google-Resnet101.h5)     |

Copy all models you downloads to your plugin directory. Eg: `C:\Users\Username\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\optimal-ipb\models`.

## Usage

This plugin can be accessed under Plugins menu, then select `Calculate > OPTIMAL-IPB` or in the Processing Toolbox, then select `OPTIMAL-IPB > OPTIMAL-IPB` as shown in the image below:

<img src='../assets/Readme01.png'>

Afterward you can input your raster layer then select model previously downloaded. You can change the default value of mean Average Precision (mAP) during the detection process. Select output type from three types of output that can be generated namely point, bounding-box and canopy circle. Then select your output layer to save, then click `run`:

<img src='../assets/Readme02.png'>
