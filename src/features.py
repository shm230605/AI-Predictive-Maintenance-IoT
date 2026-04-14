def create_features(df):
    # Input features
    X = df[['temperature', 'vibration', 'current']]
    
    # Target
    y = df['failure']
    
    return X, y