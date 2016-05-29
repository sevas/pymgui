"""
Why does this exist?
Because I'm done trying to make Configuration-depdendent postbuild events 
with CMake. Generator expressions are unusable as soon as you need build 
command lines with arguments in quote.

So here it is: a script that copies a target to a destination directory, and 
takes the PDB along for the relevant configurations.
"""

import argparse
import shutil
import os

def copy(src_file, dest_dir):
	fname = os.path.basename(src_file)
	dest_file = os.path.join(dest_dir, fname)
	print("-- Copying {} to {}".format(src_file, dest_file))
	shutil.copy(src_file, dest_file)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Proper postbuild')
	
	parser.add_argument('--config', type=str, required=True)
	parser.add_argument('--target-file', type=str, required=True)
	parser.add_argument('--dest-dir', type=str, required=True)
	
	args = parser.parse_args()
	copy(args.target_file, args.dest_dir)
	if args.config in ('RelWithDebInfo', 'Debug'):
		pdb_file = args.target_file.replace('.dll', '.pdb')
		if os.path.exists(pdb_file):
			copy(pdb_file, args.dest_dir)