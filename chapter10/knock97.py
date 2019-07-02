from sklearn.externals import joblib
from gensim.models import word2vec, KeyedVectors
import numpy as np
from tqdm import tqdm
from scipy.stats import spearmanr
from sklearn.cluster import KMeans


def main():
    country_vecs = joblib.load('country_vecs')
    vecs = []
    keys = []
    for key, value in country_vecs.items():
        keys.append(key)
        vecs.append(value)

    kmeans = KMeans(n_clusters=5)
    model = kmeans.fit_predict(vecs)
    for key, cluster in zip(keys, model):
        print(f'{key}\t{cluster}')


if __name__ == '__main__':
    main()
