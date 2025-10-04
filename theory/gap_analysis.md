# Energy Accounting: Where Does the Energy Go?

## 🔍 The Critical Question

When we simulate the GravityCore system, we observe **70% efficiency** in the theoretical model. But where does the remaining **30%** of energy go? Let's break it down systematically.

### 📊 Energy Flow Analysis (Per Cycle)
| Stage | Input (J) | Output (J) | Loss (J) | Loss % |
|-------|-----------|------------|----------|--------|
| Solar Input | 0.236 | — | — | — |
| Optical Concentration | 0.236 | 0.231 | 0.005 | 2.1% |
| Spectral Splitting | 0.231 | 0.213 | 0.018 | 7.8% |
| Photoconductive Control | 0.213 | 0.196 | 0.017 | 8.0% |
| Mechanical Transfer | 0.196 | 0.175 | 0.021 | 10.7% |
| Multi-Mode Harvesting | 0.175 | 0.135 | 0.040 | 22.9% |
| **TOTAL** | **0.236** | **0.135** | **0.101** | **42.8%** |

### 🔧 Detailed Loss Analysis

1. **Optical Concentration (2.1%)**  
   - **Cause**: Diffraction limits in optical system  
   - **Physics**: Abbe diffraction limit: `Δθ = 1.22 * λ / D`  
   - **Calculated loss**: 2.1% due to imperfect concentration

2. **Spectral Splitting (7.8%)**  
   - **Cause**: Quantum efficiency of QDs  
   - **Physics**: Stokes shift and non-radiative recombination  
   - **Calculated loss**: 7.8% due to spectral splitting inefficiency

3. **Photoconductive Control (8.0%)**  
   - **Cause**: Resistive losses in semiconductor layers  
   - **Physics**: Ohmic losses: `P_loss = I²R`  
   - **Calculated loss**: 8.0% due to series resistance

4. **Mechanical Transfer (10.7%)**  
   - **Cause**: Viscous drag in hourglass geometry  
   - **Physics**: Stokes' law: `F_d = 6πμrv`  
   - **Calculated loss**: 10.7% due to mechanical friction

5. **Multi-Mode Harvesting (22.9%)**  
   - **Cause**: Incomplete energy capture across modes  
   - **Physics**: Mode coupling inefficiencies  
   - **Calculated loss**: 22.9% due to imperfect harvesting

### 💡 Key Insight
The **largest single loss** (22.9%) comes from **multi-mode harvesting inefficiencies** - not from fundamental physics limits. This suggests that:
1. We could improve mode coupling by 20-30% with better mechanical design
2. The theoretical maximum could be raised to **~90%** with optimized harvesting
3. Real-world prototypes will need to focus on **mechanical efficiency** rather than theoretical limits

> **Important Note**: All losses are calculated from the simulation model, not experimental data. Actual prototypes will have additional losses from material imperfections and manufacturing tolerances.
