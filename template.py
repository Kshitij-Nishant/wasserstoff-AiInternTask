import os
from pathlib import Path
import logging # to log all info during runtime

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "AI_ImageSegmentation"

list_of_files = [
    ".github/workflows/.gitkeep", # yaml file for CICD deployment purpose
    f"{project_name}/data/input_images/",
    f"{project_name}/data/segmented_objects/",
    f"{project_name}/data/output/",
    f"{project_name}/models/segmentation_model.py",
    f"{project_name}/models/identification_model.py",
    f"{project_name}/models/text_extraction_model.py",
    f"{project_name}/models/summarization_model.py",
    f"{project_name}/utils/preprocessing.py",
    f"{project_name}/utils/postprocessing.py",
    f"{project_name}/utils/data_mapping.py",
    f"{project_name}/utils/visualization.py",
    f"{project_name}/streamlit_app/app.py",
    f"{project_name}/streamlit_app/components/",
    f"{project_name}/tests/test_segmentation.py",
    f"{project_name}/tests/test_identification.py",
    f"{project_name}/tests/test_text_extraction.py",
    f"{project_name}/tests/test_summarization.py",
    "app.py",
    "main.py",
    "requirements.txt",
    "research/trials.ipynb",
    "README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True) 
        logging.info(f"Creating Directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}")