import subprocess

#
# A script to choose parameters and run modelpadf.py
#
configfile = 'ia3d_config_modelpadf.txt'
flags = ""
result = subprocess.run(f'python "C:/Users/s3599678/OneDrive - RMIT University/PhD/scripts/model_padf/modelpadf.py" -c "./configs/{configfile}" '+flags,shell=True)
