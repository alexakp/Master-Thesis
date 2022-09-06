PROJECT="inpainting"
import sys
sys.path.insert(0,"./")
import torch
import torch.nn as nn
import torchvision
from glob import glob
import random
import numpy as np
import models
from tqdm import tqdm
import os
from PIL import Image
import dataset  ## fix
import engine  ## fix
import config
import pandas as pd
import matplotlib.pyplot as plt

torch.cuda.empty_cache()

if __name__=="__main__":
    train_path = config.INPAINTING["TRAINPATH"]
    train_files = glob(os.path.join(train_path,"*.jpg"))
    print(f"TRAIN FILES LOADED : {len(train_files)}")

    mask_train_path = config.INPAINTING["MASKTRAINPATH"]
    mask_train_files = glob(os.path.join(mask_train_path,"*.jpg"))
    print(f"TRAIN MASK FILES LOADED : {len(mask_train_files)}")

    test_path=config.INPAINTING["TESTPATH"]
    test_files=glob(os.path.join(test_path,"*.jpg"))
    print(f"TEST FILES LOADED: {len(test_files)}")

    mask_test_path = config.INPAINTING["MASKTESTPATH"]
    mask_test_files = glob(os.path.join(mask_test_path,"*.jpg"))
    print(f"TRAIN MASK FILES LOADED : {len(mask_test_files)}")


    train_dataset=dataset.InfillDatasetCutout(train_files, maskPath=mask_train_files)
    test_dataset=dataset.InfillDatasetCutout(test_files, maskPath=mask_test_files)

    train_loader=torch.utils.data.DataLoader(
        train_dataset,
        batch_size=1,
        shuffle=True,
        num_workers=8
    )
    test_loader=torch.utils.data.DataLoader(
        test_dataset,
        batch_size=1,
        shuffle=False,
        num_workers=8
    )

    G=models.Generator().to(config.DEVICE)
    D=models.Discriminator().to(config.DEVICE)

    G.apply(models.init_weights)
    D.apply(models.init_weights)

    oG=torch.optim.Adam(G.parameters(), lr=0.0002, betas=(0.5, 0.999), eps=1e-08, weight_decay=0, amsgrad=False)
    oD=torch.optim.Adam(D.parameters(), lr=0.0002, betas=(0.5, 0.999), eps=1e-08, weight_decay=0, amsgrad=False)
    
    criterion=nn.BCEWithLogitsLoss().to(config.DEVICE)
    l1loss=nn.L1Loss().to(config.DEVICE)

    E=engine.Engine(PROJECT,G,D,criterion,l1loss,oD,oG,config.DEVICE)
    losses=[]
    GLoss_arr = []
    DLoss_arr = []
    for epoch in range(config.EPOCHS):
        train_loss=E.train(train_loader,epoch)
        print(epoch,train_loss)
        E.generate(test_loader,epoch)
        
        losses.append(train_loss)
        GLoss_arr.append(losses[epoch][0])
        DLoss_arr.append(losses[epoch][1])

        plt.plot(GLoss_arr)
        plt.plot(DLoss_arr)

        plt.savefig('G_and_D_Loss_main.png')
        
        # break

    logdf=pd.DataFrame(losses).reset_index()

    logdf.columns=["epochs","GLoss","Dloss"]
    logdf.to_csv(os.path.join(PROJECT,config.LOGPATH,"log_df.csv"))

