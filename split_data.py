import splitfolders
### SPLIT DATA INTO 80 % TRAIN 0 % VALIDATION 20 % TEST
splitfolders.ratio('Kvasir-SEG', output="output", seed=1337, ratio=(.8, 0,0.2)) 