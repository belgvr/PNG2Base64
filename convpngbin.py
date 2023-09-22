import argparse
import base64

# Create a command-line argument parser
parser = argparse.ArgumentParser(description='Convert PNG to base64-encoded text')

# Add a command-line argument for the input PNG file
parser.add_argument('-f', '--file', required=True, help='Input PNG file to convert')

# Parse the command-line arguments
args = parser.parse_args()

# Get the input PNG file name from the command-line argument
png_file = args.file

# Define the output text file name
txt_file = png_file.replace('.png', '.txt')

# Open the PNG file in binary read mode
with open(png_file, 'rb') as image_file:
    # Read the binary data
    binary_data = image_file.read()

# Convert the binary data to a base64-encoded string
base64_data = base64.b64encode(binary_data).decode('utf-8')

# Write the base64-encoded data to a text file
with open(txt_file, 'w') as text_file:
    text_file.write(base64_data)

# Print a message to confirm the operation
print(f'Base64-encoded data saved to {txt_file} 😊')
