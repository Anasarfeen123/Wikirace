from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

print("Loading AI Brain...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Words we want to map
words = [
    "Dog",
    "Cat",
    "Wolf",
    "Tiger",
    "Car",
    "Truck",
    "Bicycle",
    "Motorcycle",
    "Apple",
    "Banana",
    "Orange",
    "Strawberry",
]

print("Calculating coordinates...")
embeddings = model.encode(words)

# Squash 384 dimensions down to 2 (X and Y coordinates)
pca = PCA(n_components=2)
xy_coordinates = pca.fit_transform(embeddings)

# Plotting the words on a 2D graph
plt.figure(figsize=(10, 8))
plt.style.use("dark_background")  # Matches the workshop vibe

for i, word in enumerate(words):
    x, y = xy_coordinates[i]
    plt.scatter(x, y, color="cyan", s=100)
    plt.text(x + 0.02, y + 0.02, word, fontsize=12, color="white")

plt.title("How the AI sees words (Clustering by Meaning)", color="white", size=16)
plt.savefig("ai_brain_map.png")
print("Saved map as ai_brain_map.png! Click it in the file explorer to view.")
