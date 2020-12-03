from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='coco',
                       karpathy_json_path='./dataset_coco_hindi.json',
                       image_folder='./images/',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='./output',
                       max_len=50)
