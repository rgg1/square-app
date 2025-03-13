building + testing a simple macOS .app file

## Installation

To create the `.app` file, run the following command:

```sh
pyinstaller --windowed --onefile --name SquareCalculator square_app.py
```

## Usage

After running the above command, you will find the `SquareCalculator.app` file in the `dist` directory. You can run this application to use the Square Calculator.
