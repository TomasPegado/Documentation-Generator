# Documentation-Generator
Project for Modular Programming class of the Computer Science undergraduation program of PUC-RIO

We developed an application that generates a documentation for your Python Project automatically.


## Format

* The application uses a pattern captured within docstrings. The files to be documented must have two docstrings at the beginning.

* The first contains the description of the script and the second contains the name to be used.

* Then have a docstring below each function def, containing any description you want to give that function.

* You can see the examples in the folder modulos

## How it works

* The user passes to the application the path of the folder containing the modules to be documented. In this case, they could use the modules folder in this repository as a test for using this application.

* Next, the application uses the Gera_Dicionario module to extract the data from the files inside the folder provided by the user and organizes the information for the Formata_HTML module to generate the documentation pages in .html.

* Finally, the application creates a local server using Flask that opens the generated documentation pages in the user's web browser.

* To use it, you can clone this repository and run the app.py

## Final Considerations

* The application doesn't take the name of the .py file by its name, but by the docstring contained within the file. This is a UX error in development that will be corrected.

* The format of the docstrings must follow the standard in the example files in the modulos folder, otherwise the code that extracts the content using regex will not capture the content of the module description.




