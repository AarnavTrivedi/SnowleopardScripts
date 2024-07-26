import os
import wandb
import shutil

#initialize wandb run

run = wandb.init(project="Snowleopard Project", job_type="dataset-creation", name="Dataset-Fetch-1")

# Create a new artifact, which is a sample dataset
dataset = wandb.use_artifact("SnowleopardDataset:v0")

# Add files to the artifact, in this case a simple text file
# Log the artifact to save it as an output of this run

dataset_dir = dataset.download()

destination_dir = r"C:\Users\aarna\Documents\SnowleopardTrial\dataset"

os.makedirs(destination_dir, exist_ok=True)

# Move the contents of the downloaded dataset directory to the destination directory
for filename in os.listdir(dataset_dir):
    src_path = os.path.join(dataset_dir, filename)
    dst_path = os.path.join(destination_dir, filename)
    shutil.move(src_path, dst_path)


run.log_artifact(dataset)
