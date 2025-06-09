import sys
import argparse

def regularinstall(package_name):
    pass

def gitcloneinstall(package_name):
    pass    
 
 
parser = argparse.ArgumentParser()
parser.add_argument("package_name", help="Name of the package to install")
args = parser.parse_args()
