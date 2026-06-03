from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

print("Loading AI Brain...")
# Using a slightly larger model if you want, but sticking to the current one for speed
model = SentenceTransformer("all-MiniLM-L6-v2")

# Words we want to map - expanded for better clustering demonstration
words = [
    "Dog", "Cat", "Wolf", "Snake", "Spider",
    "Table", "Chair", "Couch",
    "Car", "Truck", "Bicycle", "Motorcycle",
    "Apple", "Banana", "Orange",
    "Spider-web", "World Wide Web", "Internet", "Computer"
]

print(f"Calculating coordinates for {len(words)} words...")
embeddings = model.encode(words)

# Clustering the words by meaning
n_clusters = 5
kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=42)
clusters = kmeans.fit_predict(embeddings)

# Squash dimensions down to 2 using PCA
pca = PCA(n_components=2)
xy_coordinates = pca.fit_transform(embeddings)
variance = pca.explained_variance_ratio_

# Plotting the words on a 2D graph
plt.figure(figsize=(12, 10))
plt.style.use("dark_background")

# Color palette for clusters
colors = plt.get_cmap("viridis", n_clusters)

# Plot each cluster
for i in range(n_clusters):
    points = xy_coordinates[clusters == i]
    plt.scatter(points[:, 0], points[:, 1], color=colors(i), s=150, edgecolors='white', alpha=0.8, label=f"Cluster {i+1}")

# Labeling with better placement
for i, word in enumerate(words):
    x, y = xy_coordinates[i]
    plt.annotate(
        word,
        xy=(x, y),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=11,
        color="white",
        fontweight='bold',
        alpha=0.9
    )

# Aesthetic improvements
plt.margins(0.15)
plt.title("AI Word Mapping: Semantic Clustering", color="white", size=20, pad=20, fontweight='bold')
plt.xlabel(f"PCA Dimension 1 ({variance[0]:.1%} variance)", color="#888888")
plt.ylabel(f"PCA Dimension 2 ({variance[1]:.1%} variance)", color="#888888")

# Add a subtle grid
plt.grid(color='white', linestyle='--', linewidth=0.5, alpha=0.1)

# Clean up axes
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_color('#444444')
plt.gca().spines['left'].set_color('#444444')

# Add legend
plt.legend(title="Meaning Clusters", loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.savefig("ai_brain_map.png", dpi=300, bbox_inches='tight')
print("Updated map saved as ai_brain_map.png!")
