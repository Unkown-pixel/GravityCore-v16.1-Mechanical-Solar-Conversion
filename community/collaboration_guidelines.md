# Collaboration Guidelines for Gravity Core

## 🤝 Core Principles

1. **Physics First, Not Hype**
   - All claims must be grounded in verified physics
   - No "game-changing" claims without energy accounting
   - Reference to established literature (e.g., IEEE, APS journals)

2. **Transparency is Mandatory**
   - All code must be open and reproducible
   - Simulation parameters must be fully documented
   - Limitations must be explicitly stated

3. **No Commercialization Pressure**
   - This is a research sandbox, not a product
   - No patents, no commercial claims, no investment pitches
   - Focus on scientific understanding, not market disruption

## 📋 Contribution Requirements

### ✅ What to Contribute
- **Physics validation**: Code that verifies or challenges the physics assumptions
- **Energy accounting**: Detailed tracking of every joule in the system
- **Alternative pathways**: Different mechanical conversion approaches
- **Real-world constraints**: Manufacturing, material, and environmental limitations
- **Analysis notebooks**: Jupyter notebooks with visualizations and explanations

### ❌ What NOT to Contribute
- "Free energy" claims that violate thermodynamics
- Unverified efficiency claims without energy accounting
- Build guides for non-experts
- Commercialization plans
- Personal opinions without scientific basis

## 🧪 Validation Process

1. **Initial Submission**
   - Fork the repository
   - Create a new branch (`git checkout -b feature/your-feature`)
   - Commit changes with descriptive messages (`git commit -am 'Add spectral splitting model'`)

2. **Physics Review**
   - All contributions must pass physics validation:
     - Energy conservation check (input ≤ output)
     - Thermodynamic feasibility (no perpetual motion)
     - Reference to established literature
   - Validation scripts are provided in `simulation/validation/`

3. **Peer Review**
   - Contributions are reviewed by at least 2 independent researchers
   - Feedback must be constructive and physics-based
   - Revisions required until consensus is reached

4. **Documentation Update**
   - All contributions must include:
     - Clear explanation of physics principles
     - Limitations of the approach
     - References to supporting literature
     - Comparison with existing methods

## 📊 Reporting Standards

### For Simulation Results
- Must include:
  - Full energy accounting table (like in `simulation/analysis/results.ipynb`)
  - Input parameters with units
  - Validation checks (energy conservation, physics compliance)
  - Comparison with baseline systems (e.g., silicon PV)

### For Theoretical Work
- Must include:
  - Derivation of key equations
  - Assumptions and limitations
  - Comparison with established models
  - References to peer-reviewed literature

## 🌍 Community Etiquette

- **No personal attacks**: Disagree with ideas, not people
- **No "I'm right" arguments**: Evidence-based discussions only
- **No gatekeeping**: Welcome all researchers, regardless of background
- **No misinformation**: Correct errors promptly and transparently
- **No commercial exploitation**: This is a research resource, not a business opportunity

## 📈 Success Metrics

| Metric | Target | Why It Matters |
|--------|--------|----------------|
| **Physics Validity** | 100% | Ensures scientific integrity |
| **Transparency** | 100% | Enables reproducibility |
| **Collaboration** | 5+ active contributors | Sustains long-term research |
| **Energy Accounting** | Complete for all processes | Prevents greenwashing |
| **Real-World Relevance** | 3+ practical applications identified | Bridges theory and practice |

## 💬 How to Engage

1. **Found a bug?**  
   File an issue with:  
   - Description of the problem  
   - Steps to reproduce  
   - Expected vs. actual behavior  

2. **Have a research idea?**  
   Open a discussion thread with:  
   - Clear research question  
   - Physics basis for the question  
   - Potential validation methods  

3. **Want to contribute code?**  
   Follow the contribution process above and reference:  
   - `CONTRIBUTING.md` for guidelines  
   - `simulation/validation/` for validation scripts  

> **Final Note**: This repository is a **community asset**, not an individual project. Your contributions help advance our collective understanding of energy conversion physics. Let's build something meaningful together.
