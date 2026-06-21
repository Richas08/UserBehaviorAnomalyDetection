import pandas as pd

# Load data
file_df = pd.read_csv(
    "datasets/raw/file.csv"
)

# Total file accesses
file_access_count = (
    file_df.groupby('user')
    .size()
    .reset_index(name='file_access_count')
)

# Unique files accessed
unique_file_count = (
    file_df.groupby('user')['filename']
    .nunique()
    .reset_index(name='unique_file_count')
)

# Extract extension
file_df['extension'] = (
    file_df['filename']
    .str.split('.')
    .str[-1]
    .str.lower()
)

# PDF count
pdf_count = (
    file_df[file_df['extension'] == 'pdf']
    .groupby('user')
    .size()
    .reset_index(name='pdf_count')
)

# DOC count
doc_count = (
    file_df[file_df['extension'].isin(['doc', 'docx'])]
    .groupby('user')
    .size()
    .reset_index(name='doc_count')
)

# Image count
image_count = (
    file_df[file_df['extension'].isin(['jpg', 'jpeg', 'png'])]
    .groupby('user')
    .size()
    .reset_index(name='image_count')
)

# Merge all features
file_features = file_access_count.merge(
    unique_file_count,
    on='user',
    how='left'
)

file_features = file_features.merge(
    pdf_count,
    on='user',
    how='left'
)

file_features = file_features.merge(
    doc_count,
    on='user',
    how='left'
)

file_features = file_features.merge(
    image_count,
    on='user',
    how='left'
)

file_features.fillna(0, inplace=True)

print(file_features.head())
print("\nShape:")
print(file_features.shape)

file_features.to_csv(
    "datasets/processed/file_features.csv",
    index=False
)