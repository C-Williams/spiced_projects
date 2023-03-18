# Image Classification Project

### This project was built upon an existing image capturing project found at [this repo](https://github.com/bonartm/imageclassifier)

The aim of the project was to build an image classification model that, when run in the terminal, opens the users webcam and can determine who's water bottle is in the frame. In addition, the file can be used to generate new images to train your own version of an image classifier.

- Start the program with:

    ```python
    python src/capture_predict.py <output-folder>
    ```

- The program launches your webcam
- You can take pictures by pressing `space`
- You can ask the model to make a prediction by pressing `p`
- Pictures are saved in the folder `<output-folder>` (e.g. `data/faces/`)
- Exit the program with `q`
