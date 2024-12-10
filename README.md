# README
## Install qiskit with Anaconda

```
bash Anaconda3-2024.10-1-Linux-x86_64.sh 
cd ..
mkdir qiskit
cd qiskit/
conda create -n qiskit_env python=3.10 -y
conda activate qiskit_env
```
## Prepare environment
```
conda install -c conda-forge qiskit
conda install -c conda-forge matplotlib
conda install ipython
```
## Test
```
ipython
python -c "import qiskit; print(qiskit.__qiskit_version__)"
```