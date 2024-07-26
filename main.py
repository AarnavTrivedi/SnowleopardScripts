import os
import sys
import yaml

from ultralytics import YOLO

import wandb
from wandb.integration.ultralytics import add_wandb_callback


import wandb
from wandb.integration.ultralytics import add_wandb_callback


wandb.init(project="Snowleopard Project", name="Yolo Nano Trial")
api = wandb.Api()



# Load a model
model = YOLO("yolov8n.pt")

#visualization using wandb
add_wandb_callback(model, enable_model_checkpointing=True)


#Use model
results = model.train(data="data.yaml", epochs=50)

#validate model
model.val()


