# ⚙️ Cleburn's Repo Setup Notes

A personal reference for creating clean, consistent repositories for AI, data, and automation projects.

---

## 🧭 Directory Layout

### Baseline (all projects)
```
project-name/
├── data/
│   ├── raw/            # Original datasets (ignored by Git)
│   └── processed/      # Cleaned / transformed data (ignored by Git)
├── notebooks/          # Jupyter notebooks (.ipynb)
├── visuals/            # Exported plots and images
├── requirements.txt    # Pinned dependencies
├── .gitignore          # Copied from template
└── README.md
```

### Add as needed based on project type

| Directory / File | When to add | Examples |
|---|---|---|
| `src/` | CLI tools, apps with modular logic | amazon-ads-analytics |
| `config/` | YAML-driven settings, metro/campaign data | property-analyst-pro, amazon-ads-analytics |
| `tests/` | Any project with testable business logic | amazon-ads-analytics |
| `reports/` | Projects that output markdown/HTML reports | amazon-ads-analytics |
| `ml/` | Projects with trained models or artifacts | property-analyst-pro |
| `app.py` | Streamlit or web app entry point | property-analyst-pro |
| `run-report.sh` | Bash wrapper for conda + CLI execution | amazon-ads-analytics |

> 🔹 Keep `data/` local — Git tracks structure only, not datasets.
> 🔹 Add `.gitkeep` to gitignored directories that need to exist (e.g., `data/raw/`, `data/processed/`, `tests/`).

---

## 🧰 Environment Setup

### Conda
```bash
conda create -n projectname python=3.14
conda activate projectname
pip install pandas numpy matplotlib seaborn scipy jupyter
```

After installing project-specific packages:
```bash
pip freeze > requirements.txt
```

### VS Code + Jupyter
- Open project folder directly in **VS Code**.
- Set kernel → `Python (projectname)` for notebooks.
- Use `Shift + Enter` or `Run All` for full notebook execution.

---

## 📦 Git Workflow

### 1️⃣ Initialize Repo
```bash
cd ~/repos/project-name
git init
git add .
git commit -m "Initial commit"
```

### 2️⃣ Create Remote + Push
```bash
gh repo create cleburn/project-name --private --source=. --push
```

To make it public instead, swap `--private` for `--public`.

---

## 🚫 Ignore Rules

### Which Ignore File for What?

**Global (~/.gitignore_global):**
- Python caches (`__pycache__/`, `*.pyc`)
- Anaconda auto-folders (`anaconda_projects/`)
- IDE files (`.vscode/`, `.idea/`)
- Jupyter checkpoints (`.ipynb_checkpoints/`)
- OS files (`.DS_Store`, `Thumbs.db`)
- Logs and temp files (`*.log`, `.cache/`)

**Local (.gitignore per repo):**
- Data files (`data/raw/*`, `data/processed/*`)
- Large outputs (`*.csv`, `*.pkl`, `*.h5` if not sample data)
- Environment files (`*.env`, `secrets.yaml`)
- Database files (`db/*.db`)
- Model artifacts (`*.joblib`) unless intentionally versioned
- Project-specific build artifacts

**Template:** Copy `amazon-ads-analytics/.gitignore` as baseline for new repos.

---

## 🧠 Commit Style

Keep commit messages consistent and informative:
```
<scope>: <short description>
```

Common scopes:
| Scope | Use for |
|---|---|
| `setup` | Repo init, environment, config files |
| `analysis` | New analysis, metrics, visualizations |
| `ingest` | Data loading, format normalization |
| `config` | YAML changes, settings updates |
| `reports` | Output rendering, markdown/terminal reports |
| `ml` | Model training, predictions, artifacts |
| `cleanup` | Remove cache, fix structure, refactor |
| `docs` | README, workflow docs |
| `fix` | Bug fixes |

Examples:
```
setup: initialized repo with .gitignore and README
analysis: added scatterplots and probability section
ingest: handle split XLSX exports from Amazon
config: add Dallas metro with rent tiers
fix: correct ACoS calculation for zero-spend keywords
```

---

## 🖥️ Recommended Tools

- **VS Code** — daily development
- **Jupyter Notebook / Lab** — analysis & prototyping
- **Terminal** — version control and environment management

---

## ✅ Quick Setup Shortcut

### Notebook / EDA project
```bash
mkdir ~/repos/new-project && cd ~/repos/new-project
mkdir -p notebooks visuals data/raw data/processed
touch data/raw/.gitkeep data/processed/.gitkeep visuals/.gitkeep
touch README.md requirements.txt
cp ~/repos/amazon-ads-analytics/.gitignore .
```

### CLI / App project
```bash
mkdir ~/repos/new-project && cd ~/repos/new-project
mkdir -p src config tests notebooks visuals data/raw data/processed
touch data/raw/.gitkeep data/processed/.gitkeep tests/.gitkeep visuals/.gitkeep
touch README.md requirements.txt
cp ~/repos/amazon-ads-analytics/.gitignore .
```

---


> ✨ This setup keeps every project reproducible, portable, and GitHub-ready — with no clutter and clear visual documentation.
