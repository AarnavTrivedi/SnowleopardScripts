import wandb
import os

# Initialize a new W&B run to track this job
run = wandb.init(project="Snowleopard Project", job_type="dataset-creation", name="Dataset Upload 3")


# Create a new artifact, which is a sample dataset
dataset = wandb.Artifact('SnowleopardDataset', type='dataset')
# Add files to the artifact, in this case a simple text file
dataset.add_dir(r'C:\Users\aarna\Documents\SnowleopardTrial\dataset')
# Log the artifact to save it as an output of this run
run.log_artifact(dataset)

