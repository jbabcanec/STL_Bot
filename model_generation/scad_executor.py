import subprocess
import os

def export_to_stl(scad_script, output_file='outputs/output.stl'):
    scad_file = os.path.join('outputs', 'output.scad')
    with open(scad_file, 'w') as f:
        f.write(scad_script)
    
    subprocess.run(['openscad', '-o', output_file, scad_file])
