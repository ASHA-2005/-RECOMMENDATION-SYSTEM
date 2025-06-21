import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load data
data = pd.read_csv("ratings.csv", index_col="user_id")
print("Ratings Data:\n", data)

# Step 2: Compute cosine similarity between users
similarity_matrix = cosine_similarity(data)
similarity_df = pd.DataFrame(similarity_matrix, index=data.index, columns=data.index)
print("\nUser Similarity Matrix:\n", similarity_df)

# Step 3: Recommend items for a given user
def recommend_items(user_id, data, similarity_df, top_n=2):
    similar_users = similarity_df[user_id].drop(user_id)  # drop self
    similar_users = similar_users[similar_users > 0]  # use only positively similar users
    
    # Get ratings from similar users
    similar_users_ratings = data.loc[similar_users.index]
    
    # Multiply ratings by similarity scores
    weighted_ratings = similar_users_ratings.T.dot(similar_users)
    
    # Normalize by sum of similarities
    weighted_avg = weighted_ratings / similar_users.sum()
    
    # Filter out items already rated by the user
    user_rated = data.loc[user_id]
    recommendations = weighted_avg[user_rated == 0].sort_values(ascending=False)
    
    return recommendations.head(top_n)
 
# Step 4: Show recommendations for User 1
print("\nTop Recommendations for User 1:")
print(recommend_items(1, data, similarity_df))