import json

def fix_notebook(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            source_str = "".join(source)
            for old, new in replacements:
                if old in source_str:
                    source_str = source_str.replace(old, new)
            
            # recreate source lines
            lines = source_str.splitlines(keepends=True)
            cell['source'] = lines
            
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2, ensure_ascii=False)
        f.write('\n')

if __name__ == "__main__":
    replacements_3dof = [
        (
            "# [yr, theta_r, vx_r, vy_r, vtheta_r, z1, z2, z3]\n"
            "x0_seg = np.array([0, 0, 0, 0, 0])\n"
            "xr0 = np.array([0.0, 0.0, v_xr, v0_yr, 0.0, 0.0, 0.0, 0.0])\n"
            "\n"
            "Xi = np.concatenate((x0_seg, z0, xr0))\n"
            "\n"
            "# Simulação\n"
            "tsim = np.linspace(0, 25, 1001)\n"
            "y0_medido = C @ x0_seg\n"
            "z0 = np.array([0.0, 0.0, 0.0])\n"
            "tss, u, x_sims = ct.forced_response(lander_Seg, U=0, T=tsim, X0=Xi, return_x=True)",
            
            "# [yr, theta_r, vx_r, vy_r, vtheta_r, z1, z2, z3]\n"
            "x0_seg = np.array([0, 0, 0, 0, 0])\n"
            "xr0 = np.array([0.0, 0.0, v_xr, v0_yr, 0.0, 0.0, 0.0, 0.0])\n"
            "y0_medido = C @ x0_seg\n"
            "z0 = np.array([0.0, 0.0, 0.0]) - J @ y0_medido\n"
            "\n"
            "Xi = np.concatenate((x0_seg, z0, xr0))\n"
            "\n"
            "# Simulação\n"
            "tsim = np.linspace(0, 25, 1001)\n"
            "tss, u, x_sims = ct.forced_response(lander_Seg, U=0, T=tsim, X0=Xi, return_x=True)"
        ),
        (
            "y0_medido = C @ x0_seg\n"
            "z0 = np.array([0.0, 0.0, 0.0]) \n"
            "xr0 = np.array([0.0, 0.0, v_xr, v0_yr, 0.0, 0.0, 0.0, 0.0])\n"
            "Xi = np.concatenate((x0_seg, z0, xr0))\n",
            
            "y0_medido = C @ x0_seg\n"
            "z0 = np.array([0.0, 0.0, 0.0]) - J @ y0_medido\n"
            "xr0 = np.array([0.0, 0.0, v_xr, v0_yr, 0.0, 0.0, 0.0, 0.0])\n"
            "Xi = np.concatenate((x0_seg, z0, xr0))\n"
        )
    ]
    fix_notebook("c:\\Users\\felip\\OneDrive\\Documentos\\GitHub\\3-DOF-Rocket-Model\\3DOF_Rocket_Maneuver_System.ipynb", replacements_3dof)

    replacements_planetary = [
        (
            "# [yr, theta_r, vx_r, vy_r, vtheta_r, z1, z2, z3]\n"
            "x0_seg = np.array([-15, 0.7, 2, -1, 0.1])\n"
            "tsim = np.linspace(0, 25, 1001)\n"
            "xr0 = ([tsim**2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])\n"
            "\n"
            "Xi = np.concatenate((x0_seg, z0, xr0))\n"
            "\n"
            "# Simulação\n"
            "tsim = np.linspace(0, 25, 1001)\n"
            "y0_medido = C @ x0_seg\n"
            "z0 = np.array([0.0, 0.0, 0.0]) - J @ y0_medido\n"
            "tss, u, x_sims = ct.forced_response(Rocket_Seg, U=0, T=tsim, X0=Xi, return_x=True)",
            
            "# [yr, theta_r, vx_r, vy_r, vtheta_r, z1, z2, z3]\n"
            "x0_seg = np.array([-15, 0.7, 2, -1, 0.1])\n"
            "tsim = np.linspace(0, 25, 1001)\n"
            "xr0 = ([tsim**2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])\n"
            "y0_medido = C @ x0_seg\n"
            "z0 = np.array([0.0, 0.0, 0.0]) - J @ y0_medido\n"
            "\n"
            "Xi = np.concatenate((x0_seg, z0, xr0))\n"
            "\n"
            "# Simulação\n"
            "tss, u, x_sims = ct.forced_response(Rocket_Seg, U=0, T=tsim, X0=Xi, return_x=True)"
        )
    ]
    fix_notebook("c:\\Users\\felip\\OneDrive\\Documentos\\GitHub\\3-DOF-Rocket-Model\\3-DOF_Planetary.ipynb", replacements_planetary)
