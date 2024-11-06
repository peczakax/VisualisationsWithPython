import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Updated DataFrame for NumPy methods including new methods
numpy_methods = {
    'Array Creation': [
        '',
        'array()', 
        'arange()', 
        'zeros()', 
        'ones()', 
        'empty()', 
        'linspace()', 
        'random.rand()', 
        'random.randint()', 
        'full()',  
        'eye()',    
        'identity()',
        'tile()',
        ''
    ],
    'Manipulation': [
        '',
        'reshape()', 
        'transpose()', 
        'concatenate()', 
        'split()', 
        'hstack()', 
        'vstack()', 
        'flip()',   
        'roll()',    
        'expand_dims()',
        'squeeze()',
        ''
    ],
    'Math Functions': [
        '',
        'add()', 
        'subtract()', 
        'multiply()', 
        'divide()', 
        'sqrt()', 
        'power()', 
        'mod()',   
        'exp()',    
        'log()',
        'dot()',
        ''
    ],
    'Statistics': [
        '',
        'mean()', 
        'median()', 
        'std()', 
        'var()', 
        'max()', 
        'min()', 
        'sum()',     
        'unique()',   
        'argmax()',
        'argmin()',
        ''
    ],
    # Data Visualization category
    'Data Visualization': [
        '',
        'histogram()',
        'meshgrid()',
        'vstack()',
        'linspace()',
        'arange()',
        ''
    ]
}

# Convert it to a DataFrame and replace NaN values with empty strings
df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in numpy_methods.items()]))
df = df.replace(np.nan, '', regex=True)  # Replace NaN with empty strings

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))  # Increased height for new category
ax.axis('tight')
ax.axis('off')

# Define colors similar to the Pandas image
colors = ['#d9ead3', '#fce5cd', '#fff2cc', '#f9cb9c']  # Light green, orange, yellow, light red

# Create a table with colored cells and remove all borders
table = ax.table(cellText=df.values,
                 colLabels=df.columns,
                 cellLoc='center', 
                 loc='center')

# Apply colors to columns and remove all borders
for i in range(len(df.columns)):
    for j in range(len(df)):
        
        # Apply background color to each column
        table[(j+1, i)].set_facecolor(colors[i % len(colors)])
        
# Remove all borders by setting edge color to none for every cell (including headers)
for (i, j), cell in table.get_celld().items():
    cell.set_edgecolor('none')  # Remove all borders

# Adjust row height for better readability (line spacing)
for i in range(len(df.columns)):
    for j in range(len(df)):
        
        # Set row height to increase line spacing (adjust this value as needed)
        table[(j+1, i)].set_height(0.05)  # Increase row height

for i in range(len(df.columns)):    
        # Set row height to increase line spacing (adjust this value as needed)
        table[(j+1, i)].set_height(0.05)  # Increase row height

# Set font properties for the header and cells
table.auto_set_font_size(False)
table.set_fontsize(12)

# Set header font style to bold and adjust alignment
for (i, j), cell in table.get_celld().items():
    if i == 0:
        cell.set_text_props(fontweight='bold', color='black', family='Comic Sans MS')  # Handwritten-style for subheaders

# Set the title with monospace font for "Important Methods" and "Packages"
title_y = 0.95
plt.text(0.05, title_y, "Important Methods ", transform=ax.transAxes, fontsize=16, fontweight='bold', family='Courier New')
plt.text(0.35, title_y, "NumPy", fontsize=16, color='red', family='Comic Sans MS', transform=ax.transAxes)
plt.text(0.45, title_y, "Packages", transform=ax.transAxes, fontsize=16, fontweight='bold', family='Courier New')

# Save the table as an image with tight layout and high resolution
plt.savefig('numpy_methods_readable.png', bbox_inches='tight', dpi=300)
plt.show()

