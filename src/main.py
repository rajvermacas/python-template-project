# ============================ Project setup ================================
from dotenv import load_dotenv
import sys
import os
import argparse
import logging
import builtins


def init_log(suffix):
    log_file_name = os.path.join(os.getenv("OUTPUT_DIR"), "logs", f"indicator_{suffix}.log")
    logging.basicConfig(filename=log_file_name, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(lineno)d:%(message)s')
    builtins.logging = logging
    
    builtins.logging.info(f"Initializing log for suffix={suffix} log_file_name={log_file_name}")

def init_project():
    # Set up PYTHONPATH
    project_src_dir = os.path.dirname(__file__)
    sys.path.append(project_src_dir)

    project_root_dir = os.path.dirname(project_src_dir)
    
    os.environ['ROOT_DIR'] = project_root_dir
    os.environ['OUTPUT_DIR'] = os.path.join(project_root_dir, 'output')
    os.environ['INPUT_DIR'] = os.path.join(project_root_dir, 'input')
    os.environ['ASSET_DIR'] = os.path.join(project_root_dir, 'asset')

    # Load environment variables from .env file
    env_file_path = os.path.join(project_root_dir, '.env')
    load_dotenv(env_file_path)

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Initialize project environment")
    parser.add_argument('--local', action='store_true', help='Run in local mode')
    args = parser.parse_args()

    os.environ['LOCAL_MODE'] = str(args.local)

    init_log("main")


if __name__ == "__main__":
    init_project()

# ============================ Business logic ==============================
if __name__ == "__main__":
    builtins.logging.info("Running main...")