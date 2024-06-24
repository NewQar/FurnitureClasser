import os
import random
import shutil

dataOrgFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\IKEAFile\ikea\ikea-data\Base"
dataBaseFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\IKEAFile\ikea\ikea-data\Training"

dataDirList = os.listdir(dataOrgFolder)
print(dataDirList)

splitSize = 0.85

# build files array
def split_data(SOURCE, TRAINING, VALIDATION, SPLIT_SIZE):
    files = []

    for filename in os.listdir(SOURCE):
        file = os.path.join(SOURCE, filename)
        print(file)
        if os.path.getsize(file) > 0:
            files.append(filename)
        else:
            print(filename + " has 0 length, will not copy this file!!")

    # print number of files:
    print(len(files))

    trainLength = int(len(files) * SPLIT_SIZE)
    validLength = len(files) - trainLength

    suffleDataSet = random.sample(files, len(files))

    trainingSet = suffleDataSet[:trainLength]
    validSet = suffleDataSet[trainLength:]

    # copy the train images
    for filename in trainingSet:
        src = os.path.join(SOURCE, filename)
        dest = os.path.join(TRAINING, filename)
        shutil.copy(src, dest)

    # copy the valid images
    for filename in validSet:
        src = os.path.join(SOURCE, filename)
        dest = os.path.join(VALIDATION, filename)
        shutil.copy(src, dest)


bedsSourceFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\IKEAFile\ikea\ikea-data\beds"
bedsTrainFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\Train\beds"
bedsValidFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\Valid\beds"

lampsSourceFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\IKEAFile\ikea\ikea-data\lamps"
lampsTrainFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\Train\lamps"
lampsValidFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\Valid\lamps"

chairsSourceFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\IKEAFile\ikea\ikea-data\chairs"
chairsTrainFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\Train\chairs"
chairsValidFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\Valid\chairs"

tablesSourceFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\IKEAFile\ikea\ikea-data\tables"
tablesTrainFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\Train\tables"
tablesValidFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\Valid\tables"

dressersSourceFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\IKEAFile\ikea\ikea-data\dressers"
dressersTrainFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\Train\dressers"
dressersValidFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\Valid\dressers"

sofasSourceFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\IKEAFile\ikea\ikea-data\sofas"
sofasTrainFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\Train\sofas"
sofasValidFolder = r"C:\Users\User\Downloads\GroupAssignmentAiCSC577\Valid\sofas"

split_data(bedsSourceFolder, bedsTrainFolder, bedsValidFolder, splitSize)
split_data(lampsSourceFolder, lampsTrainFolder, lampsValidFolder, splitSize)
split_data(chairsSourceFolder, chairsTrainFolder, chairsValidFolder, splitSize)
split_data(tablesSourceFolder, tablesTrainFolder, tablesValidFolder, splitSize)
split_data(dressersSourceFolder, dressersTrainFolder, dressersValidFolder, splitSize)
split_data(sofasSourceFolder, sofasTrainFolder, sofasValidFolder, splitSize)
