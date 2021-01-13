# Functionality 4: PyMOL colour change for hydrophobic/hydrophilic residues using the Eisenberg & Weiss hydrophobicity scale
# =================================================================================
# Hydrophobic = Red
# Hydrophilic = Blue
# Above 0.50 = Dark red
# Above 0.1 = Red
# Above 0.0 = Light red 
# Below 0.0 = Light blue
# Below 0.1 = Blue
# Below 0.5 = Dark blue
# =================================================================================
# Ile - 0.73 
# Phe - 0.61 
# Val - 0.54 
# Leu - 0.53
# Trp - 0.37
# Met - 0.26
# Ala - 0.25
# Gly - 0.16
# Cys - 0.04
# Tyr - 0.02
# Pro - -0.07
# Thr - -0.18
# Ser - -0.26
# His - -0.40
# Glu - -0.62
# Asn - -0.64
# Gln - -0.69
# Asp - -0.72
# Lys - -1.10
# Arg - -1.80
# =================================================================================
def hydrophobic_res(selection='all'):
        string_sel = str(selection)
        print string_sel
        cmd.set_color('color_ile',[1.00,0.00,0.00])
        cmd.set_color('color_phe',[1.00,0.00,0.00])
        cmd.set_color('color_val',[1.00,0.00,0.00])
        cmd.set_color('color_leu',[1.00,0.00,0.00])
        cmd.set_color('color_trp',[1.00,0.40,0.40])
        cmd.set_color('color_met',[1.00,0.40,0.40])
        cmd.set_color('color_ala',[1.00,0.40,0.40])
        cmd.set_color('color_gly',[1.00,0.40,0.40])
        cmd.set_color('color_cys',[1.00,0.80,0.80])
        cmd.set_color('color_tyr',[1.00,0.80,0.80])
        cmd.set_color('color_pro',[0.80,0.80,1.00])
        cmd.set_color('color_thr',[0.40,0.40,1.00])
        cmd.set_color('color_ser',[0.40,0.40,1.00])
        cmd.set_color('color_his',[0.40,0.40,1.00])
        cmd.set_color('color_glu',[0.00,0.00,1.00])
        cmd.set_color('color_asn',[0.00,0.00,1.00])
        cmd.set_color('color_gln',[0.00,0.00,1.00])
        cmd.set_color('color_asp',[0.00,0.00,1.00])
        cmd.set_color('color_lys',[0.00,0.00,1.00])
        cmd.set_color('color_arg',[0.00,0.00,1.00])
        cmd.color("color_ile","("+string_sel+" and resn ile)")
        cmd.color("color_phe","("+string_sel+" and resn phe)")
        cmd.color("color_val","("+string_sel+" and resn val)")
        cmd.color("color_leu","("+string_sel+" and resn leu)")
        cmd.color("color_trp","("+string_sel+" and resn trp)")
        cmd.color("color_met","("+string_sel+" and resn met)")
        cmd.color("color_ala","("+string_sel+" and resn ala)")
        cmd.color("color_gly","("+string_sel+" and resn gly)")
        cmd.color("color_cys","("+string_sel+" and resn cys)")
        cmd.color("color_tyr","("+string_sel+" and resn tyr)")
        cmd.color("color_pro","("+string_sel+" and resn pro)")
        cmd.color("color_thr","("+string_sel+" and resn thr)")
        cmd.color("color_ser","("+string_sel+" and resn ser)")
        cmd.color("color_his","("+string_sel+" and resn his)")
        cmd.color("color_glu","("+string_sel+" and resn glu)")
        cmd.color("color_asn","("+string_sel+" and resn asn)")
        cmd.color("color_gln","("+string_sel+" and resn gln)")
        cmd.color("color_asp","("+string_sel+" and resn asp)")
        cmd.color("color_lys","("+string_sel+" and resn lys)")
        cmd.color("color_arg","("+string_sel+" and resn arg)")
cmd.extend('hydrophobic_res', hydrophobic_res)

