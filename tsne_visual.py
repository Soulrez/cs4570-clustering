# That's an impressive list of imports.
import numpy as np
from numpy import linalg
from numpy.linalg import norm
from scipy.spatial.distance import squareform, pdist

# We import sklearn.
import sklearn
from sklearn.manifold import TSNE
from sklearn.datasets import load_digits
from sklearn.preprocessing import scale

# We'll hack a bit with the t-SNE code in sklearn 0.15.2.
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.manifold.t_sne import (_joint_probabilities,
                                    _kl_divergence)
from sklearn.utils.extmath import _ravel
# Random state.
RS = 20150101

# We'll use matplotlib for graphics.
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import matplotlib

# We import seaborn to make nice plots.
import seaborn as sns
sns.set_style('darkgrid')
sns.set_palette('muted')
sns.set_context("notebook", font_scale=1.5,
                rc={"lines.linewidth": 2.5})

# We'll generate an animation with matplotlib and moviepy.
#from moviepy.video.io.bindings import mplfig_to_npimage
#import moviepy.editor as mpy

def scatter(x):
    f = plt.figure(figsize=(10, 5))
    ax = plt.subplot(121)
    sc = ax.scatter(x[:,0], x[:,1])
    #subplot(122)
    #scatter(X_pca[:, 0], X_pca[:, 1], c=iris.target)
    plt.savefig('tsne-generated.png', dpi=120)

    '''
    # We choose a color palette with seaborn.
    palette = np.array(sns.color_palette("hls", 10))

    # We create a scatter plot.
    f = plt.figure(figsize=(8, 8))
    ax = plt.subplot(aspect='equal')
    sc = ax.scatter(x[:,0], x[:,1], lw=0, s=40)
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    ax.axis('off')
    ax.axis('tight')
    '''

with open('eb_scrubbed') as f:
    data = [map(float, i.split(',')) for i in f]
    print data
    data_transform = TSNE(learning_rate=100).fit_transform(data)
    scatter(data_transform)
