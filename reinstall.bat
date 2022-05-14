pip uninstall --yes pytorchgui
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q pytorchgui.egg-info
python setup.py install