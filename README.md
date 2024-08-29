# Automated File Organizer

This project is an automated file organizer that sorts files into folders based on their file types. It is a simple yet powerful tool to help keep your directories clean and well-organized.

## Features

- Automatically organizes files into folders by type (e.g., Images, Videos, Documents).
- Supports common file formats, including images, videos, documents, and more.
- Easy to customize with additional file types and rules.
- Minimal user intervention required—just run the script and watch it work!

## Prerequisites

- Python 3.x

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/anishakrishn/File-Organizer.git
   cd File-Organizer
   ```

## Usage

1. **Configure Your Directories:**
   - By default, the script organizes files in the current directory. You can customize the target directory by editing the `TARGET_DIRECTORY` variable in the script.

2. **Run the Script:**
   ```bash
   python file_organizer.py
   ```

3. **Watch Your Files Get Organized:**
   - The script will automatically create folders (e.g., Images, Videos, Documents) and move files into their respective folders.

## Customization

- **Adding New File Types:**
  - You can customize the script to recognize and organize additional file types by editing the `FILE_TYPES` dictionary in the script.

- **Changing Folder Names:**
  - To change the names of the folders (e.g., from `Images` to `Photos`), modify the `FOLDER_NAMES` dictionary.

## Example

After running the script, your directory structure might look something like this:

```
/path/to/your/directory
|-- Images
|   |-- photo1.jpg
|   |-- photo2.png
|
|-- Videos
|   |-- video1.mp4
|
|-- Documents
|   |-- report.pdf
|
|-- Others
|   |-- randomfile.xyz
```

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. Contributions are welcome!


## Contact

For any questions or feedback, please contact Anisha at anishakrishn@gmail.com.

