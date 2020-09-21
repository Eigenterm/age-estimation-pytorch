@echo off

echo 'start'
cd C:\Users\

python --version

pip install better-exceptions==0.2.2

pip install numpy==1.19.1

pip install opencv-python==3.4.2.17

pip install tensorboard==2.3.0

pip install dlib-19.17.99-cp37-cp37m-win_amd64.whl

del dlib-19.17.99-cp37-cp37m-win_amd64.whl

pip install future==0.17.1

pip install imgaug==0.2.9

pip install pandas==0.24.2

pip install tqdm==4.48.2

pip install yacs==0.1.6

pip install pretrainedmodels==0.7.4

pip install torch==1.4.0 -f https://download.pytorch.org/whl/torch_stable.html

pip install torchvision==0.5.0


del newrecord.bat

pause


