import os

src = ['components','pipeline']
src_2 = ['__init__.py','utils.py','logger.py','exception.py']
components = ['data_ingestion.py',"data_transformation.py","model_training.py","__init__.py"]
pipeline = ['training_pipeline.py','predicting_pipeline.py',"__init__.py"]

os.makedirs('src',exist_ok=True)

for i in src:
    os.makedirs(f"src/{i}",exist_ok=True)

for i in src_2:
    with open(f"src/{i}", 'wb') as f:
        print(f"File Created... {i}")

for i in components:
    with open(f"src/components/{i}" , 'wb') as f:
        print(f"File Created... {i}")

for i in pipeline:
    with open(f"src/pipeline/{i}" , 'wb') as f:
        print(f"File Created... {i}")


os.remove('create_end_to_end_structure.py')
