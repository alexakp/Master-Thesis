IMAGE_HEIGHT=256
IMAGE_WIDTH=256


LAMBDA=100
EPOCHS=201
DEVICE="cuda:0"

LOGPATH="log"

MX={
    "TRAINPATH":"colorize/data/train",
    "TESTPATH":"colorize/data/test",
    }

INPAINTING={
    "TRAINPATH":"output/train/images", ## EDIT HERE
    "TESTPATH":"output/test/images", ## EDIT HERE
    "MASKTRAINPATH":"output/train/masks",
    "MASKTESTPATH":"output/test/masks",
    }
DOODLE2FACE={
    "TRAINPATH_IMAGES":"doodle2face/data/train/images",
    "TRAINPATH_TARGETS":"doodle2face/data/train/targets",
    "TESTPATH":"doodle2face/data/test",
    }    

FACELANDMARK_MODEL="pretrained_models/face/shape_predictor_68_face_landmarks.dat"
HOLY_MODEL_CONFIG="pretrained_models/hogedge/deploy.txt"
HOLY_MODEL="pretrained_models/hogedge/hed_pretrained_bsds.caffemodel"