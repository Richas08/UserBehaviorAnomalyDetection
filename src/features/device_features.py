import pandas as pd

# Load device data
device = pd.read_csv(
    "datasets/raw/device.csv"
)

# USB Connect Count
usb_connect_count = (
    device[device['activity'] == 'Connect']
    .groupby('user')
    .size()
    .reset_index(name='usb_connect_count')
)

# USB Disconnect Count
usb_disconnect_count = (
    device[device['activity'] == 'Disconnect']
    .groupby('user')
    .size()
    .reset_index(name='usb_disconnect_count')
)

# Total USB Usage
usb_usage_count = (
    device
    .groupby('user')
    .size()
    .reset_index(name='usb_usage_count')
)

# Merge
usb_features = usb_connect_count.merge(
    usb_disconnect_count,
    on='user',
    how='outer'
)

usb_features = usb_features.merge(
    usb_usage_count,
    on='user',
    how='outer'
)

usb_features.fillna(0, inplace=True)

print(usb_features.head())

print("\nShape:")
print(usb_features.shape)

usb_features.to_csv(
    "datasets/processed/usb_features.csv",
    index=False
)