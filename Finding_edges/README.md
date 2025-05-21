# Edge Detection Project

This project demonstrates various techniques for detecting edges in images. Edge detection is a fundamental process in image processing and computer vision, used to identify points in a digital image at which the image brightness changes sharply or has discontinuities.

## Edge Detection Techniques

The following edge detection techniques are showcased in this project:

### 1. Sobel Filter
The Sobel filter is a gradient-based method that computes the gradient of image intensity at each pixel, allowing for the detection of edges. It uses two 3x3 kernels which are convolved with the original image to calculate approximations of the derivatives – one for horizontal changes, and one for vertical.
- Example Output: `Results/Sobel_y_finding_edges.png` (Illustrates Sobel Y-direction edge detection)

### 2. Laplacian Operator
The Laplacian operator is a second-order derivative filter that is also used to find regions of rapid intensity change. It is an isotropic measure of the 2nd spatial derivative of an image, meaning its response is independent of direction.
- Example Output: `Results/basket_binary_laplacian.png`

### 3. Canny Edge Detector
The Canny edge detector is a multi-stage algorithm that can detect a wide range of edges in images. The steps include:
    1. Noise reduction (e.g., Gaussian filter)
    2. Finding intensity gradients
    3. Non-maximum suppression
    4. Double thresholding
    5. Edge tracking by hysteresis
- Example Output: `Results/baskett_binary_Canny.png`

## Input and Output Examples

Below are examples of input images and their corresponding outputs after applying different edge detection techniques. The `gt.png` image serves as a ground truth for comparison.

| Input Image             | Description                                   | Output Image                                     | Method Used      |
| :---------------------- | :-------------------------------------------- | :----------------------------------------------- | :--------------- |
| `basket.png`            | Original basket image                         | `Results/basket_binary_laplacian.png`            | Laplacian        |
|                         |                                               | `Results/baskett_binary_Canny.png`               | Canny            |
| `basket_noisy.png`      | Basket image with added noise                 | `Results/basket_noisy_binary_2.png`              | (Assumed Method) |
|                         |                                               | `Results/Sobel_y_finding_edges.png`              | Sobel (Y-dir)    |
| `gt.png`                | Ground truth edges for comparison             | N/A                                              | Ground Truth     |

**Note:** Image paths are relative to the `Finding_edges` directory.
- Original images: `basket.png`, `basket_noisy.png`, `gt.png`
- Output images are located in the `Results/` subdirectory.
