import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the dataset into a pandas dataframe
data = pd.read_csv('iris.csv')

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('Species', axis=1), data['Species'], test_size=0.2)

# Create the KNN classifier with k=3
knn = KNeighborsClassifier(n_neighbors=3)

# Train the classifier using the training set
knn.fit(X_train, y_train)

# Use the trained classifier to predict the species of the test set
y_pred = knn.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")
