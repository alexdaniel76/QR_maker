# QR Code Generator

This is a simple Python application that generates a QR code based on the URL entered by the user. It uses the qrcode and tkinter libraries for generating the QR code and building the user interface, respectively.

## Prerequisites

Before running this application, you need to have Python 3.x installed on your machine. You can download Python from the official website: https://www.python.org/downloads/

Also, make sure you have the following Python libraries installed:

- tkinter
- qrcode

You can install them using pip, the package installer for Python, by running the following commands in your terminal:

```
pip install tkinter
pip install qrcode
```

## How to use

1. Clone this repository to your local machine.
2. Navigate to the repository's directory.
3. Run the following command in your terminal:

```
python main.py
```

4. The GUI for the QR Code Generator application should open.
5. Enter the URL that you want to generate a QR code for.
6. Click the "Создать" button to generate the QR code.
7. The QR code will be displayed in the canvas below the input field.
8. Click the "Сохранить" button to save the QR code as a JPEG or PNG file.

## How it works

The application uses the QRCode class from the qrcode library to generate the QR code. The URL entered by the user is passed to the QRCode instance, which creates the QR code image. The image is then saved as a file and displayed in the tkinter Canvas widget.

## License

This application is released under the MIT License.
