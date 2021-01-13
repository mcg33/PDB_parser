# PDB parser program using Python3 - User Guide 
## Installing Biopython 
* Open Linux terminal 
* Enter into the command line - '*pip install biopython*' 
## Running the hydrophobicity colour change program
* Open relevant .pdb file into PyMOL 
* In the PyMOL Viewer, click "S" -> "Surface" (To view the surface of the protein) 
* Click "File" -> "Run Script" -> "hydrophobic_res_pymol.py" 
* Enter in the Pymol command line "hydrophobic_res" 
* Hydrophobic residues appear red, more hydrophilic residues appear blue 
## Altering hydrophobicity colour change program for PyMOL
* Editing the co-ordinates for each residue changes their colour in PyMOL, e.g. turning Ile from red to blue:
  * '*cmd.set_color('color_ile',[1.00,0.00,0.00])*'
  * '*cmd.set_color('color_ile',[0.00,0.00,1.00])*'  
* Full colour values can be found at: https://pymolwiki.org/index.php/Color_Values 
## Running the protein annotation program "pdb_functions_script.py" via the terminal
* Open terminal from within the same folder as the program 
* Enter "Python3 pdb_functions_script.py *filename.pdb* *structure_ID*" to see annotations for your desired protein in .pdb format e.g. '*Python3 pdb_functions_script.py 7buy.pdb 7buy*' 
## Altering "pdb_functions_script.py" code to suit individual needs
* To alter information displayed about your .pdb file # and un-# specific lines as you need: To display the authors of the file - un-# line 22 
  * '*#print(author)*'
  * '*print(author)*' 
The same applies to the other variables including resolution and keywords 

* Printing out results to a text file, un-# lines 9 and 85 to print results to text file 
  * '*#sys.stdout = open("results.txt", "w")*' 
  * '*sys.stdout = open("results.txt", "w")*' 

  * '*#sys.stdout.close()*' 
  * '*sys.stdout.close()*' 

* To determine the distance between Alpha-Carbons of all residues, "#" line 47 in the code 
  * '*break*' 
  * '*#break*' 

* To find the names of all residues and co-ordinates of their Alpha-Carbons with a B-factor > 75, "#" line 62 
  * '*break*' 
  * '*#break*' 

* To find all torsion angles of all residues, "#" line 83 
  * '*break*' 
  * '*#break*' 
