## Detection of Abnormal Cervical Cells

Comparison detector:It is a publicly available cervical cytology image dataset. The dataset consists of a total of 7,410 cervical microscopic images. These microscope images were cropped from whole-slide images (WSI) obtained using the
Pannoramic WSI II digital slide scanner. The corresponding specimens were prepared using the Papanicolaou (Pap) staining method. The dataset is divided into a training set and a test set. The training set contains 6,666 images, and the test set contains 744 images. The cell images were annotated by experienced pathologists. The cell dataset includes 11 categories: ascus (atypical squamous cells of undetermined significance), asch (atypical squamous cells that cannot exclude high-grade squamous intraepithelial lesions), lsil (low-grade squamous intraepithelial lesions), hsil (high-grade squamous intraepithelial lesions), scc (squamous cell carcinoma), agc (atypical glandular cells),trich (trichomonas), cand (candida), flora, herps (herpes), and actinomyces. 

This code is implemented using pytorch.

Multi-Scale Feature Fusion Network for Detecting Cervical Abnormal Cells
