import subprocess
import numpy as np
import os
import shutil
import glob


def move_files_out(start_path,end_path,file_name):
    start_file = os.path.join(start_path,file_name)
    end_file = os.path.join(end_path,file_name)
    shutil.copy2(start_file,end_file)

def move_files_in(outpath,start_path):
    files = os.listdir(outpath) 
    for file in files:
        startf = os.path.join(outpath,file)
        endf = os.path.join(start_path,file)
        shutil.move(startf,endf)

tag = "ia3d_3_3_3_channels_and_nearest"

start_path = "C:/Users/s3599678/OneDrive - RMIT University/PhD/scripts/model_padf/ia3d/results/"
end_path = "C:/Users/s3599678/ia3d/"
file_name = f"{tag}_mPADF_total_sum.npy"

move_out = move_files_out(start_path,end_path,file_name)


fname = f"C:/Users/s3599678/ia3d/{tag}_mPADF_total_sum.npy"
outpath = "C:/Users/s3599678/ia3d/results/"
configfile = 'plot_ia3d_config.txt'



data = np.load(fname)
data += data[:,:,::-1]
outname = fname[:-4]+"_sym.npy"
np.save(outname,data)

fname = outname

flags = f'--stype reqr --rval 2.5 --rpval 2.5 --suffix reqr --fname {fname} --outpath {outpath}'
result = subprocess.run(f'python "C:/Users/s3599678/OneDrive - RMIT University/PhD/scripts/pypadf/plotfxs3d.py" -c "../model_padf/configs/{configfile}" '+flags,shell=True) #,capture_output=True)

move_in = move_files_in(outpath,start_path)







#flags = f'--rval 2.5 --rpval 4.0 --suffix 2p5_4p0 --fname {fname} --outpath {outpath}'
#result = subprocess.run('python /Users/andrewmartin/cloudstor/Work/Research/SF/codes/code_projects/pypadf/plotfxs3d.py -c config_tac_plot_rline.txt '+flags,shell=True) #,capture_output=True)

#flags = f'--stype rconst --rval 2.5 --rpval 2.5 --suffix r2p5 --fname {fname} --outpath {outpath}'
#result = subprocess.run('python /Users/andrewmartin/cloudstor/Work/Research/SF/codes/code_projects/pypadf/plotfxs3d.py -c config_tac_plot.txt '+flags,shell=True) #,capture_output=True)

# RCONST SERIES
"""
r, rlabel = 2.5, '2p5'

flags = f'--stype rconst --thwid 5 --rval {r} --rpval {r} --suffix r{rlabel}_thwid5 --fname {fname} --outpath {outpath}'
result = subprocess.run(f'python /Users/andrewmartin/cloudstor/Work/Research/SF/codes/code_projects/pypadf/plotfxs3d.py -c config_tac_plot{cfx}.txt '+flags,shell=True) #,capture_output=True)


flags = f'--stype rconst --thwid 10 --rval {r} --rpval {r} --suffix r{rlabel}_thwid10 --fname {fname} --outpath {outpath}'
result = subprocess.run(f'python /Users/andrewmartin/cloudstor/Work/Research/SF/codes/code_projects/pypadf/plotfxs3d.py -c config_tac_plot{cfx}.txt '+flags,shell=True) #,capture_output=True)

flags = f'--stype rconst --thwid 15 --rval {r} --rpval {r} --suffix r{rlabel}_thwid15 --fname {fname} --outpath {outpath}'
result = subprocess.run(f'python /Users/andrewmartin/cloudstor/Work/Research/SF/codes/code_projects/pypadf/plotfxs3d.py -c config_tac_plot{cfx}.txt '+flags,shell=True) #,capture_output=True)

# some reqr blurred planes
flags = f'--stype reqr --thwid 5 --rval {r} --rpval {r} --suffix reqr_thwid5 --fname {fname} --outpath {outpath}'
result = subprocess.run(f'python /Users/andrewmartin/cloudstor/Work/Research/SF/codes/code_projects/pypadf/plotfxs3d.py -c config_tac_plot{cfx}.txt '+flags,shell=True) #,capture_output=True)


flags = f'--stype reqr --thwid 10 --rval {r} --rpval {r} --suffix reqr_thwid10 --fname {fname} --outpath {outpath}'
result = subprocess.run(f'python /Users/andrewmartin/cloudstor/Work/Research/SF/codes/code_projects/pypadf/plotfxs3d.py -c config_tac_plot{cfx}.txt '+flags,shell=True) #,capture_output=True)

flags = f'--stype reqr --thwid 15 --rval {r} --rpval {r} --suffix reqr_thwid15 --fname {fname} --outpath {outpath}'
result = subprocess.run(f'python /Users/andrewmartin/cloudstor/Work/Research/SF/codes/code_projects/pypadf/plotfxs3d.py -c config_tac_plot{cfx}.txt '+flags,shell=True) #,capture_output=True)

"""
"""
# THCONST SERIES
thlist = [5, 30, 60, 90]
thwidlist = [5, 10, 15]
for th in thlist:
    for thw in thwidlist:
        flags = f'--stype thconst --thwid {thw} --thval {th} --suffix thconst_th{th}_thwid{thw} --fname {fname} --outpath {outpath}'
        result = subprocess.run(f'python /Users/andrewmartin/cloudstor/Work/Research/SF/codes/code_projects/pypadf/plotfxs3d.py -c config_tac_plot{cfx}.txt '+flags,shell=True) #,capture_output=True)
"""
