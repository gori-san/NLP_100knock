from sklearn.decomposition import TruncatedSVD
from sklearn.externals import joblib


def main():
    X_PCA = joblib.load('X_PCA')
    t_index = joblib.load('t_index')

    print(X_PCA[t_index['United_States']])


if __name__ == '__main__':
    main()
