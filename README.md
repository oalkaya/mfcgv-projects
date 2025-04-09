# Mathematical Foundations of Computer Graphics and Vision

This repository contains a series of practical assignments for the course **Mathematical Foundations of Computer Graphics and Vision** at ETH Zurich. Each task combines core mathematical tools with hands-on implementations in computer graphics and vision topics, ranging from image deformation to segmentation and deep learning.

---

## Assignment Overview

| Assignment | Description |
|------------|-------------|
| **Exercise 1: RANSAC** | Implemented the RANSAC (Random Sample Consensus) algorithm for robust model estimation in the presence of outliers. |
| **Exercise 2: Branch and Bound** | Solved the Consensus Set Maximization Problem using a Branch and Bound algorithm for robust model fitting. |
| **Exercise 3: MLS & PCA** | Applied image deformation using backward warping and Moving Least Squares as described in Schaefer et al. Reconstructed curves and surfaces using MLS, and implemented image compression using Principal Component Analysis (PCA). |
| **Exercise 4: Graph Cuts & Optimal Transport** | Developed an interactive graph cuts segmentation tool with max-flow/min-cut. Implemented sliced 2-Wasserstein distance for color transfer between images using optimal transport theory. |
| **Exercise 5: Denoising with Variational Methods** | Compared three denoising methods: Gaussian filtering, heat diffusion via the Laplacian PDE, and energy minimization with variational calculus (Euler-Lagrange formulation). |
| **Exercise 6: Deep Learning for Super-Resolution** | Implemented a fully convolutional neural network for 2x image upscaling using PyTorch. Designed datasets, created baseline/residual models, and evaluated with PSNR and SSIM. |

---

## Libraries Used
- Python, NumPy, OpenCV, Matplotlib, SciPy
- PyMaxflow, PyTorch, torchvision, scikit-learn