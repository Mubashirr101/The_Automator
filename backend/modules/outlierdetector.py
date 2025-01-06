class OutlierDetector:
    def __init__(self, df):
        self.data = df

    # different outlier detection methods
    def choose_method():
        pass

    # statistical methods
    def z_score():
        # implement both z-score and modified z-score
        pass

    def iqr():
        pass

    def grubbs_test():
        pass

    def dixons_qtest():
        pass

    def ESD_test():
        # Generalized Extreme Studentized Deviate (ESD) Test
        pass

    def Chi_sq_test():
        pass

    # ML methods
    def knn_test():
        pass

    def isolation_forest_test():
        pass

    def OC_SVM():
        # One-Class Support Vector Machine (OC-SVM)
        pass

    def autoencoders():
        # neural nets to construct n reconstruct data and find outliers by finding reconstructure errors
        # will keep it for the end since its not that feasable
        pass

    def LOF():
        # Local Outlier Factor (LOF)
        pass

    def INFLO():
        # influience outlier detection
        # Extends LOF by also considering reverse neighbors (neighbors that consider the point as their neighbor)
        # Detects outliers based on influence regions of a point.
        pass

    def MST():
        # minimum spanning tree
        # graph theory will be used
        pass

    def PCA():
        # principal component analysis
        pass

    # distance based methods
    def euclidean_dist():
        pass

    def manhattan_dist():
        pass

    def mahalanobis_dist():
        pass

    def minkowski_dist():
        pass

    def radius_based_dist():
        pass

    # clustering based methods

    def dbscan():
        pass

    def kmeans_clus():
        pass

    def optics():
        # ordering points to identify clustering structure
        pass

    def kmedoids_clus():
        # Similar to k-means, but instead of using centroids, it selects actual data points (medoids) as cluster centers
        pass

    def GMM():
        # gaussian mixture modelss
        pass

    def hierrachical_clus():
        pass

    def mean_shift_clus():
        pass
