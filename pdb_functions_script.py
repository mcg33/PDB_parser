# BS7105 Mini-Project: Parsing PDB files
# =================================================================================
import sys
import Bio.PDB
from Bio.PDB.PDBParser import PDBParser 

#Printing out to text file
# =================================================================================
#sys.stdout = open("results.txt", "w")

#Biopython parser
parser = PDBParser(PERMISSIVE=1)
PDBstructure = sys.argv[1]
Structure_ID = sys.argv[2]
structure = parser.get_structure(Structure_ID, PDBstructure)

#Isolating key sections of the .pdb file
resolution = structure.header['resolution']
keywords = structure.header['keywords']
author = structure.header['author']
print(keywords)
#print(author)
#print(resolution)

#Iterating through all atoms of a structure
for model in structure:
    for chain in model:
        for residue in chain:
            for atom in residue:
                break

#Functionality 1: Determining the distance between adjacent residue Alpha-Carbons in Angstroms
# =================================================================================
print(" ")
print("Distance between adjacent residue alpha-carbons:")
for residue1 in chain:
    for residue2 in chain:
        if residue1 != residue2:
            try:
                distance = residue1['CA'] - residue2['CA']
            #If there is no Alpha-Carbon
            except KeyError:
                continue
            if distance < 6:
                print(residue1, residue2, "Distance: ", distance, "Angstroms")
        #Stop after 1st residue, #break to run through whole protein
        break

#Functionality 2: Finding names and co-ordinates of Alpha-carbons with a B-factor > 75
# =================================================================================
print(" ")
print("Names and co-ordinates of residues with B-factor > 75:")
for model in structure.get_list():
    for chain in model.get_list():
        for residue in chain.get_list():
            if residue.has_id("CA"):
                alpha_c = residue["CA"]
                if alpha_c.get_bfactor() > 75.0:                                 
                    print(residue)                    
                    print(alpha_c.get_coord())                  
                #Stop after 1st residue with Bfactor > 75, "#" to run whole protein                    
                break
                    
#Functionality 3: Calculating torsion angles (Phi & Psi angles in radians)
# =================================================================================
print(" ")
print("Torsion angles in radians:")
for model in structure:
    for chain in model:
        polypeptides = Bio.PDB.PPBuilder().build_peptides(chain)   
        for poly_index, poly in enumerate(polypeptides) :
            print("Chain %s" % (str(chain.id)),)
            print("(part %i of %i)" % (poly_index+1, len(polypeptides)),)
            print("Polypeptide length: %i" % (len(poly)),)
            print("From %s%i" % (poly[0].resname, poly[0].id[1]),)
            print("to %s%i" % (poly[-1].resname, poly[-1].id[1]))
            print("Residue (Phi, Psi) bond angles in radians:")
            phi_psi = poly.get_phi_psi_list()
            for res_index, residue in enumerate(poly) :
                res_name = "%s%i" % (residue.resname, residue.id[1])
                print(res_name, phi_psi[res_index])   
                #Stop after 1st residue, #break to run through whole protein       
                break

#sys.stdout.close()
