# Setting up your laptop

Allow about 30 minutes, at home, a few days before the course. You need about 5 GB of free disk space and administrator rights are not required. The steps are the same on macOS, Windows and Linux except where marked.

Commands are typed into a terminal: **Terminal** on macOS and Linux, and **Miniforge Prompt** (installed in step 1) on Windows. Copy each command, paste it into the terminal and press Enter.

## 1. Install Miniforge

Miniforge installs Python together with `conda`, the tool that installs the packages the course uses. If you already have Anaconda or Miniconda you can skip this step and use it instead.

Download the installer for your computer from <https://conda-forge.org/download/>:

- **macOS (Apple silicon: M1, M2, M3, M4):** `Miniforge3-Darwin-arm64.sh`
- **macOS (Intel):** `Miniforge3-Darwin-x86_64.sh`
- **Windows:** `Miniforge3-Windows-x86_64.exe`
- **Linux:** `Miniforge3-Linux-x86_64.sh`

On **Windows**, double-click the `.exe` and accept the defaults ("Just me"). Afterwards, open **Miniforge Prompt** from the Start menu.

On **macOS and Linux**, open a terminal and run the installer you downloaded, for example:

```
bash ~/Downloads/Miniforge3-Darwin-arm64.sh
```

Press Enter to page through the licence, type `yes` to accept it, accept the suggested install location, and answer `yes` when asked whether to initialise the shell. Then **close the terminal and open a new one**. Your prompt now begins with `(base)`.

## 2. Download the tutorial suite

Download <https://github.com/EarthByte/GPlately-pyGMT-tutorials/archive/refs/heads/main.zip> (about 430 MB; on the repository page this is **Code > Download ZIP**). Unzip it into your Documents folder and rename the folder `GPlately-pyGMT-tutorials-main` to `GPlately-pyGMT-tutorials`, so that you have `Documents/GPlately-pyGMT-tutorials/` containing `Notebooks/`, `data/`, `course/` and `environment.yml`.

If you use git, you can clone the repository instead:

```
cd ~/Documents
git clone https://github.com/EarthByte/GPlately-pyGMT-tutorials.git
```

## 3. Create the course environment

In the terminal, go into the tutorial folder and create the environment from its `environment.yml` file. This downloads about 1.5 GB of packages and takes 5 to 15 minutes.

macOS and Linux:

```
cd ~/Documents/GPlately-pyGMT-tutorials
conda env create -f environment.yml
```

Windows (Miniforge Prompt):

```
cd %USERPROFILE%\Documents\GPlately-pyGMT-tutorials
conda env create -f environment.yml
```

When it finishes, activate the environment:

```
conda activate gplately-pygmt
```

The prompt now begins with `(gplately-pygmt)`. You need to activate the environment every time you open a new terminal for the course.

## 4. Run the setup check

Still in the tutorial folder, with the environment active:

```
python course/setup_check.py
```

The check takes a few minutes the first time, because it downloads the plate models (about 450 MB) into `gplately_data/` inside the tutorial folder. It ends with one of two lines:

- `READY: everything the course needs works on this laptop.` You are done.
- `NOT READY.` Look at the lines marked `FAIL` and at the list below.

It also writes a small test map, `course/setup_check_map.png`. Open it: you should see a world map with Hobart marked.

## 5. Try JupyterLab

```
jupyter lab
```

JupyterLab opens in your web browser. In the file panel on the left, open `Notebooks/` and double-click `A01_Hello_Deep_Time.ipynb`. Choose **Run > Run All Cells**. After about half a minute a map of the world at 50 million years ago appears near the bottom. To stop JupyterLab, close the browser tab and press Ctrl+C twice in the terminal.

## On the day

Bring your laptop charged, with its charger. To start:

macOS and Linux:

```
cd ~/Documents/GPlately-pyGMT-tutorials
conda activate gplately-pygmt
jupyter lab
```

Windows (Miniforge Prompt):

```
cd %USERPROFILE%\Documents\GPlately-pyGMT-tutorials
conda activate gplately-pygmt
jupyter lab
```

## If something fails

| What you see | What to do |
|---|---|
| `conda: command not found` (macOS, Linux) or `'conda' is not recognized` (Windows) | Close the terminal and open a new one. On Windows use **Miniforge Prompt**, not the ordinary Command Prompt |
| `conda env create` stops with a solver or download error | Run the same command again; downloads sometimes time out. On a university or company network, try from home |
| `CondaValueError: prefix already exists` | The environment was created earlier. Run `conda env update -f environment.yml --prune` instead |
| A `FAIL` line for a package | Check that the prompt shows `(gplately-pygmt)`; if not, run `conda activate gplately-pygmt` and run the check again |
| `GMTCLibNotFoundError` or the test map fails | Remove and recreate the environment: `conda env remove -n gplately-pygmt`, then repeat step 3 |
| A plate model fails to download | Run the check again later; it only downloads what is missing |
| The online services are not reachable | Only A02, G03 and I01 need them. They work on the day if the venue network allows it |
| `python: can't open file 'course/setup_check.py'` | You are not in the tutorial folder. Run the `cd` command from step 3 first |

If the check still says `NOT READY`, email the full output of the setup check to the course organiser before the course. On the day, notebook A02 runs on any laptop with Python and internet access, so nobody is left without something to do.
