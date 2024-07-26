import os
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--numvalidimgs', type=int, help="The number of target validation images.")
parser.add_argument('--validratio', type=float, help="A number between 0 and 1 representing the fraction of validation images in the total dataset, e.g. 0.3 means 30% of the dataset will be reserved for the validation set.")
args = parser.parse_args()

# --------------- Add directory info here ----------------
datadir = 'dataset'
traindir = 'train'  # Make sure this folder exists already!
validdir = 'val'  # Make sure this folder exists already!
#---------------------------------------------------------

#-------- Set parameters: optional, can use these instead of command line arguments
validratio = 0.1
numvalidimgs = -1
#------------------------------------------------------------

data = os.listdir(datadir)
dataimgs = []
datalabels = []
for file in data:
    if file.endswith('.txt'):
        datalabels += [file]
    else:
        dataimgs += [file]

# Get a random sample of indices for the validation set
if args.numvalidimgs:
    idx = random.sample(range(0, len(dataimgs)), args.numvalidimgs)
elif args.validratio:
    idx = random.sample(range(0, len(dataimgs)), int(args.validratio * len(dataimgs)))
elif numvalidimgs > 0:
    idx = random.sample(range(0, len(dataimgs)), numvalidimgs)
elif validratio > 0:
    idx = random.sample(range(0, len(dataimgs)), int(validratio * len(dataimgs)))
else:
    # Default case if no arguments specified. 70-30 split.
    idx = random.sample(range(0, len(dataimgs)), int(0.3 * len(dataimgs)))

# Break dataset (images and labels) into train and validation sets
validdata = []
traindata = []
for i in range(len(dataimgs)):
    if i in idx:
        validdata += [dataimgs[i], datalabels[i]]
    else:
        traindata += [dataimgs[i], datalabels[i]]

# Move data into respective folders
for validfile in validdata:
    oldvalidfile = datadir + "/" + validfile
    newvalidfile = validdir + "/" + validfile
    os.rename(oldvalidfile, newvalidfile)
for trainfile in traindata:
    oldtrainfile = datadir + "/" + trainfile
    newtrainfile = traindir + "/" + trainfile
    os.rename(oldtrainfile, newtrainfile)

print("Done!")

 