import os

os.environ['KAGGLEHUB_CACHE'] = os.path.join(os.path.dirname(__file__), '..', 'data', 'kagglehub')

import kagglehub

# каталог товаров с ценами, рейтингами и атрибутами 
catalog_path = kagglehub.dataset_download('djagatiya/myntra-fashion-product-dataset')

# 44 тыс товаров с фото 80x60 
images_path = kagglehub.dataset_download('paramaggarwal/fashion-product-images-small')
